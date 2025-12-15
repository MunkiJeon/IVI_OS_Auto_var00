
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_verify_security_screen(driver):
    page = VehicleControlPage(driver)
    
    # Start Activity
    print("\n[Step] Starting Vehicle Control App...")
    page.start()
    time.sleep(3)
    
    # Test Screen: Security (보안)
    print("\n[Step] Testing 'Security' Screen...")
    page.click_sidebar_menu("보안")
    time.sleep(1)
    
    assert page.is_displayed(page.SECURITY_TITLE), "Security Title not found"
    assert page.is_displayed(page.RECORDING_OPTIONS), "Recording Options header not found"
    assert page.is_displayed(page.DRIVING_RECORDING), "Driving Recording option not found"
    print(" - Security Screen Verified.")
