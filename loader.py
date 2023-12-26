from __future__ import annotations

# System imports
import random, os
from typing import List, TypeAlias
from pathlib import Path
from enum import IntEnum

# Core imports
import tensorflow as tf
import numpy as np

# Helper imports
import pickle


def tf_seed(seed=0):
    np.random.seed(seed)  # numpy seed
    tf.random.set_seed(seed)  # tensorflow seed
    random.seed(seed)  # random seed
    os.environ['TF_DETERMINISTIC_OPS'] = '1'
    os.environ['TF_CUDNN_DETERMINISM'] = '1'
    os.environ['PYTHONHASHSEED'] = str(seed)


class DatasetSource(IntEnum):
    MSSPOOF = 1
    _3DMAD = 2
    CSMAD = 3
    REPLAY_ATTACK = 4
    OUR = 5
    CUMULATIVE = 6

    def dataset_path(self) -> Path:
        return {
            DatasetSource.MSSPOOF.value: Path('./datasets/msspoof'),
            DatasetSource._3DMAD.value: Path('./datasets/3dmad'),
            DatasetSource.CSMAD.value: Path('./datasets/csmad'),
            DatasetSource.REPLAY_ATTACK.value: Path('./datasets/replay_attack'),
            DatasetSource.OUR.value: Path('./datasets/our.array'),
        }.get(self.value, None)

    @classmethod
    def to_list(cls) -> List[DatasetSource]:
        return [DatasetSource.MSSPOOF,
                DatasetSource._3DMAD,
                DatasetSource.CSMAD,
                DatasetSource.REPLAY_ATTACK,
                DatasetSource.OUR]

    def model(self) -> tf.keras.Model:
        return {
            DatasetSource.MSSPOOF.value: tf.keras.models.load_model("./models/model_MSSpoof.h5"),
            DatasetSource._3DMAD.value: tf.keras.models.load_model("./models/model_3DMAD.h5"),
            DatasetSource.CSMAD.value: tf.keras.models.load_model("./models/model_CSMAD.keras"),
            DatasetSource.REPLAY_ATTACK.value: tf.keras.models.load_model("./models/model_Replay_Attack.h5"),
            DatasetSource.OUR.value: tf.keras.models.load_model("./models/model_our.h5"),
            DatasetSource.CUMULATIVE.value: tf.keras.models.load_model("./models/model_cumulative.keras"),
        }[self.value]


# Dataset type specification.
# Dataset consists of 4 numpy arrays:
# 1. Training data
# 2. Validation data
# 3. Training labels
# 4. Validation labels
Dataset: TypeAlias = (np.ndarray, np.ndarray, np.ndarray, np.ndarray)


class DatasetLoader:
    """
    Dataset loader class.
    """

    @staticmethod
    def _load_3dmad() -> Dataset:
        (X_train, X_test, y_train, y_test) = pickle.loads(
            open(DatasetSource._3DMAD.dataset_path(), "rb").read())
        return X_train, X_test, y_train, y_test

    @staticmethod
    def _load_csmad() -> Dataset:
        (X_train, X_test, y_train, y_test) = pickle.loads(
            open(DatasetSource.CSMAD.dataset_path(), "rb").read())
        # Cutting off the alpha channel
        X_train = X_train[..., :3]
        X_test = X_test[..., :3]
        return X_train, X_test, y_train, y_test

    @staticmethod
    def _load_our() -> Dataset:
        (X_train, X_test, y_train, y_test, _, _) = pickle.loads(
            open(DatasetSource.OUR.dataset_path(), "rb").read())
        return X_train, X_test, y_train, y_test

    @staticmethod
    def _load_replay_attack() -> Dataset:
        (X_train, X_test, y_train, y_test) = pickle.loads(
            open(DatasetSource.REPLAY_ATTACK.dataset_path(), "rb").read())
        return X_train, X_test, y_train, y_test

    @staticmethod
    def _load_msspoof() -> Dataset:
        (X_train, X_test, y_train, y_test) = pickle.loads(
            open(DatasetSource.MSSPOOF.dataset_path(), "rb").read())
        return X_train, X_test, y_train, y_test

    @staticmethod
    def load_multiple_sources(sources: List[DatasetSource],
                              verbose: bool = False,
                              shuffle: bool = False) -> Dataset:
        """
        Loads multiple datasets from the specified sources. The datasets are concatenated.

        :param sources: List of dataset sources.
        :param verbose: If True, prints the number of samples in each dataset.
        :param shuffle: If True, shuffles the dataset.

        :return: Dataset consisting of concatenated datasets from the specified sources.
        """
        assert len(sources) > 0, "At least one dataset source must be specified."
        X_train, X_test, y_train, y_test = DatasetLoader.load_dataset(sources[0])
        if verbose:
            print(f"Dataset {sources[0]}: {len(X_train)} training samples, {len(X_test)} testing samples loaded")

        for source in sources[1:]:
            (_X_train, _X_test, _y_train, _y_test) = DatasetLoader.load_dataset(source)
            X_train = np.concatenate((X_train, _X_train))
            X_test = np.concatenate((X_test, _X_test))
            y_train = np.concatenate((y_train, _y_train))
            y_test = np.concatenate((y_test, _y_test))
            if verbose:
                print(f"Dataset {source}: {len(_X_train)} training samples, {len(_X_test)} testing samples loaded")

        if shuffle:
            np.random.shuffle(X_train)
            np.random.shuffle(X_test)
            np.random.shuffle(y_train)
            np.random.shuffle(y_test)

        return X_train, X_test, y_train, y_test

    @staticmethod
    def load_dataset(dataset: DatasetSource) -> Dataset:
        """
        Loads the dataset from the specified source.
        """
        return {
            DatasetSource.MSSPOOF: DatasetLoader._load_msspoof,
            DatasetSource._3DMAD: DatasetLoader._load_3dmad,
            DatasetSource.CSMAD: DatasetLoader._load_csmad,
            DatasetSource.REPLAY_ATTACK: DatasetLoader._load_replay_attack,
            DatasetSource.OUR: DatasetLoader._load_our,
            DatasetSource.CUMULATIVE: lambda: DatasetLoader.load_multiple_sources(DatasetSource.to_list()),
        }[dataset]()
