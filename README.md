# Liveness detection

## Introduction

Code and materials for a research paper about liveness detection.

Model training can be found in the [Andrea Maranesi's research](https://github.com/andreamaranesi/Spoofing-Attack-Detection-2022/tree/main).

## Confusion matrices

### MSSpoof model on MSSpoof dataset

|   |   |
|---|---|
| 757 | 62 |
| 32 | 787 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.96 | 0.93 |
| **Recall** | 0.92 | 0.96 |
| **F1 score** | 0.94 | 0.94 |

### MSSpoof model on 3DMAD dataset

|   |   |
|---|---|
| 300 | 60 |
| 231 | 129 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.56 | 0.68 |
| **Recall** | 0.83 | 0.36 |
| **F1 score** | 0.67 | 0.47 |

### MSSpoof model on CSMAD dataset

|   |   |
|---|---|
| 192 | 216 |
| 0 | 408 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 1.0 | 0.65 |
| **Recall** | 0.47 | 1.0 |
| **F1 score** | 0.64 | 0.79 |

### MSSpoof model on Replay Attack dataset

|   |   |
|---|---|
| 518 | 444 |
| 361(?) | 607 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.59 | 0.58 |
| **Recall** | 0.54 | 0.63 |
| **F1 score** | 0.56 | 0.6 |

### MSSpoof model on our dataset

|   |   |
|---|---|
| 350 | 859 |
| 314 | 895 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.53 | 0.51 |
| **Recall** | 0.29 | 0.74 |
| **F1 score** | 0.37 | 0.6 |

### 3DMAD model on MSSpoof dataset

|   |   |
|---|---|
| 265 | 554 |
| 93 | 726 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.74 | 0.57 |
| **Recall** | 0.32 | 0.89 |
| **F1 score** | 0.45 | 0.69 |

### 3DMAD model on 3DMAD dataset

|   |   |
|---|---|
| 360 | 0 |
| 0 | 360 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 1.0 | 1.0 |
| **Recall** | 1.0 | 1.0 |
| **F1 score** | 1.0 | 1.0 |

### 3DMAD model on CSMAD dataset

|   |   |
|---|---|
| 298 | 110 |
| 1 | 407 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 1.0 | 0.79 |
| **Recall** | 0.73 | 1.0 |
| **F1 score** | 0.84 | 0.88 |

### 3DMAD model on Replay Attack dataset

|   |   |
|---|---|
| 456 | 506 |
| 99 | 863 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.82 | 0.63 |
| **Recall** | 0.47 | 0.9 |
| **F1 score** | 0.6 | 0.74 |

### 3DMAD model on our dataset

|   |   |
|---|---|
| 455 | 754 |
| 23 | 1186 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.95 | 0.61 |
| **Recall** | 0.38 | 0.98 |
| **F1 score** | 0.54 | 0.75 |

### CSMAD model on MSSpoof dataset

|   |   |
|---|---|
| 738 | 81 |
| 736 | 83 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.5 | 0.51 |
| **Recall** | 0.9 | 0.1 |
| **F1 score** | 0.64 | 0.17 |

### CSMAD model on 3DMAD dataset

|   |   |
|---|---|
| 271 | 89 |
| 328 | 32 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.45 | 0.26 |
| **Recall** | 0.75 | 0.09 |
| **F1 score** | 0.56 | 0.13 |

### CSMAD model on CSMAD dataset

|   |   |
|---|---|
| 408 | 0 |
| 316 | 92 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.56 | 1.0 |
| **Recall** | 1.0 | 0.23 |
| **F1 score** | 0.72 | 0.37 |

### CSMAD model on Replay attack dataset

|   |   |
|---|---|
| 889 | 73 |
| 809 | 153 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.52 | 0.68 |
| **Recall** | 0.92 | 0.16 |
| **F1 score** | 0.66 | 0.26 |

### CSMAD model on our dataset

|   |   |
|---|---|
| 751 | ? |
| 733 | ? |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.51 | 0.51 |
| **Recall** | 0.62 | 0.39 |
| **F1 score** | 0.56 | 0.44 |

### Replay attack model on MSSpoof dataset

|   |   |
|---|---|
| 50 | 769 |
| 20 | 799 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.71 | 0.51 |
| **Recall** | 0.06 | 0.98 |
| **F1 score** | 0.11 | 0.67 |

### Replay attack model on 3DMAD dataset

|   |   |
|---|---|
| 360 | 0 |
| 250 | 110 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.59 | 1.0 |
| **Recall** | 1.0 | 0.31 |
| **F1 score** | 0.74 | 0.47 |

### Replay attack model on CSMAD dataset

|   |   |
|---|---|
| 408 | 0 |
| 171 | 237 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.7 | 1.0 |
| **Recall** | 1.0 | 0.58 |
| **F1 score** | 0.82 | 0.73 |

### Replay attack model on Replay attack dataset

|   |   |
|---|---|
| 894 | 68 |
| 23 | 939 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.97 | 0.93 |
| **Recall** | 0.93 | 0.98 |
| **F1 score** | 0.95 | 0.95 |

### Replay attack model on our dataset

|   |   |
|---|---|
| 632 | 577 |
| 274 | 935 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.7 | 0.62 |
| **Recall** | 0.52 | 0.77 |
| **F1 score** | 0.6 | 0.69 |

### Our model on MSSpoof dataset

|   |   |
|---|---|
| 107 | 712 |
| 26 | 793 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.8 | 0.53 |
| **Recall** | 0.13 | 0.97 |
| **F1 score** | 0.22 | 0.69 |

### Our model on 3DMAD dataset

|   |   |
|---|---|
| 360 | 0 |
| 348 | 12 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.51 | 1.0 |
| **Recall** | 1.0 | 0.03 |
| **F1 score** | 0.68 | 0.06 |

### Our model on CSMAD dataset

|   |   |
|---|---|
| 408 | 0 |
| 171 | 237 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.7 | 1.0 |
| **Recall** | 1.0 | 0.58 |
| **F1 score** | 0.82 | 0.73 |

### Our model on Replay attack dataset

|   |   |
|---|---|
| 941 | 21 |
| 565 | 397 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.62 | 0.95 |
| **Recall** | 0.98 | 0.41 |
| **F1 score** | 0.76 | 0.57 |

### Our model on our dataset

|   |   |
|---|---|
| 1092 | 117 |
| 278 | 931 |

| | Bonafide  | Attacker  |
| --- |---|---|
| **Precision** | 0.8 | 0.89 |
| **Recall** | 0.9 | 0.77 |
| **F1 score** | 0.85 | 0.83 |
