
# Quantum Classification

This repository is designed for quantum-classical hybrid machine learning for image classification. It is organized into the following folders and files:

[Direct Numerical Simulation of Airfoil with Vortex Trapping Cavity](https://github.com/adibgpt/QML4SCIENCE/blob/fcfcfeed1326bd9a24d81339262e2a0dcf8590bb/Videos/Direct%20numerical%20simulation%20of%20airfoil%20with%20vortex%20trapping%20cavity%20%20Penlized%20Vortex%20particle%20method.mp4)

[Direct Numerical Simulation of Airfoil without Vortex Trapping Cavity](https://github.com/adibgpt/QML4SCIENCE/blob/8dacc969cc72f515afe90a578398090ff9a68cda/Videos/Direct%20numerical%20simulation%20of%20the%20airfoil%20-%20Penalized%20vortex%20particle%20method.mp4)

[Turbulent channel flow](https://github.com/adibgpt/QML4SCIENCE/blob/a45f879991c22f3d789fcbeb9532860eb58e9578/Videos/Turbulent%20channel%20flow%20(Direct%20Numerical%20Simulation).mp4)

[DNS of CO2 Seqestration (Ra=16000)](https://github.com/adibgpt/QML4SCIENCE/blob/55fdfa087130a857343b852d210f2880a2ce8d3d/Videos/DNS%20of%20CO2%20Seqestration%20(Ra%3D16000)%20(Fortran%20%2B%20MatLab).mp4)

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

![cavity](https://github.com/adibgpt/QML4SCIENCE/blob/0ff590561a991e88525bf6ad6bb321c5a4a1b59b/Images/snapshots.png)

- **Key Features**:
  - Reading CSV files with image metadata.
  - Randomly splitting datasets into training and testing sets.
  - Organizing and copying images into structured folders.


![cavity](https://github.com/adibgpt/QML4SCIENCE/blob/23639223bddb2b2243a006426ac530c4479204f3/Images/With-cavity/1%20(1).png) 
![cavity](https://github.com/adibgpt/QML4SCIENCE/blob/6252f95658bde1b38eba89bdb7029b43f1556583/Images/Without-cavity/1%20(1).png)

---

### **3. `Scripts/`**
Contains scripts for building and training a classical neural network using PyTorch. These scripts include everything from data preparation to model training and evaluation.

![cavity](https://github.com/adibgpt/QML4SCIENCE/blob/21036fe1a95de665d9b709fd798cb74b240d0f28/Images/with-without%20cavity.png)

- **Key Features**:
  - Data loading and visualization.
  - Training a classical Perceptron model.
  - Evaluating model performance using metrics and confusion matrices.
  - Visualizing predictions on test data.

![cavity](https://github.com/adibgpt/QML4SCIENCE/blob/54cb93745caacb9a4179c6bd7c9e3f6fe727ec0e/Images/confusion%20matrix-perceptron.png)

---

### **4. `Scripts-quantum/`**
This folder includes scripts for building, training, and evaluating a hybrid quantum-classical neural network using PyTorch and Qiskit.

![cavity](https://github.com/adibgpt/QML4SCIENCE/blob/1290ab0dadb03850ff7c6e3210181ce25c748a63/Images/Density%20matrix.png)

- **Key Features**:
  - Building quantum neural networks (QNNs) with Qiskit.
  - Creating hybrid models that combine classical layers with quantum layers.
  - Training the hybrid model using PyTorch.
  - Visualizing training loss and accuracy.
  - Evaluating the hybrid model and visualizing predictions.

![cavity](https://github.com/adibgpt/QML4SCIENCE/blob/5c6c31a7a44c4f59aabbe7cacc3477d4d965eaae/Images/prediction.png)

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
