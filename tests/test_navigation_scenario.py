
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_navigation_scenario(driver):
    page = VehicleControlPage(driver)
    page.start()
    
    # Click Navigation Menu
    print("Navigating to Navigation...")
    page.click(page.MENU_NAVIGATION)
    time.sleep(5) # Increased wait for screen transition
    
    # Verify Elements
    print("Verifying Navigation Elements...")
    assert page.is_displayed(page.NAV_CHARGING_STATION), "Charging Station not visible"
    assert page.is_displayed(page.NAV_EV_ROUTE), "EV Route not visible"
    assert page.is_displayed(page.NAV_PREF_STATION), "Preferred Station not visible"
    
    # Check Version (Dynamic text check)
    # Using generic check or specific locator
    version_element = page.find_element(page.NAV_VERSION)
    print(f"Navigation Version: {version_element.text}")
    assert version_element.is_displayed(), "Version info not visible"

    print("Navigation Scenario Passed!")
