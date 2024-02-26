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

# What knowledge I used for develop framework
* created different test files to test different functionality (login, register, search);
* wrote independent tests for every case;
* created a fixture and moved it to the conftest.py file;
* wrapped tests into classes;
* used a fixture to the classes.