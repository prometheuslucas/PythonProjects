import subprocess
import sys

def run_test(module_name):
    print(f"\nRunning {module_name}...")
    result = subprocess.run([sys.executable, '-m', module_name], capture_output=True, text=True)
    print(result.stdout)
    if result.returncode != 0:
        print(result.stderr)
        print(f"{module_name} failed.")
    else:
        print(f"{module_name} passed.")

test_modules = [
    'tests.test_domain_primitives',
    'tests.test_application_exceptions',
]

if __name__ == "__main__":
    for module in test_modules:
        run_test(module)
    print("\nAll tests completed.")
