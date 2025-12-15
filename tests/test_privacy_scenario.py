
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_verify_privacy_screen(driver):
    page = VehicleControlPage(driver)
    
    # Start Activity
    print("\n[Step] Starting Vehicle Control App...")
    page.start()
    time.sleep(3)
    
    # Reset Sidebar
    page.reset_sidebar()

    # Test Screen: Privacy (개인정보 보호)
    print("\n[Step] Testing 'Privacy' Screen...")
    page.click_sidebar_menu("개인정보 보호")
    time.sleep(1)
    
    assert page.is_displayed(page.PRIVACY_TITLE), "Privacy Title not found"
    assert page.is_displayed(page.MIC_USAGE), "Mic Usage option not found"
    assert page.is_displayed(page.LOCATION_USAGE), "Location Usage option not found"
    print(" - Privacy Screen Verified.")
