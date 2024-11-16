import os
import random
import numpy as np
import pandas as pd

from skimage import io
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score

import matplotlib.pyplot as plt
import seaborn as sns

# Function to create a confusion matrix heatmap
def matrix_confusion(yt, yp):
    data = {'Y_Real': yt,
            'Y_Prediccion': yp}

    df = pd.DataFrame(data, columns=['Y_Real', 'Y_Prediccion'])
    confusion_matrix = pd.crosstab(df['Y_Real'], df['Y_Prediccion'], rownames=['Real'], colnames=['Predicted'])
    sns.heatmap(confusion_matrix, annot=True, fmt='g')

    plt.show()

# Load and explore data
data = pd.read_csv("/content/binary_classification_data.csv")
data.info()
print(data['class_number'].value_counts(sort=False))

# Target variable
Y = data['class_number']
print(data['image_filename'])

# Path to resized images
path = "/content/drive/MyDrive/resize/"

# Load images as grayscale
%time img = data['image_filename'].apply(lambda x: io.imread(path + x, as_gray=True))

# Check dimensions of images
print(img.shape)
print(img[0].shape)

# Stack images into a single array
IMG = np.stack(img, axis=0)
print(IMG.shape)

# Flatten images for training
X = IMG.reshape(IMG.shape[0], -1)
print(X.shape)
