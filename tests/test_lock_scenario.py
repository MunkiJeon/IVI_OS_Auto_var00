import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestLockScenario:
    def test_lock_scenario(driver):
        vehicle_page = VehicleControlPage(driver)
        
        print("Starting Lock Scenario Test...")
        vehicle_page.start()
        time.sleep(3)  # Wait for app transform
        
        if not vehicle_page.is_loaded():
            print("Error: App not loaded.")
            return

        # Navigate to Lock Screen
        print("Navigating to Lock Screen...")
        vehicle_page.click(vehicle_page.MENU_LOCK)
        time.sleep(1)
        
        # Verify Top Elements
        print("Verifying Top Elements...")
        if vehicle_page.is_displayed(vehicle_page.LOCK_CHILD_LOCK):
            print("Verified: Child Lock is visible.")
        else:
            print("Error: Child Lock not visible.")

        if vehicle_page.is_displayed(vehicle_page.LOCK_UNLOCK_DOOR):
            print("Verified: Door Unlock is visible.")
        else:
            print("Error: Door Unlock not visible.")
            
        # Scroll down to see bottom elements
        print("Scrolling down...")
        vehicle_page.scroll_content_down()
        time.sleep(2)
        
        # Verify Bottom Elements
        print("Verifying Bottom Elements...")
        try:
            if vehicle_page.is_displayed(vehicle_page.LOCK_AUTO_OPEN_TRUNK):
                print("Verified: Auto Open Trunk is visible.")
            else:
                print("Error: Auto Open Trunk not visible.")
                
            if vehicle_page.is_displayed(vehicle_page.LOCK_TRUNK):
                print("Verified: Trunk text is visible.")
            else:
                print("Error: Trunk text not visible.")
        except Exception as e:
            print(f"Error checking bottom elements: {e}")
            
        # Extra Scroll as per User Request (to be safe)
        print("Performing extra scroll...")
        vehicle_page.scroll_content_down()
        time.sleep(1)

        print("Lock Scenario Test Completed")
