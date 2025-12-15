import pytest
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

@pytest.fixture(scope="function")
def driver():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.automation_name = "UiAutomator2"
    options.device_name = "emulator-5554" 
    options.app_package = "ai.umos.vehiclecontrol"
    options.app_activity = "ai.umos.vehiclecontrol.MainActivity"
    options.no_reset = True
    
    driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
    yield driver
    driver.quit()

def test_profile_scenario(driver):
    page = VehicleControlPage(driver)
    page.start()
    
    # Click Profile Menu
    print("Navigating to Profile (with auto-scroll)...")
    page.reset_sidebar()
    page.click_sidebar_menu("프로필")
    time.sleep(2)
    
    # Verify Elements
    print("Verifying Profile Elements...")
    assert driver.find_element(*page.PROFILE_SETTINGS).is_displayed(), "Profile Settings not visible"
    print("Settings verified.")
    assert driver.find_element(*page.PROFILE_DRIVER).is_displayed(), "Driver Profile not visible"
    print("Driver verified.")
    assert driver.find_element(*page.PROFILE_KEY).is_displayed(), "Key Management not visible"
    print("Key verified.")

    print("Profile Scenario Passed!")
