
# Quantum Classification

This repository is designed for quantum-classical hybrid machine learning for image classification. It is organized into the following folders and files:

## Folder Structure

### **1. `Noisy dataset/`**
This folder contains scripts and utilities for augmenting datasets by adding noise to images. This helps create robust machine learning models by simulating real-world scenarios with noise.

- **Key Features**:
  - Resizing images.
  - Converting images to grayscale.
  - Adding Gaussian and Poisson noise.
  - Compressing noisy datasets into `.zip` files.

---

### **2. `Preprocessing/`**
Contains scripts for processing raw image datasets into formats suitable for machine learning. These include splitting datasets, labeling images, and creating train-test splits.

- **Key Features**:
  - Reading CSV files with image metadata.
  - Randomly splitting datasets into training and testing sets.
  - Organizing and copying images into structured folders.

[!With-cavity](https://github.com/adibgpt/QML4SCIENCE/blob/f4b05cb60f6b13f603c1bf623927663817612952/Images/With-cavity/1%20(1).png)

---

### **3. `Scripts/`**
Contains scripts for building and training a classical neural network using PyTorch. These scripts include everything from data preparation to model training and evaluation.

- **Key Features**:
  - Data loading and visualization.
  - Training a classical Perceptron model.
  - Evaluating model performance using metrics and confusion matrices.
  - Visualizing predictions on test data.

---

### **4. `Scripts-quantum/`**
This folder includes scripts for building, training, and evaluating a hybrid quantum-classical neural network using PyTorch and Qiskit.

- **Key Features**:
  - Building quantum neural networks (QNNs) with Qiskit.
  - Creating hybrid models that combine classical layers with quantum layers.
  - Training the hybrid model using PyTorch.
  - Visualizing training loss and accuracy.
  - Evaluating the hybrid model and visualizing predictions.

---

### **5. `LICENSE`**
Specifies the terms and conditions for using and distributing the repository.

---

### **6. `README.md`**
Provides detailed documentation for the repository, including the folder structure, descriptions of scripts, and instructions for usage.

---

## Instructions for Use

### **1. Setting Up the Environment**
Install the required dependencies for classical and quantum models:
```bash
pip install torch torchvision qiskit qiskit-machine-learning torchviz matplotlib
```

### **2. Preprocessing**
Use the scripts in the `Preprocessing/` folder to organize your dataset:
- Split data into training and testing sets.
- Copy and organize images into structured folders.

### **3. Classical Model**
Use the scripts in the `Scripts/` folder to:
- Train a classical neural network (Perceptron).
- Visualize training metrics and predictions.

### **4. Hybrid Quantum-Classical Model**
Use the scripts in the `Scripts-quantum/` folder to:
- Build and train a quantum-classical hybrid neural network.
- Visualize quantum neural network properties.
- Evaluate the hybrid model on the test dataset.

### **5. Noise Augmentation**
Use the scripts in the `Noisy dataset/` folder to:
- Add Gaussian or Poisson noise to images.
- Create and compress noisy datasets for further training.

---

## Dependencies
This repository uses the following libraries:
- **PyTorch**: For building and training neural networks.
- **Qiskit**: For quantum computing and building quantum neural networks.
- **Torchvision**: For image processing.
- **Matplotlib**: For visualizations.
- **Numpy**: For numerical computations.

---

## Outputs
- **Trained Models**: Saved as `.pt` files.
- **Visualizations**:
  - Quantum neural network density matrices.
  - Training convergence (loss and accuracy).
  - Predictions on test data.
- **Augmented Datasets**: Datasets with added noise, saved as `.zip` files.

---

This project showcases a comprehensive workflow for both classical and quantum machine learning in image classification tasks.
