# QSim-HW — Quantum Hardware-Inspired Circuit Simulator

QSim-HW is my first quantum computing project using Python, aimed at simulating and visualizing noisy quantum hardware behaviors, with a special focus on superconducting qubits (e.g., transmons). Using realistic noise models (decoherence, thermal effects, gate infidelity), this simulator lets you explore the impact of physical limitations on quantum gates and states — all from your laptop, without access to a lab.

The goal is to make quantum hardware simulation accessible, intuitive, and pedagogical — especially for students and enthusiasts interested in the quantum hardware layer.

---

## Project Overview

<!-- > (To be filled in: Write a paragraph about why you wanted to make this, e.g. “Bridging quantum physics and embedded systems through hands-on simulation”...) -->

---

## Screenshots & Demos

<!-- > (To be added: include visualizations such as Bloch sphere animations, state vector plots, decoherence graphs, etc.) -->

---

## Project structure 

```bash
QSim-HW/
├── README.md
├── docs/
│   └── qubit_modeling.md          # Theoretical models and equations
├── notebooks/
│   ├── 01_single_qubit_decay.ipynb
│   ├── 02_bell_state_under_noise.ipynb
│   └── ...
├── src/
│   ├── simulator.py               # Core simulation logic
│   ├── noise_models.py            # T1, T2, thermal noise, gate errors
│   ├── circuits.py                # Reusable gate circuits
│   └── visualizer.py              # Bloch sphere, fidelity plots, etc.
├── examples/
│   └── visualize_bloch.py         # Minimal visualization demos
├── tests/
│   └── test_noise.py              # Unit tests
├── requirements.txt
└── LICENSE

```

## Tech Stack

- Python 3.10+
- QuTiP (Quantum Toolbox in Python)
- NumPy / SciPy
- Matplotlib / Plotly
- JupyterLab / Jupyter Notebooks
- (Optional) Streamlit / PyQtGraph for GUI
- (Optional) Qiskit for interoperability

---

## Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/QSim-HW.git
cd QSim-HW
pip install -r requirements.txt
```

## Usage

Explore the Jupyter notebooks inside the notebooks/ directory. Examples include:
- Decoherence of a single qubit
- Bell state under noise
- Fidelity vs gate error
- Bloch sphere visualization over time


## Resources & References

- MIT OpenCourseWare - Quantum Physics II  
  Available at: [https://ocw.mit.edu](https://ocw.mit.edu)

- Michel Devoret – Yale University Lecture Notes  
  Available at: [https://courses.yale.edu](https://courses.yale.edu)

- IBM Quantum – Quantum Hardware Overview  
  Available at: [https://quantum-computing.ibm.com](https://quantum-computing.ibm.com)

- Nielsen, M.A., & Chuang, I.L. (2010). *Quantum Computation and Quantum Information*. Cambridge University Press.


## 🧑‍💻 Author
Made with ❤️ by Chlo
(Master’s student in Microelectronics & Embedded Systems — Mines Saint-Étienne)

