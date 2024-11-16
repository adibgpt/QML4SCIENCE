
# Scripts for Quantum-Classical Hybrid Neural Networks

This folder contains scripts for building, training, and evaluating hybrid quantum-classical neural networks using Qiskit and PyTorch.

## Files and Usage

### 1. `install_dependencies.py`
Installs the necessary Python libraries for quantum computing and machine learning.

- **Usage**:
```bash
! pip install torchviz
! pip install qiskit
! pip install qiskit_machine_learning
! pip install qiskit-aer
```

---

### 2. `import_libraries.py`
Imports all required libraries for PyTorch, Qiskit, and quantum machine learning.

- **Includes**:
  - PyTorch modules for neural networks.
  - Qiskit modules for quantum circuits and machine learning.

---

### 3. `load_and_visualize_data.py`
Loads image data for training and testing using PyTorch's `DataLoader`. It also visualizes a sample of images.

- **Usage**:
```python
train_loader = DataLoader(train_data, shuffle=True, batch_size=1)
test_loader = DataLoader(test_data, shuffle=True, batch_size=1)
```

---

### 4. `create_and_visualize_qnn.py`
Defines and visualizes a quantum neural network (QNN) using Qiskit. It computes the QNN's density matrix and entanglement properties.

- **Usage**:
```python
qnn = create_qnn()
rho_01 = DensityMatrix.from_instruction(qnn.circuit.bind_parameters(params))
```

---

### 5. `build_hybrid_model.py`
Builds a hybrid neural network combining classical convolutional layers and a QNN in PyTorch.

- **Key Components**:
  - Convolutional layers.
  - Quantum layer using `TorchConnector`.

---

### 6. `train_hybrid_model.py`
Trains the hybrid model using the Adam optimizer and cross-entropy loss.

- **Usage**:
```python
optimizer = optim.Adam(model.parameters(), lr=0.00001)
loss_func = CrossEntropyLoss()
```

---

### 7. `plot_training_convergence.py`
Visualizes the training process by plotting loss and accuracy over epochs.

- **Output**:
  - A plot showing loss and accuracy trends.

---

### 8. `evaluate_hybrid_model.py`
Evaluates the trained hybrid model on test data and computes performance metrics such as loss and accuracy.

- **Usage**:
```python
model1.load_state_dict(torch.load("model.pt"))
```

---

### 9. `visualize_predictions.py`
Visualizes the model's predictions on test samples with corresponding images.

- **Output**:
  - A grid of test images with predicted labels.

---

## Instructions
1. Clone this repository to your local machine.
2. Update the paths in each script to match your dataset structure.
3. Run the scripts sequentially to build, train, and evaluate the hybrid model.

## Dependencies
Ensure the following Python libraries are installed:
- `torch`
- `torchvision`
- `qiskit`
- `qiskit-machine-learning`
- `qiskit-aer`
- `matplotlib`
- `numpy`

## Directory Structure
```
Scripts-quantum/
│
├── install_dependencies.py
├── import_libraries.py
├── load_and_visualize_data.py
├── create_and_visualize_qnn.py
├── build_hybrid_model.py
├── train_hybrid_model.py
├── plot_training_convergence.py
├── evaluate_hybrid_model.py
├── visualize_predictions.py
```

---

## Outputs
- Quantum neural network visualization.
- Trained hybrid model saved as `model.pt`.
- Training convergence plots (loss and accuracy).
- Predictions and visualizations on test data.
