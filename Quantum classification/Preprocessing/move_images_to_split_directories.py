import pathlib
import shutil

# Define target directory
target_dir_name = 'target directory'
print(f"Creating directory: '{target_dir_name}'")

# Setup the directories and make the directories
target_dir = pathlib.Path(target_dir_name)
target_dir.mkdir(parents=True, exist_ok=True)

count = 0

# Move images into their respective directories
for image_split in label_splits.keys():
    for image_path in label_splits[image_split]:
        dest_dir = target_dir / image_split / image_path.parts[-2] / image_path.name
        if not dest_dir.parent.is_dir():
            dest_dir.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(image_path, dest_dir)
        count += 1

print(f'{count:.0f} images moved')
