
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_verify_apps_screen(driver):
    page = VehicleControlPage(driver)
    
    # Start Activity
    print("\n[Step] Starting Vehicle Control App...")
    page.start()
    time.sleep(3)
    
    # Test Screen: Apps (앱)
    print("\n[Step] Testing 'Apps' Screen...")
    page.click_sidebar_menu("앱")
    time.sleep(1)
    
    assert page.is_displayed(page.APPS_TITLE), "Apps Title not found"
    assert page.is_displayed(page.ANDROID_AUTO), "Android Auto option not found"
    assert page.is_displayed(page.CARPLAY), "CarPlay option not found"
    print(" - Apps Screen Verified.")
