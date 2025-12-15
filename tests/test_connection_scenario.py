
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_verify_connection_screen(driver):
    page = VehicleControlPage(driver)
    
    # Start Activity
    print("\n[Step] Starting Vehicle Control App...")
    page.start()
    time.sleep(3)
    
    # Test Screen: Connection (연결)
    print("\n[Step] Testing 'Connection' Screen...")
    page.click_sidebar_menu("연결")
    time.sleep(1)
    
    assert page.is_displayed(page.CONNECTION_TITLE), "Connection Title not found"
    assert page.is_displayed(page.BLUETOOTH), "Bluetooth option not found"
    assert page.is_displayed(page.WIFI), "Wi-Fi option not found"
    print(" - Connection Screen Verified.")
