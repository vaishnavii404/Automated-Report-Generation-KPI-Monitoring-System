import subprocess
from pathlib import Path
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
SCRIPTS_DIR = BASE_DIR / "scripts"

def run(script_name):
    result = subprocess.run(
        [sys.executable, SCRIPTS_DIR / script_name],
        capture_output=True,
        text=True,
        encoding="utf-8"  # <-- add this
    )
    print(result.stdout)
    if result.stderr:
        print(result.stderr)
if __name__ == "__main__":
    run("data_cleaning.py")
    run("report_generator.py")
    run("alerts.py")
