
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_verify_hipass_screen(driver):
    page = VehicleControlPage(driver)
    
    # Start Activity
    print("\n[Step] Starting Vehicle Control App...")
    page.start()
    time.sleep(3)
    
    # Test Screen: Hi-Pass (하이패스)
    print("\n[Step] Testing 'Hi-Pass' Screen...")
    page.click_sidebar_menu("하이패스")
    time.sleep(1)
    
    assert page.is_displayed(page.HIPASS_TITLE), "Hi-Pass Title not found"
    assert page.is_displayed(page.PAYMENT_INFO), "Payment Info section not found"
    assert page.is_displayed(page.PAYMENT_DISPLAY), "Payment Display toggle not found"
    print(" - Hi-Pass Screen Verified.")
