import pytest
import sys
import os

# Ensure the root directory is in the python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture to handle driver setup and teardown.
    """
    driver_instance = DriverFactory.get_driver()
    yield driver_instance
    # Teardown
    if driver_instance:
        driver_instance.quit()
