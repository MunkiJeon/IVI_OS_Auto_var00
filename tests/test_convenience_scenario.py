
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_verify_convenience_screen(driver):
    page = VehicleControlPage(driver)
    
    # Start Activity
    print("\n[Step] Starting Vehicle Control App...")
    page.start()
    time.sleep(3)
    
    # Test Screen: Convenience (편의 기능)
    print("\n[Step] Testing 'Convenience' Screen...")
    page.click_sidebar_menu("편의 기능")
    time.sleep(1)
    
    assert page.is_displayed(page.CONVENIENCE_TITLE), "Convenience Title not found"
    assert page.is_displayed(page.CAR_WASH_MODE), "Car Wash Mode not found"
    assert page.is_displayed(page.VALET_MODE), "Valet Mode not found"
    print(" - Convenience Screen Verified.")
