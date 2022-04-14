Introduction:
This repository contains usage PageObject pattern with Selenium and Python (PyTest + Selenium).
Practical execution of autotests for UI web application www.skinport.com - online Market for selling and 
purchase game items. Market has a lot of items, search and sort functions.

Files:
conftest.py contains all the required code to catch failed test cases and
make screenshot of the page in case any test case will fail.

pages/base.py contains PageObject pattern implementation for Python.

pages/elements.py contains helper class to define web elements on web pages.

tests contains several smoke Web UI tests for skinport.com

How To Run Tests:

1)Install all requirements:

pip3 install -r requirements

2)Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3)Run tests:

python3 -m pytest -v --driver Chrome --driver-path ${PATH_TO_DRIVER} {name of the tests}




