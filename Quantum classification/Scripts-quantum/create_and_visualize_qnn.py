# Install Qiskit Aer
! pip install qiskit-aer

# Import necessary libraries
from qiskit import Aer
from qiskit.utils import QuantumInstance
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes
from qiskit_machine_learning.neural_networks import TwoLayerQNN
from qiskit.opflow import AerPauliExpectation
from qiskit.quantum_info import DensityMatrix, entanglement_of_formation
from qiskit.visualization import plot_state_city
import numpy as np
from IPython.display import display

# Create a QuantumInstance
qi = QuantumInstance(Aer.get_backend("aer_simulator_statevector"))

# Function to create a QNN
def create_qnn():
    feature_map = ZZFeatureMap(2)  # Feature map for quantum encoding
    ansatz = RealAmplitudes(2, reps=1)  # Ansatz for the QNN
    qnn = TwoLayerQNN(
        2,  # Number of qubits
        feature_map,
        ansatz,
        input_gradients=True,
        exp_val=AerPauliExpectation(),
        quantum_instance=qi,
    )
    return qnn

# Create the QNN
qnn = create_qnn()

# Display the QNN circuit parameters
print(qnn.circuit.parameters)

# Initialize random parameters for the circuit
params = np.random.uniform(-1, 1, len(qnn.circuit.parameters))
print(params)

# Create a density matrix from the QNN circuit
rho_01 = DensityMatrix.from_instruction(qnn.circuit.bind_parameters(params))

# Visualize the density matrix
plot_state_city(rho_01.data, title='Density Matrix', figsize=(12, 6))

# Calculate and display the purity of the quantum state
gamma_p = rho_01.purity()
display(rho_01.draw('latex', prefix='\\rho_p = '))
print("State purity: ", np.round(np.real(gamma_p), 3))

# Calculate and display the entanglement of formation
print(f'{entanglement_of_formation(rho_01):.4f}')
