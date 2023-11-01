import subprocess
from automated import clear_log_folder

def execute_python_script(script_path):
    try:
        result = subprocess.run(['python', script_path], capture_output=True, text=True)
        return result.returncode, result.stdout
    except subprocess.CalledProcessError as e:
        return e.returncode, e.stderr

def execute(scripts):
    clear_log_folder()
    results = []

    for script in scripts:
        return_code, output = execute_python_script(script)
        results.append((script, return_code, output))

    print("Script Results:")
    for script, return_code, output in results:
        if return_code == 0:
            print(f'Script {script} executed successfully.')
        else:
            print(f'Script {script} failed with the following error:\n{output}')

    if all(return_code == 0 for script, return_code, output in results):
        print('\nAll scripts were executed successfully.')
    else:
        print('\nAt least one script failed, listed below:')

    for script, return_code, output in results:
        if return_code == 1:
            print(f'{script}')