import subprocess
import os

def run_python_script(script_path):
    try:
        print(f"Running script: {script_path}")
        subprocess.run(['python', script_path], check=True)
        print("Script finished successfully")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Relative path to Main.py from the location of Boot.py
relative_path = os.path.join('..', 'MainSys', 'Main.py')
run_python_script(relative_path)

