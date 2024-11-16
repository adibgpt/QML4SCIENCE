import os
from PIL import Image
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

TRAINING_PATH = 'training/'
TEST_PATH = 'test/'

RESIZED_PATH = 'resized/'  # Define a new directory for resized images

def resize_images(directory, target_size=(260, 260)):
    for i, filename in enumerate(os.listdir(directory)):
        if filename.endswith('.png'):
            print(f'{i}: {filename}')
            # Open the image file
            with Image.open(os.path.join(directory, filename)) as img:
                # Resize the image to the specified dimensions
                img_resized = img.resize(target_size)
                # Save the resized image with a new name in the RESIZED_PATH
                resized_filename = os.path.join(RESIZED_PATH, f'resized_{filename}')
                img_resized.save(resized_filename)

# Usage
resize_images(TEST_PATH)
resize_images(TRAINING_PATH)
