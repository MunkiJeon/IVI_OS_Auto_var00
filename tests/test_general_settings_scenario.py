
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_verify_general_settings_screen(driver):
    page = VehicleControlPage(driver)
    
    # Start Activity
    print("\n[Step] Starting Vehicle Control App...")
    page.start()
    time.sleep(3)
    
    # Test Screen: General (일반 설정)
    print("\n[Step] Testing 'General' Screen...")
    page.click_sidebar_menu("일반 설정")
    time.sleep(1)

    assert page.is_displayed(page.GENERAL_SETTINGS_TITLE), "General Settings Title not found"
    assert page.is_displayed(page.FONT_SETTING), "Font Setting not found"
    assert page.is_displayed(page.LANGUAGE_SETTING), "Language Setting not found"
    print(" - General Screen Verified.")
