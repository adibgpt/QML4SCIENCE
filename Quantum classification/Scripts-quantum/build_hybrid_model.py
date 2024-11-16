from torch.nn import Module, Conv2d, Linear, Dropout2d
import torch.nn.functional as F
from torch import cat
from qiskit_machine_learning.connectors import TorchConnector

# Define a hybrid neural network
class Net(Module):
    def __init__(self, qnn):
        super().__init__()
        self.conv1 = Conv2d(3, 128, kernel_size=5)  # First convolutional layer
        self.conv2 = Conv2d(128, 128, kernel_size=3)  # Second convolutional layer
        self.dropout = Dropout2d()  # Dropout layer
        self.fc1 = Linear(508032, 128)  # Fully connected layer
        self.fc2 = Linear(128, 2)  # Fully connected layer for binary input
        self.qnn = TorchConnector(qnn)  # Bind the QNN using TorchConnector
        self.fc3 = Linear(1, 1)  # Fully connected layer for quantum circuit output

    def forward(self, x):
        x = F.relu(self.conv1(x))  # Apply ReLU after the first convolution
        x = F.max_pool2d(x, 2)  # Max pooling
        x = F.relu(self.conv2(x))  # Apply ReLU after the second convolution
        x = F.max_pool2d(x, 2)  # Max pooling
        x = self.dropout(x)  # Apply dropout
        x = x.view(x.shape[0], -1)  # Flatten the tensor
        x = F.relu(self.fc1(x))  # Fully connected layer with ReLU
        x = self.fc2(x)  # Apply the second fully connected layer
        x = self.qnn(x)  # Apply the QNN
        x = self.fc3(x)  # Apply the final fully connected layer
        return cat((x, 1 - x), -1)  # Return the output in binary form

# Instantiate the model with the QNN
model = Net(qnn)
