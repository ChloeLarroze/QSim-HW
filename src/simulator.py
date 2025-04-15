#library imports
import numpy as np

#simple quantum simulator that can initialize qubits, apply gates, and simulate noise.
class Simulator:
    #constructor 
    def __init__(self, num_qubits):
        self.num_qubits = num_qubits
        self.state = np.zeros(2**num_qubits, dtype=complex)
        self.state[0] = 1  #initialize to |0...0⟩

    #initialize the state of the qubits 
    def initialize(self, state):
        if state == "|0⟩":
            self.state = np.zeros(2**self.num_qubits, dtype=complex)
            self.state[0] = 1
        elif state == "|+⟩":
            self.state = np.ones(2**self.num_qubits, dtype=complex) / np.sqrt(2**self.num_qubits)
        else:
            raise ValueError("Unsupported initial state")

    #apply a gate to the qubits
    def apply_gate(self, gate, target, control=None):
        if gate == "X":
            self._apply_single_qubit_gate(self._x_gate(), target)
        elif gate == "H":
            self._apply_single_qubit_gate(self._h_gate(), target)
        elif gate == "CNOT":
            if control is None: #todo
                raise ValueError("CNOT gate requires a control qubit")
            self._apply_two_qubit_gate(self._cnot_gate(), control, target)
        else:
            raise ValueError("Unsupported gate")

    def apply_noise(self, noise_model):
        # todo
        pass

    #gate functions ---
    def _apply_single_qubit_gate(self, gate_matrix, target):
        full_gate = 1
        for i in range(self.num_qubits):
            full_gate = np.kron(full_gate, gate_matrix if i == target else np.eye(2))
        self.state = np.dot(full_gate, self.state)

    def _apply_two_qubit_gate(self, gate_matrix, control, target):
        #todo 
        raise NotImplementedError("Two-qubit gate application is not yet implemented")

    def _x_gate(self):
        return np.array([[0, 1], [1, 0]])

    def _h_gate(self):
        return np.array([[1, 1], [1, -1]]) / np.sqrt(2)

    def _cnot_gate(self):
        # todo 
        raise NotImplementedError("CNOT gate matrix is not yet implemented")

#test 
if __name__ == "__main__":
    sim = Simulator(2)
    sim.initialize("|0⟩")
    print("Initial state:", sim.state)
    sim.apply_gate("H", 0)
    print("After H gate on qubit 0:", sim.state)
    sim.apply_gate("X", 1)
    print("After X gate on qubit 1:", sim.state)

''''
result : 
Initial state: [1.+0.j 0.+0.j 0.+0.j 0.+0.j]
After H gate on qubit 0: [0.70710678+0.j 0.        +0.j 0.70710678+0.j 0.        +0.j]
After X gate on qubit 1: [0.        +0.j 0.70710678+0.j 0.        +0.j 0.70710678+0.j] 
'''