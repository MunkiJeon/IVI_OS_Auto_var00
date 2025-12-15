import sys
import os
import time

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage

def capture_lights_screen():
    driver = DriverFactory.get_driver()
    try:
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3) # Wait for launch
        
        print("Navigating to Lights (라이트)...")
        if page.is_displayed(page.MENU_LIGHTS):
            page.click(page.MENU_LIGHTS)
            time.sleep(3) # Wait for screen transition
        else:
            print("Error: Lights menu not found!")
            return

        print("Dumping page source...")
        source = driver.page_source
        with open("source_lights.xml", "w", encoding="utf-8") as f:
            f.write(source)
        print("Saved to source_lights.xml")
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    capture_lights_screen()
