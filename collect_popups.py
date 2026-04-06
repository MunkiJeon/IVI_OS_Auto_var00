from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage
import time
import sys
import os

def collect_ui_state(menu_name, output_prefix):
    driver = None
    try:
        driver = DriverFactory.get_driver()
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)
        
        # Navigate to menu
        print(f"Navigating to {menu_name}...")
        page.click_sidebar_menu(menu_name)
        time.sleep(2)
        
        # Dump current state
        xml_file = f"{output_prefix}_initial.xml"
        png_file = f"{output_prefix}_initial.png"
        print(f"Capturing initial state: {xml_file}")
        with open(xml_file, 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        driver.save_screenshot(png_file)
        
        # Optional: Swipe down to find more (for long menus like Quick Settings)
        if menu_name == '빠른 설정':
            print("Scrolling Quick Settings down...")
            driver.swipe(1400, 800, 1400, 200, 1000)
            time.sleep(2)
            with open(f"{output_prefix}_scrolled.xml", 'w', encoding='utf-8') as f:
                f.write(driver.page_source)
            driver.save_screenshot(f"{output_prefix}_scrolled.png")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python collect_popups.py <menu_name> <output_prefix>")
        sys.exit(1)
        
    menu_name = sys.argv[1]
    output_prefix = sys.argv[2]
    collect_ui_state(menu_name, output_prefix)
