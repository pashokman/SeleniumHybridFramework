import pytest
from selenium import webdriver
from utilities.ReadConfigurations import read_configuration


@pytest.fixture()
def setup_and_teardown(request):
    browser = read_configuration("basic info", "browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        print('Provide a valid browser name from this list - chrome/firefox/edge')
    driver.maximize_window()
    app_url = read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()