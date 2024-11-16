import os
import shutil
import pathlib

# Define target and source directories
target_dir = 'target directory'
image_path = 'image directory'

count = 0

# Split and copy images
for image_split in [False, True]:
    labels = list(data[data['class'] == image_split]['image_filename'])
    for label in labels:
        to_dir = pathlib.Path(os.path.join(target_dir, str(image_split), label))
        if not to_dir.parent.is_dir():
            to_dir.parent.mkdir(parents=True, exist_ok=True)
        from_dir = pathlib.Path(os.path.join(image_path, label))
        shutil.copy2(from_dir, to_dir)
        count += 1

print(f'{count:.0f} images copied')
