import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        from selenium.webdriver.chrome.service import Service
        serv_obj = Service("E:\\python\\drivers\\chromedriver.exe")
        driver = webdriver.Chrome(service=serv_obj)
    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service
        serv_obj = Service("E:\\python\\drivers\\geckodriver.exe")
        driver = webdriver.Firefox(service=serv_obj)
    return driver

def pytest_addoption(parser):    # This will get the value from CLI
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):       # This will return the Browser value to setup method
    return request.config.getoption("--browser")

# customizing reHTML Report
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'Orange HRM'
    config._metadata['Module Name'] = 'Login Module'
    config._metadata['Tester Name'] = 'Parag'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)