import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage
from appium.webdriver.common.appiumby import AppiumBy

def capture_lights_scrolled():
    driver = DriverFactory.get_driver()
    try:
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)
        
        print("Navigating to Lights tab...")
        if page.is_displayed(page.MENU_LIGHTS):
            page.click(page.MENU_LIGHTS)
            time.sleep(2)
        
        print("Scrolling down...")
        # Get screen size
        size = driver.get_window_size()
        start_x = size['width'] // 2 + 300 # Right side (content area)
        start_y = size['height'] * 3 // 4  # Bottom Quarter
        end_y = size['height'] // 4        # Top Quarter
        
        # Perform swipe (Scroll down)
        driver.swipe(start_x, start_y, start_x, end_y, 1000)
        time.sleep(2) # Wait for animation

        print("Dumping detailed page source...")
        source = driver.page_source
        with open("source_lights_scrolled.xml", "w", encoding="utf-8") as f:
            f.write(source)
        print("Saved to source_lights_scrolled.xml")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    capture_lights_scrolled()
