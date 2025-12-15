
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_verify_vehicle_info_screen(driver):
    page = VehicleControlPage(driver)
    
    # Start Activity
    print("\n[Step] Starting Vehicle Control App...")
    page.start()
    time.sleep(3)
    
    # Test Screen: Vehicle Info (차량 정보)
    print("\n[Step] Testing 'Vehicle Info' Screen...")
    page.click_sidebar_menu("차량 정보")
    time.sleep(1)

    assert page.is_displayed(page.VEHICLE_INFO_TITLE), "Vehicle Info Title not found"
    assert page.is_displayed(page.SOFTWARE_INFO), "Software Info found"
    assert page.is_displayed(page.VIN), "VIN not found"
    print(" - Vehicle Info Screen Verified.")
