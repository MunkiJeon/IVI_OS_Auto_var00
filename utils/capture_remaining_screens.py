import time
import os
import sys
from appium import webdriver
from appium.options.android import UiAutomator2Options

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pages.vehicle_control_page import VehicleControlPage
from utils.driver_factory import DriverFactory

def capture_xml(driver, filename):
    print(f"Capturing {filename}...")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"Saved {filename}")

def main():
    driver = DriverFactory.get_driver()
    
    try:
        page = VehicleControlPage(driver)
        
        # Ensure app is started
        page.start()
        time.sleep(5)
        
        if not page.is_loaded():
            print("App not loaded!")
            return

        screens = [
            "편의 기능", "연결", "앱", "보안", "개인정보 보호", 
            "하이패스", "일반 설정", "차량 정보"
        ]

        for screen in screens:
            try:
                print(f"--- Processing {screen} ---")
                time.sleep(1)
                page.click_sidebar_menu(screen)
                time.sleep(2)
                
                # Default capture
                capture_xml(driver, f"source_{screen}.xml")
                
                # Check for scroll requirement
                if screen in ["앱", "하이패스", "일반 설정"]:
                    print(f"Scrolling down for {screen}...")
                    page.scroll_down()
                    time.sleep(1)
                    capture_xml(driver, f"source_{screen}_scroll.xml")
                    
            except Exception as e:
                print(f"Error processing {screen}: {e}")
                
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    main()
