from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import time
import os
import sys

# Add project root to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import AppConfig
from utils.driver_factory import DriverFactory

def capture_screens():
    driver = DriverFactory.get_driver()
    
    try:
        # Start App
        driver.terminate_app(AppConfig.VEHICLE_CONTROL['package'])
        driver.execute_script('mobile: startActivity', {
            'component': f"{AppConfig.VEHICLE_CONTROL['package']}/{AppConfig.VEHICLE_CONTROL['activity']}"
        })
        time.sleep(3)

        # 1. Capture 'Quick Settings' (빠른 설정)
        # It is the default screen, but click ensures we are there.
        print("Navigating to Quick Settings...")
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='빠른 설정']").click()
        time.sleep(2)
        with open("source_qs.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Captured source_qs.xml")

        # 2. Capture 'Driving' (주행) - Top
        print("Navigating to Driving...")
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='주행']").click()
        time.sleep(2)
        with open("source_driving_top.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Captured source_driving_top.xml")

        # 3. Scroll and Capture 'Driving' - Mid
        print("Scrolling Driving page (1/2)...")
        size = driver.get_window_size()
        start_x = size['width'] * 3 // 4
        start_y = size['height'] * 3 // 4
        end_y = size['height'] // 4
        
        driver.swipe(start_x, start_y, start_x, end_y, 1000)
        time.sleep(2)
        with open("source_driving_mid.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Captured source_driving_mid.xml")

        # 4. Scroll and Capture 'Driving' - Bot
        print("Scrolling Driving page (2/2)...")
        driver.swipe(start_x, start_y, start_x, end_y, 1000)
        time.sleep(2)
        with open("source_driving_bot.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        print("Captured source_driving_bot.xml")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    capture_screens()
