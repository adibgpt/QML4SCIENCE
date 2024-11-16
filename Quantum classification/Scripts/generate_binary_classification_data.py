from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive')

import os
import pandas as pd
import shutil
import random
import pathlib

# Set the paths to your image directories for each class
class_0_dir = "/content/class0"
class_1_dir = "/content/class1"

# List all image files in each directory and extract just the filenames
class_0_images = [os.path.basename(filename) for filename in os.listdir(class_0_dir) if filename.endswith(".png")]
class_1_images = [os.path.basename(filename) for filename in os.listdir(class_1_dir) if filename.endswith(".png")]

# Create a DataFrame with the file paths and labels (False for class 0, True for class 1)
data = pd.DataFrame({
    'image_filename': class_0_images + class_1_images,
    'class_number': [0] * len(class_0_images) + [1] * len(class_1_images),
    'class': [False] * len(class_0_images) + [True] * len(class_1_images)
})

# Shuffle the DataFrame to randomize the order
data = data.sample(frac=1).reset_index(drop=True)

# Save the DataFrame to a CSV file with the specified headers
data.to_csv("binary_classification_data.csv", index=False, header=["image_filename", "class_number", "class"])

# Load the saved CSV for verification
data = pd.read_csv("/content/binary_classification_data.csv")
print(data.tail())
print(data['class'].value_counts())
