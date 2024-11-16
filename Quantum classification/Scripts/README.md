
# Scripts for Binary Classification and Image Processing

This folder contains scripts for preprocessing image datasets, training models, and visualizing results for binary classification tasks. The scripts use Perceptron models and various tools to process, visualize, and evaluate the data.

## Files and Usage

### 1. `generate_binary_classification_data.py`
Generates a shuffled DataFrame from two directories containing images of different classes. Saves the data as a CSV file.

- **Usage**:
```python
# Process images from class directories and save to CSV
data = pd.DataFrame({'image_filename': ..., 'class_number': ..., 'class': ...})
data.to_csv("binary_classification_data.csv", index=False)
```

---

### 2. `copy_images_to_target.py`
Copies images from a source directory to a target directory based on binary classification labels.

- **Usage**:
```python
# Specify source and target directories
target_dir = '/path/to/target'
image_path = '/path/to/source'

# Copy images based on classification labels
shutil.copy2(...)
```

---

### 3. `train_test_split.py`
Performs a train-test split for images and organizes their paths into corresponding splits.

- **Usage**:
```python
# Split the dataset into train and test
label_splits = train_test_split(split=0.3, seed=42)
```

---

### 4. `verify_train_test_split.py`
Verifies the train-test split and ensures no overlap between training and testing datasets.

- **Usage**:
```python
# Verify and count overlapping elements
common_elements = counter1 & counter2
```

---

### 5. `move_images_to_random_split.py`
Creates a target directory and moves images into subdirectories based on train-test splits.

- **Usage**:
```python
# Move images to train-test directories
shutil.copy2(...)
```

---

### 6. `prepare_data_and_train_perceptron.py`
Prepares image data for training by flattening grayscale images into feature vectors and targets. Trains a Perceptron model for binary classification.

- **Usage**:
```python
# Prepare the feature matrix and target
X = IMG.reshape(IMG.shape[0], -1)

# Train Perceptron
model_p.fit(X_train, y_train)
```

---

### 7. `visualize_image_samples.py`
Visualizes a grid of randomly selected images from each class.

- **Usage**:
```python
# Plot a grid of images
plt.imshow(...)
```

---

### 8. `train_and_evaluate_perceptron.py`
Trains multiple Perceptron models with varying configurations and evaluates their performance.

- **Usage**:
```python
# Train Perceptron and evaluate
model_p.fit(X_train, y_train)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

## Instructions
1. Clone this repository to your local machine.
2. Update the paths in each script to match your dataset directory structure.
3. Run the scripts sequentially for preprocessing, training, and evaluation.

## Dependencies
Ensure the following Python libraries are installed:
- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `skimage`

## Directory Structure
```
scripts/
│
├── generate_binary_classification_data.py
├── copy_images_to_target.py
├── train_test_split.py
├── verify_train_test_split.py
├── move_images_to_random_split.py
├── prepare_data_and_train_perceptron.py
├── visualize_image_samples.py
├── train_and_evaluate_perceptron.py
```

---

## Outputs
- Binary classification dataset (`binary_classification_data.csv`).
- Visualizations of image samples.
- Train and test accuracy metrics.
- Confusion matrix heatmaps for model predictions.
