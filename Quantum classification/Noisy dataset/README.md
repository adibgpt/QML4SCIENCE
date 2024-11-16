
# Noisy Dataset Processing Scripts

This repository contains Python scripts for processing image datasets, including resizing, converting to grayscale, adding noise (Gaussian and Poisson), and zipping the processed images. These scripts are designed to streamline preprocessing for machine learning or computer vision tasks.

## Files and Usage

### 1. `install_dependencies.py`
This script installs the required Python libraries.

```bash
!pip install Pillow
!pip install opencv-python
!pip install numpy
```

### 2. `resize_images.py`
Resizes images in a specified directory to a target size (default: 260x260 pixels).

- **Usage**:
  Update the paths for training and test datasets before running.

```python
resize_images(TEST_PATH)
resize_images(TRAINING_PATH)
```

### 3. `resize_to_grayscale.py`
Resizes images and converts them to grayscale, saving them in a specified directory.

- **Usage**:
  Update the paths for training, validation, and test datasets before running.

```python
convert_and_resize_images(TEST_PATH)
convert_and_resize_images(TRAINING_PATH)
convert_and_resize_images(VALIDATION_PATH)
```

### 4. `add_gaussian_noise.py`
Adds Gaussian noise to images in a directory and saves the noisy versions.

- **Parameters**:
  - `noise_stddev`: Adjust the standard deviation of the noise as needed.

- **Usage**:
```python
add_gaussian_noise_to_images(RESIZED_PATH)
```

### 5. `add_poisson_noise.py`
Adds Poisson noise to images in a directory and saves the noisy versions.

- **Usage**:
```python
add_poisson_noise_to_images(RESIZED_PATH)
```

### 6. `zip_images.py`
Zips all images in a directory into a single `.zip` file.

- **Usage**:
```python
zip_resized_images(RESIZED_PATH, ZIP_FILENAME)
```

## Directory Structure
```
Noisy_dataset/
│
├── install_dependencies.py
├── resize_images.py
├── resize_to_grayscale.py
├── add_gaussian_noise.py
├── add_poisson_noise.py
├── zip_images.py
```

## Instructions
1. Clone this repository to your local machine.
2. Update the paths in each script to match your dataset directory structure.
3. Run the scripts in the appropriate order for your preprocessing pipeline.

## Dependencies
Ensure the following Python libraries are installed:
- Pillow
- OpenCV
- NumPy
