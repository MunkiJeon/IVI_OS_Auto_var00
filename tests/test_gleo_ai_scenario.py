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

def test_gleo_ai_scenario(driver):
    page = VehicleControlPage(driver)
    page.start()
    
    # Click Gleo AI Menu
    print("Navigating to Gleo AI...")
    driver.find_element(*page.MENU_GLEO_AI).click()
    time.sleep(2)
    
    # Verify Elements
    print("Verifying Gleo AI Elements...")
    assert driver.find_element(*page.GLEO_VOICE_1).is_displayed(), "Voice 1 not visible"
    assert driver.find_element(*page.GLEO_VOICE_2).is_displayed(), "Voice 2 not visible"
    assert driver.find_element(*page.GLEO_STYLE).is_displayed(), "Dialogue Style not visible"
    assert driver.find_element(*page.GLEO_START).is_displayed(), "Start Dialogue not visible"

    print("Gleo AI Scenario Passed!")
