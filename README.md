# Selenium Test Automation Framework

A web automation testing framework built with Selenium, Pytest, and Python using Page Object Model (POM).

## 📌 Features
- Page Object Model structure
- Data-driven testing (JSON)
- Positive & negative test scenarios
- Screenshot capture on failure
- HTML test reporting

## 🛠️ Tech Stack
- Python
- Selenium
- Pytest

## 📂 Project Structure
selenium-test-automation/
│
├── tests/
│ └── test_login.py
│
├── pages/
│ └── login_page.py
│
├── data/
│ └── login_data.json
│
├── conftest.py
└── README.md


## ▶️ How to Run
git clone https://github.com/GreatEhi/selunium-test-automation
cd selenium-test-automation

python3 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
pytest -v --html=report.html


## ✅ Test Coverage
- Login (valid credentials)
- Login (invalid username)
- Login (invalid password)
