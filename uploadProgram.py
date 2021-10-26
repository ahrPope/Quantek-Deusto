import os
from qiskit import IBMQ

IBMQ.load_account()
provider = IBMQ.get_provider(hub="ibm-q-lantik", group="udeusto", project="project1")  # Substitute with your provider.

provider.runtime.delete_program("ibmq-qsvm")


program_json = os.path.join(os.getcwd(), "IBMQ-QSVM.json")
program_data = os.path.join(os.getcwd(), "IBMQ-QSVM.py")

program_id = provider.runtime.upload_program(
    data=program_data,
    metadata=program_json
)

provider.runtime.set_program_visibility(program_id="ibmq-qsvm", public=True)

print(program_id)