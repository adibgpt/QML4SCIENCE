import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

TRAINING_PATH = 'training/'
VALIDATION_PATH = 'validation/'
TEST_PATH = 'test/'

RESIZED_PATH = 'resized/'  # Define a new directory for resized grayscale images

def convert_and_resize_images(directory):
    for i, filename in enumerate(os.listdir(directory)):
        if filename.endswith('.png'):
            print(f'{i}: {filename}')
            # Open the image file
            with Image.open(os.path.join(directory, filename)) as img:
                # Convert the image to grayscale
                img_gray = img.convert('L')
                # Resize the grayscale image to 260x260 pixels
                img_resized = img_gray.resize((260, 260))
                # Save the resized grayscale image with a new name in the RESIZED_PATH
                resized_filename = os.path.join(RESIZED_PATH, f'resized_gray_{filename}')
                img_resized.save(resized_filename)

# Usage
convert_and_resize_images(TEST_PATH)
convert_and_resize_images(TRAINING_PATH)
convert_and_resize_images(VALIDATION_PATH)
