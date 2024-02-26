import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_a_valid_product(self):
        self.driver.find_element(By.XPATH, "//input[@name='search']").send_keys('HP')
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed(), "Element does not displayed"


    def test_search_for_invalid_product(self):
        self.driver.find_element(By.XPATH, "//input[@name='search']").send_keys('Honda')
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        
        expected_search_err_message = "There is no product that matches the search criteria."
        result_search_err_message = self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        assert result_search_err_message == expected_search_err_message, "Invalid search err messages does not match"


    def test_search_without_entering_any_product(self):
        self.driver.find_element(By.XPATH, "//button[contains(@class,'btn-default')]").click()
        
        expected_search_err_message = "There is no product that matches the search criteria."
        result_search_err_message = self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text
        assert result_search_err_message == expected_search_err_message, "Empty search err messages does not match" 