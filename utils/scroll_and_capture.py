from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import os

APPIUM_SERVER_URL = "http://127.0.0.1:4723"
DEVICE_ID = "192.168.0.111:5555"
APP_PACKAGE = "ai.umos.vehiclecontrol"
APP_ACTIVITY = "ai.umos.vehiclecontrol.VehicleControlActivity"

def scroll_and_capture():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.udid = DEVICE_ID
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.no_reset = True
    options.new_command_timeout = 300

    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    
    try:
        print("Explicitly launching Vehicle Control Activity...")
        try:
            driver.terminate_app(APP_PACKAGE)
        except:
            pass
        driver.execute_script('mobile: startActivity', {
            'component': f"{APP_PACKAGE}/{APP_ACTIVITY}"
        })
        time.sleep(6)
        
        # Initial dump
        with open("sidebar_page_1.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        print("Attempting to scroll sidebar...")
        # Sidebar bounds approx x=640 to x=993. Center x=816.
        # Swipe from bottom (y=800) to top (y=300)
        driver.swipe(816, 800, 816, 200, 1000)
        time.sleep(3)
        
        with open("sidebar_page_2.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
            
        # Swipe again just in case
        driver.swipe(816, 800, 816, 200, 1000)
        time.sleep(3)
        with open("sidebar_page_3.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        print("Captured 3 pages of sidebar.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    scroll_and_capture()
