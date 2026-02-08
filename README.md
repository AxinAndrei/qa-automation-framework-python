🧪 QA Automation Framework (Python | Selenium | API)
📘 Overview

This project is a QA Automation framework built with Python, covering both UI automation and API automation.

It demonstrates real-world QA practices such as Page Object Model, REST API testing (CRUD), positive & negative testing, and HTML reporting.

🧰 Tech Stack
- Python 3
- Selenium WebDriver
- Pytest
- Requests (API testing)
- Pytest-HTML (reports)
- WebDriver Manager
- GitHub Actions (CI-ready structure)

🚀 Features
- UI automation using Selenium and Page Object Model (POM)
- API automation (GET, POST, PUT, DELETE)
- Positive & negative API testing
- Explicit waits and stable UI tests
- HTML reports generation
- Logs and screenshots on failures
- Clean and scalable project structure

📂 Project Structure
selenium-google-tests/
- api_tests
- pages
- tests
- utils
- reports
- logs
- conftest.py
- requirements.txt
- README.md

▶️ How to Run
- Install dependencies:
pip install -r requirements.txt

- Run all tests:
python -m pytest

- Run API tests only:
python -m pytest api_tests

- Generate HTML report
python -m pytest --html=reports/report.html --self-contained-html

🔌 API Testing Notes
- API tests cover CRUD operations
- Includes negative testing scenarios
- Uses mock APIs (dummyjson)
- Test expectations are aligned with mock API behavior

👤 Author
Andrei Axin
GitHub: https://github.com/andrei-axin
