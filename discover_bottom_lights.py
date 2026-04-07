import sys
import os
import time

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage
from appium.webdriver.common.appiumby import AppiumBy
import xml.etree.ElementTree as ET

def discover_bottom_lights():
    driver = None
    try:
        driver = DriverFactory.get_driver()
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)
        page.click_sidebar_menu("라이트")
        time.sleep(2)
        
        # Scroll to bottom
        for i in range(4):
            page.scroll_content("down", 1000)
            time.sleep(1)
            
        # Capture context
        driver.save_screenshot("lights_bottom_test.png")
        xml_source = driver.page_source
        with open("lights_bottom_test.xml", "w", encoding="utf-8") as f:
            f.write(xml_source)
            
        print("XML captured. Parsing bounds...")
        root = ET.fromstring(xml_source)
        for elem in root.iter():
            text = elem.get('text', '')
            if text in ['무드 조명', '사운드 연동 조명', '항상 켜기', '주차시', '끄기', '켜기', '자동', '색상']:
                bounds = elem.get('bounds')
                print(f"{text}: {bounds}")
                
        # Also let's try to click 색상 and get parser for popup
        if page.click_text("색상", scroll=False):
            print("Opened Color Popup")
            time.sleep(2)
            driver.save_screenshot("lights_color_popup.png")
            pop_source = driver.page_source
            with open("lights_color_popup.xml", "w", encoding="utf-8") as f:
                f.write(pop_source)
                
            print("Popup XML captured.")
            root = ET.fromstring(pop_source)
            for elem in root.iter():
                text = elem.get('text', '')
                if text or 'Button' in elem.get('class', ''):
                    print(f"Popup Elem [{elem.get('class')}]: '{text}' - {elem.get('bounds')}")
            
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    discover_bottom_lights()
