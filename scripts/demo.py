# scripts/demo.py
# Runs the three workflow scripts and prints results.

import subprocess
import sys
import os

def run_script(script_path):
    print(f'Running {script_path}...')
    result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
    if result.returncode != 0:
        print(f'Error running {script_path}:')
        print(result.stderr)
    else:
        print(result.stdout)

if __name__ == '__main__':
    base = os.path.dirname(os.path.abspath(__file__))
    workflows = [
        os.path.join(base, '../workflows/marketing_reels.py'),
        os.path.join(base, '../workflows/hr_decision_tree.py'),
        os.path.join(base, '../workflows/ops_svm_knn.py')
    ]
    for wf in workflows:
        run_script(wf)