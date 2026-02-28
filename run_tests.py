import os
import sys
import subprocess
import shutil
from datetime import datetime

# Main folder for results
main_folder = "allure-results"
os.makedirs(main_folder, exist_ok=True)

# Current date & time
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# Create new timestamp folder
new_folder = os.path.join(main_folder, timestamp)
os.makedirs(new_folder, exist_ok=True)

print(f"\nRunning tests for: {new_folder}\n")

workers = 3

# Run pytest
subprocess.run(
    [
        sys.executable,
        "-m",
        "pytest",
        "testCases",
        "-v",
        # "-m", "negative", or "-m", "positive", or "-m", "sanity",
        f"-n={workers}",
        f"--alluredir={new_folder}"
    ]
)

# -----------------------------
# COPY HISTORY FOR TREND
# -----------------------------

report_folder = "allure-report"

history_source = os.path.join(report_folder, "history")
history_dest = os.path.join(new_folder, "history")

if os.path.exists(history_source):
    print("Copying previous history for Trend...")
    shutil.copytree(history_source, history_dest, dirs_exist_ok=True)

# -----------------------------
# GENERATE NEW REPORT
# -----------------------------

subprocess.run(
    [
        r"C:\allure-2.27.0\allure-2.27.0\bin\allure.bat",
        "generate",
        new_folder,
        "-o",
        report_folder,
        "--clean"
    ]
)

# Open report
subprocess.run(
    [
        r"C:\allure-2.27.0\allure-2.27.0\bin\allure.bat",
        "open",
        report_folder
    ]
)
# use below score when you push to gitrepo
#
# import os
# import sys
# import subprocess
#
# # Fixed Allure results folder (Jenkins requirement)
# ALLURE_RESULTS_DIR = "allure-results"
#
# # Create folder if not exists
# os.makedirs(ALLURE_RESULTS_DIR, exist_ok=True)
#
# print("\n===== Running Pytest on Jenkins =====\n")
#
# # Number of parallel workers
# workers = 3  # Change if needed
#
# # Run pytest
# result = subprocess.run(
#     [
#         sys.executable,
#         "-m",
#         "pytest",
#         "testCases",          # Run all test cases folder
#         "-v",
#         f"-n={workers}",      # Parallel execution
#         f"--alluredir={ALLURE_RESULTS_DIR}",
#         "--clean-alluredir"   # Clean old results (important for CI)
#     ]
# )
#
# # Exit with pytest result code (important for Jenkins build status)
# sys.exit(result.returncode)