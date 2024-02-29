from datetime import datetime
import pytest


@pytest.mark.usefixtures("setup_and_teardown", "log_on_failure")
class BaseTest:
    
    def generate_email_with_timestamp(self):
        time_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        address = "test_auto" + time_stamp + "@gmail.com"
        return address