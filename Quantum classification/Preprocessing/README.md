
# Preprocessing Scripts

This folder contains scripts for preprocessing image datasets, including organizing images into train-test splits and moving them into corresponding directories. These scripts help streamline the dataset preparation for machine learning or computer vision tasks.

## Files and Usage

### 1. `import_libraries.py`
Imports all the necessary Python libraries for the preprocessing pipeline.

```python
import os
import shutil
import random
import pathlib
import pandas as pd
```

---

### 2. `read_and_process_csv.py`
Reads a CSV file, selects specific columns, and processes the data to create binary classification labels.

- **Usage**:
```python
data = pd.read_csv("URL_TO_CSV", usecols=[1, 2])
data['class'] = data['class_number'] == 1
print(data.head())
print(data['class'].value_counts())
```

---

### 3. `split_and_copy_images.py`
Splits images based on binary classification labels and copies them into train-test directories.

- **Usage**:
Update the source and target directories in the script before running.

```python
for image_split in [False, True]:
    # Process images for each class and split
```

---

### 4. `train_test_split.py`
Performs a train-test split on the dataset and organizes image paths into corresponding splits.

- **Parameters**:
  - `split`: Fraction of the dataset for testing (default: 30%).
  - `seed`: Random seed for reproducibility.

- **Usage**:
```python
label_splits = train_test_split(split=0.3, seed=42)
print(label_splits['Train'][0:10])
```

---

### 5. `move_images_to_split_directories.py`
Creates a target directory and moves images into train-test split subdirectories.

- **Usage**:
```python
for image_split in label_splits.keys():
    # Move images to respective directories
```

---

## Instructions
1. Clone this repository to your local machine.
2. Update the paths in each script to match your dataset directory structure.
3. Run the scripts sequentially to preprocess your dataset.

## Dependencies
Ensure the following Python libraries are installed:
- `os`
- `shutil`
- `random`
- `pathlib`
- `pandas`

---

## Directory Structure
```
preprocessing/
│
├── import_libraries.py
├── read_and_process_csv.py
├── split_and_copy_images.py
├── train_test_split.py
├── move_images_to_split_directories.py
```
