import os
import shutil
from datetime import datetime, timedelta

# Paths
allure_results_path = 'allure-results'
allure_report_path = 'allure-report'
history_save_path = 'allure-history'
bash_script_path = 'all_feature.sh'  # Path to your Bash script


# Function to save history data
def save_history():
    try:
        history_path = os.path.join(allure_report_path, 'history')
        if os.path.exists(history_path):
            if os.path.exists(history_save_path):
                shutil.rmtree(history_save_path)
            shutil.copytree(history_path, history_save_path)
            print("History saved to", history_save_path)
        else:
            print("No history data found to save.")
    except Exception as e:
        print(f"An error occurred while saving history: {e}")


# Function to restore history data
def restore_history():
    try:
        history_path = os.path.join(allure_results_path, 'history')
        if os.path.exists(history_save_path):
            if os.path.exists(history_path):
                shutil.rmtree(history_path)
            shutil.copytree(history_save_path, history_path)
            print("History restored from", history_save_path)
        else:
            print("No saved history data found to restore.")
    except Exception as e:
        print(f"An error occurred while restoring history: {e}")


# Function to delete old .json and .png files
def delete_old_files(path, days=1):
    now = datetime.now()
    cutoff = now - timedelta(days=days)

    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for file_name in files:
                if file_name.endswith('.json') or file_name.endswith('.png'):
                    file_path = os.path.join(root, file_name)
                    file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
                    if file_time < cutoff:
                        try:
                            os.remove(file_path)
                            print(f"Deleted {file_path}")
                        except Exception as e:
                            print(f"An error occurred while deleting file {file_path}: {e}")


# Restore history before running tests
restore_history()

# Run your tests using the Bash script
print(f"Running tests using Bash script: {bash_script_path}")
test_result = os.system(f'bash {bash_script_path}')
if test_result != 0:
    print("An error occurred while running the tests.")
else:
    # Generate the Allure report
    generate_result = os.system(f'allure generate {allure_results_path} -o {allure_report_path} --clean')
    if generate_result != 0:
        print("An error occurred while generating the Allure report.")
    else:
        # Save history after generating the report
        save_history()

        # Delete old files from allure-results and allure-report
        delete_old_files(allure_results_path, days=1)
        delete_old_files(allure_report_path, days=1)