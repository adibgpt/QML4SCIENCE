import os
import cv2
import numpy as np

# Directory containing the resized images
RESIZED_PATH = 'resized/'

def add_poisson_noise(image):
    # Generate Poisson noise for each channel separately
    noisy_image = np.random.poisson(image).astype(np.uint8)
    return noisy_image

def add_poisson_noise_to_images(directory):
    for i, filename in enumerate(os.listdir(directory)):
        if filename.endswith('.png'):
            print(f'{i}: {filename}')
            image_path = os.path.join(directory, filename)
            image = cv2.imread(image_path)
            noisy_image = add_poisson_noise(image)
            noisy_image_path = os.path.join(directory, f'poisson_noisy_{filename}')
            cv2.imwrite(noisy_image_path, noisy_image)

# Usage
add_poisson_noise_to_images(RESIZED_PATH)
