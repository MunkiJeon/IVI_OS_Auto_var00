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

def test_sound_scenario(driver):
    page = VehicleControlPage(driver)
    page.start()
    
    # Click Sound Menu
    print("Navigating to Sound (with auto-scroll)...")
    page.reset_sidebar()
    page.click_sidebar_menu("사운드")
    time.sleep(2)
    
    # Verify Elements
    print("Verifying Sound Elements...")
    assert driver.find_element(*page.SOUND_VOLUME).is_displayed(), "Volume not visible"
    assert driver.find_element(*page.SOUND_SYSTEM).is_displayed(), "System Volume not visible"
    assert driver.find_element(*page.SOUND_MEDIA).is_displayed(), "Media Volume not visible"

    print("Sound Scenario Passed!")
