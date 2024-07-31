import subprocess

def run_module(module):
    return subprocess.Popen(['python3', '-m', f'lolstaticdata.{module}'])

def main():
    modules = ['champions', 'items', 'championrates']
    processes = [run_module(module) for module in modules]

    # Wait for all processes to complete
    for process in processes:
        process.wait()

if __name__ == "__main__":
    main()
