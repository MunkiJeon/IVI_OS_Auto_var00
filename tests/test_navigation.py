import pytest
import time
from pages.vehicle_control_page import VehicleControlPage
from pages.app_grid_page import AppGridPage
from pages.main_screen_page import MainScreenPage

class TestNavigation:
    
    def test_vehicle_control_activity(self, driver):
        """
        Verify that Vehicle Control Activity can be launched.
        """
        vehicle_page = VehicleControlPage(driver)
        vehicle_page.start()
        
        # Adding a small sleep to allow app to launch since we don't have robust element wait locators yet
        time.sleep(3) 
        
        assert vehicle_page.is_loaded(), "Vehicle Control Activity failed to load"

    def test_app_grid_activity(self, driver):
        """
        Verify that App Grid Activity can be launched.
        """
        app_grid_page = AppGridPage(driver)
        app_grid_page.start()
        time.sleep(3)
        assert app_grid_page.is_loaded(), "App Grid Activity failed to load"

    def test_main_screen_activity(self, driver):
        """
        Verify that Main Screen Activity can be launched.
        """
        main_screen_page = MainScreenPage(driver)
        main_screen_page.start()
        time.sleep(3)
        assert main_screen_page.is_loaded(), "Main Screen Activity failed to load"
