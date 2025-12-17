
import pytest
import time
import random
from appium.webdriver.common.appiumby import AppiumBy

class TestSeatScenario:
    def test_seat_adjustment(self, page):
        print("\n[Test] Seat: Position and Save")
        page.reset_sidebar()
        page.click_sidebar_menu("시트 포지션")
        time.sleep(1)
        
        # Click Memory 1
        page.click(page.SEAT_MEMORY_1)
        time.sleep(1)
        
        # Click Memory 2
        page.click(page.SEAT_MEMORY_2)
        time.sleep(1)
        
        # Arbitrary adjustment
        # Tapping the driver seat image generally to simulate adjustment
        try:
             seat_header = page.find_element(page.SEAT_DRIVER)
             # Tap below header
             loc = seat_header.location
             dims = seat_header.size
             center_x = loc['x'] + dims['width'] // 2
             center_y = loc['y'] + dims['height'] + 200 # 200px below
             page.driver.tap([(center_x, center_y)])
             print("Tapped simulated seat area")
        except:
             print("Could not simulate seat tap")

        time.sleep(1)
        
        # Click Save
        page.click(page.SEAT_SAVE)
        time.sleep(1)
