import shutil
import pathlib

# Define source and target directories
target_dir = '/content/drive/MyDrive/Target/'
image_path = '/content/drive/MyDrive/resize/'

count = 0

# Iterate through binary classification labels (False and True)
for image_split in [False, True]:
    labels = list(data[data['class'] == image_split]['image_filename'])
    for label in labels:
        to_dir = pathlib.Path(target_dir) / str(image_split) / str(label)
        if not to_dir.is_dir():
            to_dir.parent.mkdir(parents=True, exist_ok=True)

        from_dir = pathlib.Path(image_path) / str(label)

        # Check if the source file exists before copying
        if from_dir.exists():
            shutil.copy2(str(from_dir), str(to_dir))
            count += 1

print(f'{count} images copied.')
