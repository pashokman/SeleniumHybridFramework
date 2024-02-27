import pytest
from pages.HomePage import HomePage
from pages.SearchPage import SearchPage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_field('HP')
        home_page.click_on_search_btn()

        search_page = SearchPage(self.driver)
        assert search_page.display_status_of_valid_product(), "Element does not displayed"


    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        home_page.enter_product_into_search_field('Honda')
        home_page.click_on_search_btn()
        
        expected_no_product_message = "There is no product that matches the search criteria."
        search_page = SearchPage(self.driver)
        result_no_product_message = search_page.retrive_no_product_message()
        assert result_no_product_message == expected_no_product_message, "Invalid search err messages does not match"


    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        home_page.click_on_search_btn()
        
        expected_search_err_message = "There is no product that matches the search criteria."
        search_page = SearchPage(self.driver)
        result_search_err_message = search_page.retrive_no_product_message()
        assert result_search_err_message == expected_search_err_message, "Empty search err messages does not match"
