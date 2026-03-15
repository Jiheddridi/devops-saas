import subprocess
from langchain.tools import tool

@tool
def run_command(command: str) -> str:
    """Exécute n'importe quelle commande DevOps : kubectl, terraform, ansible, az, docker, helm"""
    result = subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        timeout=300
    )
    output = result.stdout + result.stderr
    return output if output else "Commande exécutée sans output"
