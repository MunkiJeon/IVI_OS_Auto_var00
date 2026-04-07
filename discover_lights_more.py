import sys
import os
import time

# Ensure root is in path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage

def discover_more():
    driver = None
    try:
        driver = DriverFactory.get_driver()
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)
        
        # Navigate to '라이트'
        page.click_sidebar_menu("라이트")
        time.sleep(2)
        
        # Capture Page 1
        driver.save_screenshot("lights_page1.png")
        with open("lights_page1.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)
        
        # Scroll down
        print("[Discovery] Scrolling down...")
        page.scroll_content("down")
        time.sleep(2)
        
        # Capture Page 2
        driver.save_screenshot("lights_page2.png")
        with open("lights_page2.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        # Scroll down again
        print("[Discovery] Scrolling down again...")
        page.scroll_content("down")
        time.sleep(2)
        
        # Capture Page 3
        driver.save_screenshot("lights_page3.png")
        with open("lights_page3.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)

        # Scroll down again
        print("[Discovery] Scrolling down again...")
        page.scroll_content("down")
        time.sleep(2)
        
        # Capture Page 3
        driver.save_screenshot("lights_page4.png")
        with open("lights_page4.xml", "w", encoding="utf-8") as f:
            f.write(driver.page_source)   
            
        print("[Success] Lights screen discovery completed.")
        
    except Exception as e:
        print(f"[Error] {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    discover_more()
