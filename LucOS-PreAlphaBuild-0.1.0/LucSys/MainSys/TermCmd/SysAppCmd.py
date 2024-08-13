import subprocess

#Not a terminal command (its used in other commands)
def run_python_script(script_path):
    try:
        # Running the script using subprocess
        subprocess.run(['python', script_path])
    except Exception as e:
        pass
   
#Opens the calcualtor
def calculator(*_):
    run_python_script('D:\LucOS\LucSys\SysApps\Calculator.py')
