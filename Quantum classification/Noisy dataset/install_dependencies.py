import os

# Define the directory structure and file path
base_dir = "/mnt/data/Noisy_dataset"
file_path = os.path.join(base_dir, "install_dependencies.py")

# Create the directory if it does not exist
os.makedirs(base_dir, exist_ok=True)

# Script content for install_dependencies.py
install_dependencies_code = """
# Script to install necessary Python libraries
!pip install Pillow
!pip install opencv-python
!pip install numpy
"""

# Write the code to the file
with open(file_path, "w") as file:
    file.write(install_dependencies_code)

file_path
