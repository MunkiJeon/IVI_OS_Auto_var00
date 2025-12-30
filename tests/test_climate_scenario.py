
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

class TestClimateScenario:
    def test_climate_toggles(self, driver):
        print("\n[Test] Climate: Toggle all buttons")
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)
        
        page.reset_sidebar()
        page.click_sidebar_menu("공조")
        time.sleep(1)
        
        # List of Toggle Texts from XML/Page Object
        toggles = [
            page.CLIMATE_WASHER,
            page.CLIMATE_TUNNEL,
            page.CLIMATE_AIR_QUALITY,
            page.CLIMATE_OVERHEAT,
            page.CLIMATE_AUTO_DRY
        ]

        for locator in toggles:
            try:
                # page.scroll_to_element(locator) #화면 스크롤 해야되는 경우 활성화

                cam_label = driver.find_element(*locator)
                rect = cam_label.rect # {'x': 100, 'y': 200, 'width': 50, 'height': 20}
             
                # Logic: X - 60, Y + 10    
                target_x = rect['x'] - 60
                target_y = rect['y'] + 10
             
                print(f"Found {locator} at {rect}. Tapping at ({target_x}, {target_y})")
                
                driver.tap([(target_x, target_y)])
                time.sleep(1)
                driver.tap([(target_x, target_y)])
                time.sleep(1)
                
            except Exception as e:
                print(f"Skipping toggle {locator}: {e}")
