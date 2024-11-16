import zipfile
import os

# Directory containing the resized images
RESIZED_PATH = 'resized/'

# Name of the zip file
ZIP_FILENAME = 'resized_images.zip'

def zip_resized_images(directory, zip_filename):
    with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, directory)
                zipf.write(file_path, arcname=arcname)

# Usage
zip_resized_images(RESIZED_PATH, ZIP_FILENAME)
