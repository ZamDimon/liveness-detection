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
