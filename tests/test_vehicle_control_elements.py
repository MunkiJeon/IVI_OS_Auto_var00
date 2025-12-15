import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestVehicleControlElements:
    
    def test_quick_settings_elements_presence(self, driver):
        """
        Verify that Quick Settings elements are present on the screen.
        Assumption: The app starts on Quick Settings or we can navigate to it.
        """
        page = VehicleControlPage(driver)
        page.start()
        
        # Wait for app to load
        time.sleep(5)
        
        print("Checking for Title/Menu presence...")
        assert page.is_displayed(page.TITLE), "Title/Menu '빠른 설정' not found"
        
        # Check Left Menu Items (Just a few samples)
        print("Checking Left Menu Items...")
        assert page.is_displayed(page.MENU_LIGHTS), "Menu '라이트' not found"
        assert page.is_displayed(page.MENU_AD), "Menu 'AD' not found"
        
        # Check Quick Settings Right Panel Elements
        # Note: If the app didn't start on Quick Settings tab, these might fail.
        # We might need to click page.TITLE (which is '빠른 설정' menu) to ensure we are there.
        print("Ensuring we are on Quick Settings tab...")
        page.click(page.TITLE) 
        time.sleep(2)
        
        print("Checking Quick Settings Panel elements...")
        elements_to_check = [
            (page.QS_ALL_WINDOWS, "모든 창문"),
            (page.QS_WINDOW_LOCK, "창문 잠금"),
            (page.QS_DOOR_LOCK, "도어 잠금"),
            (page.QS_TRUNK, "트렁크"),
            (page.QS_CHILD_LOCK, "차일드락")
        ]
        
        results = []
        for locator, name in elements_to_check:
            is_present = page.is_displayed(locator)
            print(f"Checking '{name}': {'Found' if is_present else 'Not Found'}")
            results.append((name, is_present))
            
        # Fail the test if any element is missing, but log all first
        failed_elements = [name for name, present in results if not present]
        assert not failed_elements, f"Missing elements: {failed_elements}"
