import os
import cv2
import numpy as np

# Directory containing the resized images
RESIZED_PATH = 'resized/'

# Standard deviation for Gaussian noise (adjust as needed)
noise_stddev = 30

def add_gaussian_noise(image, stddev):
    noisy_image = image + np.random.normal(0, stddev, image.shape).astype(np.uint8)
    noisy_image = np.clip(noisy_image, 0, 255)  # Ensure pixel values are within the valid range
    return noisy_image

def add_gaussian_noise_to_images(directory):
    for i, filename in enumerate(os.listdir(directory)):
        if filename.endswith('.png'):
            print(f'{i}: {filename}')
            image_path = os.path.join(directory, filename)
            image = cv2.imread(image_path)
            noisy_image = add_gaussian_noise(image, noise_stddev)
            noisy_image_path = os.path.join(directory, f'gaussian_noisy_{filename}')
            cv2.imwrite(noisy_image_path, noisy_image)

# Usage
add_gaussian_noise_to_images(RESIZED_PATH)
