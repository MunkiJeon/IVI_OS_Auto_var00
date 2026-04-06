import sys
import os
import time

# Ensure root is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage

def discover():
    driver = None
    try:
        driver = DriverFactory.get_driver()
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)
        
        # 1. Click Sidebar '라이트'
        page.click_sidebar_menu("라이트")
        time.sleep(3)
        
        # 2. Capture Screenshot & XML
        driver.save_screenshot("lights_main.png")
        with open("lights_main.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
            
        print("[Success] Lights screen captured: lights_main.png / lights_main.xml")
        
    except Exception as e:
        print(f"[Error] {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    discover()
