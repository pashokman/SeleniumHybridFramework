# SeleniumHybridFramework

# Tasks/tests
## test_Login.py
* login_with_valid_credentials;
* login_with_invalid_email_and_valid_password;
* login_with_valid_email_and_invalid_password;
* login_without_entering_credentials.

## test_Register.py
* register_with_mandatory_fields;
* register_with_all_fields;
* register_with_duplicate_email;
* register_without_entering_any_fields.

## test_Search.py
* search_for_a_valid_product;
* search_for_invalid_product;
* search_without_entering_any_product.

# Steps for develop the framework
* created different test files to test different functionality (login, register, search);
* wrote independent tests for every test-case;
* created a fixture and moved it to the conftest.py file;
* wrapped tests into classes;
* used a fixture to classes;
* added utility for reading (browser, url) from configuration file - create new package - configurations;
* change all tests into POM (page object model) - create new  package - pages;
* added return statements to the next page object into last page methods which called in tests with previous page object;
* refactored the code in page classes and tests - develop methods which consists from another methods to make test more readable and shorter;
* created BasePage class and described main methods of working with an web element, refactored other classes to be inherited from BasePage class, used parent methods;
* added BaseTest class before which should paste pytest mark with fixture for all test classes and inherited this class by other test classes;
* moved duplicate methods from test classes to BaseTest class;
* implemented DDT in test_Login file (created new utility - ExcelUtils, added a folder for text files - ExcelFiles);
* implemented DDT in test_Register file;
* added code for taking screenshot on failure in conftest.py - log_on_failure, pytest_runtest_makereport, call the fixture in BaseTest class for working with all tests, broke one search test for getting a screenshot on failure;
* added virtual environment;


# Selenium Grid 4
Selenium Grid is used to distribute and run tests on multiple machines.
If we configure Selenium Grid and Pytest parallel we can parallel run all tests on different machines without heavy impact on computer performanse (if we run all scripts in parallel in 1 machine it will decrease the performance of this machine).
## Standalone mode
1. Download Selenium Grid - https://www.selenium.dev/downloads/
2. Download browser driver from the same URL (if after run next command, some of browsers didn't detect) and paste them to the same folder where we downloaded Selenium Grid.
3. Open ```cmd``` from the same folder where we downloaded Selenium Grid.
4. Run command: ```java -jar selenium-server-4.18.1.jar standalone```.
5. To check if grid successfully run (non UI mode), go to: ```http://localhost:4444/status```.
6. To check if grid successfully run (UI mode), go to: ```http://localhost:4444```.
7. Change ```conftest.py``` file:\
Before
```
@pytest.fixture()
def setup_and_teardown(request):
    browser = read_configuration("basic info", "browser")
    global driver
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
```
After
```
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOprions
from selenium.webdriver.edge.options import Options as EdgeOprtions

@pytest.fixture()
def setup_and_teardown(request):
    browser = read_configuration("basic info", "browser")
    global driver
    if browser == "chrome":
        options = ChromeOprions()
    elif browser == "firefox":
        options = FirefoxOptions()
    elif browser == "edge":
        options = EdgeOprtions()
    else:
        print('Provide a valid browser name from this list - chrome/firefox/edge')
    driver = webdriver.Remote('http://192.168.31.197:4444/wd/hub', options=options)
    driver.maximize_window()
    app_url = read_configuration("basic info", "url")
    driver.get(app_url)
    request.cls.driver = driver
    yield
    driver.quit()
```
8. Now if we run tests, they will be in the Grid: ```python -m pytest tests/test_Search.py```.

## Hub and Node mode
1. Download Selenium Grid - https://www.selenium.dev/downloads/
2. Download browser driver from the same URL (if after run next command, some of browsers didn't detect) and paste them to the same folder where we downloaded Selenium Grid.
3. Open ```cmd``` from the same folder where we downloaded Selenium Grid.
4. Run command to start hub on the first machine: ```java -jar selenium-server-4.18.1.jar hub```.
5. Run command to start node on the same first machine: ```java -jar selenium-server-4.18.1.jar node```.
6. If we want to start node on the second machine and hub already running on the first machine, we should run the command on the second machine (where <hub-ip> we can get from ```cmd``` console): 
```
java -jar selenium-server-4.18.1.jar node --detect-drivers true --publish-events tcp://<hub-ip>:4442 --subscribe-events tcp://<hub-ip>:4443
```
7. Also we should change ```conftest.py``` file as in Standalone mode and then we can run tests.

## Distributed mode (use if we have a large size of Grid to setup)
1. Download Selenium Grid - https://www.selenium.dev/downloads/
2. Download browser driver from the same URL (if after run next command, some of browsers didn't detect) and paste them to the same folder where we downloaded Selenium Grid.
3. Open ```cmd``` from the same folder where we downloaded Selenium Grid.
We shoul configure comunication between different components of Grid
All these command shoul run in new ```cmd``` console from folder where Selenium Grid was downloaded:
4. First we should run ```even-bus``` component: ```java -jar selenium-server-4.18.1.jar event-bus```. \
It has socket - ```<ip>:5556```.
5. Second we should run ```session-map``` component: ```java -jar selenium-server-4.18.1.jar sessions```. \
It has socket - ```<ip>:5557```.
6. Third we should run ```session-queue``` component: ```java -jar selenium-server-4.18.1.jar sessionqueue```. \
It has socket - ```<ip>:5559```.
7. Fourth we should run ```distributor``` component:
```
java -jar selenium-server-4.18.1.jar distributor --sessions http://<ip_from_session_map>:5556 --sessionqueue http://<ip_from_session_queue>:5559 --bind-bus false
``` 
It has socket - ```<ip>:5553```.\
8. Fifth we should run ```router``` component:
```
java -jar selenium-server-4.18.1.jar router --sessions http://<ip_from_session_map>:5556 --distributor http://<ip_from_distributor>:5553 --sessionqueue http://<ip_from_session_queue>:5559
``` 
It has socket - ```<ip>:4444```.\
9. Run command to start node (if we run on the same machine): ```java -jar selenium-server-4.18.1.jar node```\
Run command to start node (if we run on another machine): 
```
java -jar selenium-server-4.18.1.jar node --detect-drivers true --publish-events tcp://<hub-ip>:4442 --subscribe-events tcp://<hub-ip>:4443
```


# Help to run tests:
* To run all test need to use command: ```python -m pytest```
* To run some type of tests need to use command (mark names you can select in pytest.ini file, example - "python -m pytest -m api", to use few markers "api or api2"): ```python -m pytest -m mark_name```
* To run test in paralel need to use command (need to be installed "pytest-xdist" module): ```python -m pytest -n 4```
* To see test names on console and its status need to use command: ```python -m pytest -m personal_ui_2 -s -v```
* To clean project folder from "__pychache__" (need to be installed "pyclean" module): ```pyclean .```
* To run only specific test file: ```python -m pytest test/test_Search.py -s -v```
* To run tests and create report files - first command, to generate the report in root folder open cmd - second command:
```
python -m pytest -v -s --alluredir="./Reports"
allure serve "./Reports"
```
* To add virtual environment: ```python -m venv venv```