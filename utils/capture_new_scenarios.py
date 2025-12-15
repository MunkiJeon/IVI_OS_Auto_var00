from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import os

# Configuration
options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'UiAutomator2'
options.device_name = 'emulator-5554'
options.app_package = 'ai.umos.vehiclecontrol'
options.app_activity = 'ai.umos.vehiclecontrol.MainActivity'
options.no_reset = True

driver = webdriver.Remote('http://localhost:4723', options=options)

def save_xml(filename):
    with open(filename, "w", encoding='utf-8') as f:
        f.write(driver.page_source)
    print(f"Saved {filename}")

def scroll_down():
    # Scroll from center right to top right (pulling up)
    driver.swipe(1400, 800, 1400, 200, 1000)
    time.sleep(2)

try:
    time.sleep(3)
    
    # 1. Lock Screen
    print("Capturing Lock Screen...")
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='잠금']").click()
    time.sleep(2)
    save_xml("source_lock_top.xml")
    scroll_down()
    save_xml("source_lock_bot.xml")
    
    # 2. Seat Position Screen
    print("Capturing Seat Position Screen...")
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='시트 포지션']").click()
    time.sleep(2)
    save_xml("source_seat_default.xml")
    
    # We need to click specific areas for seats.
    # Analyzing source_seat_default.xml will pinpoint exact click locations later, 
    # but for now we try to click broadly or rely on blind coordinates if we don't have locators yet.
    # However, since we are just capturing now, let's capture the default state first.
    # To be effective, I might need to know WHERE to click. 
    # Let's save the default first, analyze it, and then maybe run a second pass for interactions?
    # Or I can try to find elements with text "운전석", "동승석" etc if they exist in the default view.
    
    # 3. Climate Screen
    print("Capturing Climate Screen...")
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='공조']").click()
    time.sleep(2)
    save_xml("source_climate.xml")
    
    # 4. Charging Screen
    print("Capturing Charging Screen...")
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='충전']").click()
    time.sleep(2)
    save_xml("source_charging_top.xml")
    scroll_down()
    save_xml("source_charging_bot.xml")

finally:
    driver.quit()
