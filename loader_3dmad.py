# System imports
import random, os

# Core imports
import tensorflow as tf
import numpy as np
import cv2

# Sklearn imports
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, roc_curve, auc
from skimage.io import imread_collection

# Display imports
from matplotlib import pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size

# Helper imports
from imutils import paths
import pickle
import shutil
import itertools
from itertools import cycle

input_width = 32
input_height = 32
n_channels = 3
dim = (input_width, input_height) # dimensionality

def tf_seed(seed=0):
    np.random.seed(seed)  # numpy seed
    tf.random.set_seed(seed)  # tensorflow seed
    random.seed(seed)  # random seed
    os.environ['TF_DETERMINISTIC_OPS'] = '1'
    os.environ['TF_CUDNN_DETERMINISM'] = '1'
    os.environ['PYTHONHASHSEED'] = str(seed)

def resize_normalize_image(image, value=255):
    image = cv2.resize(image, dim)
    return image / value

def get_file_name(path):
    """
    get_file_name returns a file name given a path
    """
    base = os.path.basename(path)
    return os.path.splitext(base)[0]

def get_images(directories, mask=True, balance_dataset=True, undersampling=False):
    image_list = []
    label_list = []
    classes = 0
    images_per_class=[]
    tf_seed()

    #for each input directory
    for i in directories:
        list_images = [f for f in os.listdir(i) if os.path.isfile(os.path.join(i, f))]
        images_number = len(list_images)
        random.Random(20).shuffle(list_images)
        
        # if we use undersampling
        if undersampling:
            images_number = images_number if ((len(images_per_class) == 0) or (images_number <= images_per_class[-1]))  else images_per_class[-1]
        
        # to fill tensors we inizialise them
        X = np.empty((images_number, input_width, input_height, n_channels))
        L = np.empty((images_number))
        ipp = 0
        
        for im_name in list_images:
            im=os.path.join(i, im_name)
            # to get "balanced dataset" using undersampling method
            if (balance_dataset and undersampling) and len(images_per_class)  and ipp == images_per_class[-1]:
                break

            image = cv2.imread(im)
            image = resize_normalize_image(image, value=255)
        
            if mask:
                mask_name = os.path.join(
                    i, "mask", get_file_name(im) + "_mask.npy")
                image_mask = np.load(mask_name)
                image_mask = resize_normalize_image(image_mask, value=2048)  #since 3DMAD mask is rgb 2^1        

            X[ipp, ..., :3] = image # each original image is rgb
            
            if mask:
                print(np.shape(image_mask))
                X[ipp, ..., 3] = image_mask # each mask can be n_channels - 3

            L[ipp] = classes  # 0 for real, 1 for fake for binary classification

            ipp += 1
        
        # check if the current class has lower images than the before
        # in this case we undersample the majority class randomly removing elements
        # we will have a balanced dataset: same images for all the classes

        if balance_dataset and undersampling:
            if len(images_per_class) and ipp < images_per_class[-1]:
                left_shift = 0
                
                for i in range(0, len(images_per_class)):
                    diff = images_per_class[i] - ipp

                    for j in range(0, diff):
                        random_index = np.random.randint(left_shift, images_per_class[i] - j)
                        image_list.pop(random_index)
                        label_list.pop(random_index)

                    left_shift += images_per_class[i] - diff

        if undersampling or balance_dataset==False:
            for image in X:
                image_list.append(image)

            for label in L:
                label_list.append(label)
        else:
            image_array=[]
            label_array=[]
            
            for image in X:
                image_array.append(image)

            image_list.append(np.array(image_array, dtype="float"))
 
            for label in L:
                label_array.append(label)
            
            label_list.append(label_array)

        if undersampling or balance_dataset==False:
            images_per_class.append(ipp)
        else:
            images_per_class.append(images_number)

        classes += 1

    #offline augmentation
    if balance_dataset and undersampling==False:
        _max = np.max((images_per_class)) #[4k,3k,2k,1k]

        for j in range(0, len(images_per_class)):  #[[4k], [4k], [4k], [4k]]
            if images_per_class[j] < _max:
                diff= _max - images_per_class[j] #how many images to generate

                image_array=image_list[j]   #[3k]
                label_array=label_list[j]   #[3k]

                new_image_array=[]
             

                # use ImageDataGenerator 
                offline_generator = tf.keras.preprocessing.image.ImageDataGenerator(rotation_range=20, zoom_range=0.15,
                    width_shift_range=0.2, height_shift_range=0.2, shear_range=0.15,
                    horizontal_flip=True, fill_mode="constant")


                offline_generator = offline_generator.flow(image_array, batch_size=1, seed=20)

                # generate the reamining images respect the majority class, to balance the dataset
                generated_images=0
                while generated_images < diff:     
                    for i in range(0,len(offline_generator)):
                        if generated_images == diff:
                            break
                        batch = next(offline_generator)
                        new_image_array.append(batch[0])
                        label_array.append(j)
                        generated_images += 1

                print(generated_images)
                image_list[j]=np.append(image_list[j], new_image_array, axis=0)

                # image_list and label_list were of type [[...], [...]] for attack and bonafide classes
                # we need a final array of type [image1,image2,...] for images and [0,1,...] for labels

            new_image_list= np.empty((0, final_x, final_y, n_channels))
            new_label_list=[]


        for class_value_array in image_list:
            new_image_list = np.vstack((new_image_list,class_value_array))

        for class_value_array in label_list:
            new_label_list += class_value_array

        image_list = new_image_list
        label_list = new_label_list

        print(image_list.shape)
        print(len(label_list))
      
    # create the one-hot encoded vector: [0 1], [1 0]
    le = LabelEncoder()
    labels = le.fit_transform(label_list)
    labels = tf.keras.utils.to_categorical(labels, 2)

    if type(image_list) is np.ndarray:
        return image_list, labels, le
    
    return np.array(image_list, dtype="float"), labels, le
