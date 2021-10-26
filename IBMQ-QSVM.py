from qiskit.circuit.library import ZZFeatureMap
from qiskit_machine_learning.algorithms import QSVC
from qiskit_machine_learning.kernels import QuantumKernel

from qiskit.providers.ibmq.runtime import UserMessenger, ProgramBackend

def main(backend: ProgramBackend, user_messenger: UserMessenger, **kwargs):

    train_features = kwargs.pop("train_features")
    train_labels = kwargs.pop("train_labels")
    test_features = kwargs.pop("test_features")
    test_labels = kwargs.pop("test_labels")

    feature_map = ZZFeatureMap(feature_dimension=2, reps=2, entanglement="linear")
    kernel = QuantumKernel(feature_map=feature_map, quantum_instance=backend)

    qsvc = QSVC(quantum_kernel=kernel)
    qsvc.fit(train_features, train_labels)
    qsvc_score = qsvc.score(test_features, test_labels)


    return qsvc_score