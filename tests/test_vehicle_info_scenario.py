
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

def test_verify_vehicle_info_screen(driver):
    page = VehicleControlPage(driver)
    
    # Start Activity
    print("\n[Step] Starting Vehicle Control App...")
    page.start()
    time.sleep(3)
    
    # Test Screen: Vehicle Info (차량 정보)
    print("\n[Step] Testing 'Vehicle Info' Screen...")
    page.click_sidebar_menu("차량 정보")

    toggles = [
        page.SOFTWARE_INFO,
        page.AUTO_UPDATE,
    ]

    for locator in toggles:
        try:

            cam_label = driver.find_element(*locator)
            rect = cam_label.rect # {'x': 100, 'y': 200, 'width': 50, 'height': 20}
            if locator == page.AUTO_UPDATE:
                # Logic: X - 60, Y + 10    
                target_x = rect['x'] - 60
                target_y = rect['y'] + 10
                print(f"Found {locator} at {rect}. Tapping at ({target_x}, {target_y})")

                driver.tap([(target_x, target_y)])
                time.sleep(1)
                driver.tap([(target_x, target_y)])
                time.sleep(1)
   
            if locator == page.SOFTWARE_INFO:
                # Logic: X - 60, Y + 10    
                target_x = rect['x'] + rect['width'] + 30
                target_y = rect['y'] + 10
                print(f"Found {locator} at {rect}. Tapping at ({target_x}, {target_y})")

                driver.tap([(target_x, target_y)])
                time.sleep(1)
                try:
                    popup_save = page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='확인']")
                    popup_save.click()
                    time.sleep(2)
                    print("Confirmed Auto Hold Off popup")
                except NoSuchElementException:
                    print("Auto Hold Popup not found")
            
        except Exception as e:
            print(f"Skipping toggle {locator}: {e}")

    
    page.click(page.FACTORY_RESET)
    time.sleep(1)
    page.click(page.LEGAL_INFO_BUTTON)
    time.sleep(1)
    try:
        popup_save = page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
        popup_save.click()
        print("Confirmed Auto Hold Off popup")
    except NoSuchElementException:
        print("Auto Hold Popup not found")



