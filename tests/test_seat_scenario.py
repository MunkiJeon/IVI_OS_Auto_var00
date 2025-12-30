
import pytest
import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

class TestSeatScenario:
     def test_seat_selection_sequence(self, driver):
        print("\n[Test] Seat: Selection Sequence (Driver -> Console -> Passenger -> Rear R -> Rear L)")
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)
        
        page.reset_sidebar()
        page.click_sidebar_menu("시트 포지션")
        time.sleep(2)
        
        # Click IconBtn
        x, y = page.SEAT_IconBtn["COMFORTABLE_RIDE"]
        driver.tap([(x*1920, y*1080)])
        time.sleep(1)
        driver.tap([(x*1920, y*1080)])
        time.sleep(1)

        sequence = [
            "이동식 콘솔",
            "동승석",
            "뒷좌석 우측",
            "뒷좌석 좌측",
            "운전석"
        ]
        
        SCREEN_WIDTH = 1920
        SCREEN_HEIGHT = 1080
        
        # Attempt to get actual size
        try:
            size = driver.get_window_size()
            SCREEN_WIDTH = size['width']
            SCREEN_HEIGHT = size['height']
        except:
            pass

        for target_name in sequence:
            print(f"Selecting '{target_name}'...")
            if target_name not in page.SEAT_TOUCH_POINTS:
                print(f"Warning: {target_name} coordinates not defined.")
                continue
                
            rx, ry = page.SEAT_TOUCH_POINTS[target_name]
            x = int(1920 * rx)
            y = int(1080 * ry)
            
            print(f"Tapping at ({x}, {y})")
            driver.tap([(x, y)])
            time.sleep(1) # Wait for animation/selection


        if not page.scroll_to_element(page.SEAT_HANDLE):
            pytest.fail("Driver Handle not found")

        page.click(page.SEAT_HANDLE)
        time.sleep(1)

        try:
            popup_save = page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
            popup_save.click()
            print("Confirmed Auto Hold Off popup")
        except NoSuchElementException:
            print("Auto Hold Popup not found")
