import shutil
import pathlib

# Assuming label_splits is a dictionary containing image splits

# Create target directory path
target_dir_name = '/content/drive/MyDrive/Images_Random_Split/'
print(f"Creating directory: '{target_dir_name}'")

# Setup the directories & Make the directories
target_dir = pathlib.Path(target_dir_name)
target_dir.mkdir(parents=True, exist_ok=True)

count = 0

# Move images into their respective directories
for image_split, image_paths in label_splits.items():
    for image_path in image_paths:
        dest_dir = target_dir / str(image_split) / image_path.parts[-2] / image_path.name
        if not dest_dir.parent.is_dir():
            dest_dir.parent.mkdir(parents=True, exist_ok=True)

        # Check if the source file exists before copying
        if image_path.exists():
            print(f"Copying from: {image_path} to {dest_dir}")
            shutil.copy2(str(image_path), str(dest_dir))
            count += 1
        else:
            print(f"Source file not found: {image_path}")

print(f'{count} images moved.')
