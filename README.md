# 🚀 Python Selenium Pytest Automation Framework

A scalable and maintainable UI Automation Framework built using Python, Selenium, Pytest, and Allure Reporting.  
The framework supports parallel execution, logging, screenshot capture, marker-based execution, and Allure Trend reporting.

---

## 📌 Features

- Selenium WebDriver integration
- Pytest Framework
- Page Object Model (POM)
- Parallel Execution (pytest-xdist)
- Allure Reporting
- Allure Trend Support
- Timestamp-Based Execution Folders
- Screenshot Capture & Attachment
- Date-wise Logging
- Marker-Based Test Execution
- CI/CD Ready Structure

---

## 🛠 Tech Stack

- Python 3.x  
- Selenium  
- Pytest  
- Pytest-xdist  
- Allure Report  
- Logging Module  

---

## 📂 Project Structure

project_root/
│
├── testCases/              # Test files  
├── pageObjects/            # Page object classes  
├── Utilities/              # Logger, Screenshot, Config reader  
├── Screenshots/            # Saved screenshots  
├── Logs/                   # Date-wise log files  
├── allure-results/         # Raw Allure results (timestamp based)  
├── allure-report/          # Generated Allure report  
├── run_test.py             # Main execution file  
├── pytest.ini              # Pytest configuration  
├── requirements.txt        # Dependencies  
└── README.md  

---

## ⚙️ Setup Instructions

### 1️⃣ Clone Repository

git clone <repository-url>  
cd <project-folder>

### 2️⃣ Create Virtual Environment (Recommended)

python -m venv venv  
venv\Scripts\activate

### 3️⃣ Install Dependencies

pip install -r requirements.txt

### 4️⃣ Install Allure

Download Allure from:  
https://docs.qameta.io/allure/

Add Allure `bin` directory to system PATH  
OR update Allure path inside `run_test.py`.

---

## ▶️ Running Tests

Run complete test suite:

python run_test.py

Execution flow:

1. Tests run in parallel
2. Timestamp-based result folder is created
3. Previous Allure history is preserved
4. New Allure report is generated
5. Report opens automatically

---

## ⚡ Parallel Execution

Parallel workers are controlled inside `run_test.py`:

workers = 3

Modify as per system capability.

---

## 🏷 Test Markers

Markers defined in `pytest.ini`:

[pytest]
markers =
    positive: marks positive test cases
    negative: marks negative test cases
    regression: marks regression tests

Run only negative tests:

pytest -m negative

Run only positive tests:

pytest -m positive

Exclude negative tests:

pytest -m "not negative"

---

## 📊 Allure Report

Allure report provides:

- Test summary
- Pass/Fail statistics
- Execution details
- Screenshots
- Logs
- Trend graph (after second execution)

Trend is enabled by preserving report history between runs.

---

## 📸 Screenshot Handling

- Screenshots are saved in the `Screenshots/` folder.
- Automatically attached to Allure report.
- Supports failure and manual capture.

---

## 📝 Logging

- Logs are generated date-wise.
- Stored inside `Logs/`.
- Includes timestamp, level, class name, method name, and message.

---

## 🧠 Framework Design

- Page Object Model (POM)
- Reusable utilities
- Clean separation of concerns
- Scalable folder structure
- CI/CD ready

---

## 🚀 Future Enhancements

- CI/CD Integration (Jenkins / GitHub Actions)
- Cross-browser support
- Selenium Grid integration
- Cloud execution
- Email reporting
- Docker support

---

## 👨‍💻 Author

Developed as a complete end-to-end Selenium-Pytest Automation Framework for scalable UI testing.