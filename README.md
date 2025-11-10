🧪 Selenium Google Search Automation Project
📘 Overview

This project is a web automation testing framework built with Python, Selenium WebDriver, and Pytest.
It automates the Google Search flow, verifying that a search operation returns valid results and that the browser title reflects the search term.

The project follows the Page Object Model (POM) design pattern and demonstrates clean, maintainable test architecture suitable for real-world QA automation.

🚀 Features

✅ Automates Google Search (navigates, accepts cookies, enters text, validates title)
✅ Uses Page Object Model for scalable and readable code
✅ Implements explicit waits (no sleep) for reliable test execution
✅ Generates HTML reports automatically via pytest-html
✅ Fully compatible with GitHub Actions CI/CD pipelines
✅ Demonstrates QA automation best practices (fixtures, asserts, structure)

⚙️ Setup Instructions
1️⃣ Clone the repository
git clone https://github.com/andrei-axin/selenium-google-tests.git
cd selenium-google-tests
2️⃣ Install dependencies
pip install -r requirements.txt
3️⃣ Run the tests
python -m pytest --html=reports/report.html --self-contained-html

After the test completes, open reports/report.html in your browser to view the HTML test report.

🧩 Test Scenario
Step	Description
1.	    Open Chrome browser and navigate to google.com
2.	    Accept cookies (if popup is displayed)
3.	    Wait until the search box becomes visible
4.	    Enter text "Selenium Python" and press ENTER
5.	    Validate that the resulting page title contains the word "Selenium"
6.	    Close the browser