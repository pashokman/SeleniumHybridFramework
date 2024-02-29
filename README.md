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


# Help to run tests:
* To run all test need to use command:
    + '''python -m pytest'''

* To run some type of tests need to use command (mark names you can select in pytest.ini file, example - "python -m pytest -m api", to use few markers "api or api2"): 
    + '''python -m pytest -m mark_name'''

* To run test in paralel need to use command (need to be installed "pytest-xdist" module):
    + '''python -m pytest -n 4'''

* To see test names on console and its status need to use command:
    + '''python -m pytest -m personal_ui_2 -s -v'''

* To clean project folder from "__pychache__" (need to be installed "pyclean" module): 
    + '''pyclean .'''

* To run only specific test file:
    + '''python -m pytest test/test_Search.py -s -v'''

* To run tests and create report files - first command, to generate the report in root folder open cmd - second command:
    + '''python -m pytest -v -s --alluredir="./Reports"'''
    + '''allure serve "./Reports"'''

* To add virtual environment:
    + '''python -m venv venv'''