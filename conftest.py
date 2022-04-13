import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
import json

valid_mail = 'your, mail'
valid_password = "your, password"

@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_argument('chrome')  # Use 'headless' if you do not need a browser UI and 'chrome' if U need UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1920,1080')
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    options = get_chrome_options
    driver = webdriver.Chrome(executable_path='/Users/bazucer/Desktop/IT/skinTesting/drivers/chromedriver.exe', options=options)
    return driver


@pytest.fixture(scope='function') # If you need to to execute all tests for 1 session, change on 'session'
def setup(request, get_webdriver):
    driver = get_webdriver
    url = 'https://skinport.com/'
    if request.cls is not None:
        request.cls.driver = driver
    driver.get(url)

    yield driver

    # path = '/Users/bazucer/Desktop/IT/skinTesting/CookieChrome/cookie2.json'
    # with open(path, 'w') as filehandler:
    #     json.dump(driver.get_cookies(), filehandler)

    driver.quit()