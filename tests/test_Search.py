from pages.HomePage import HomePage
from tests.BaseTest import BaseTest


class TestSearch(BaseTest):
    
    def test_search_for_a_valid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product('HP')

        assert search_page.display_status_of_valid_product(), "Element does not displayed"


    def test_search_for_invalid_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product('Honda')

        expected_no_product_message = "There is no product that matches the search criteria."
        result_no_product_message = search_page.retrive_no_product_message()        
        assert result_no_product_message == expected_no_product_message, "Invalid search err messages does not match"


    def test_search_without_entering_any_product(self):
        home_page = HomePage(self.driver)
        search_page = home_page.search_for_a_product('')

        # default working code
        # expected_search_err_message = "There is no product that matches the search criteria."

        # code for taking screenshot on failure
        expected_search_err_message = "There is no product that matches the search criteria.Unnecessary text"
        result_search_err_message = search_page.retrive_no_product_message()        
        assert result_search_err_message == expected_search_err_message, "Empty search err messages does not match"
