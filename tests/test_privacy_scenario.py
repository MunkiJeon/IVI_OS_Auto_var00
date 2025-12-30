
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_verify_privacy_screen(driver):
    print("\n[Step] Starting Vehicle Control App...")
    page = VehicleControlPage(driver)
    page.start()
    time.sleep(3)
    
    page.reset_sidebar()
    page.click_sidebar_menu("개인정보 보호")
    time.sleep(1)
    
    toggles = [
        page.MIC_USAGE,
        page.LOCATION_USAGE,
        page.CAMERA_USAGE
    ]

    for locator in toggles:
        try:
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