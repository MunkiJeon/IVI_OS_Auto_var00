
import pytest
import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

class TestADScenario:
    def test_ad_speed_offset(self, driver):
        print("\n[Test] AD: Speed Offset Adjustment")
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(1)
        
        page.click_sidebar_menu("AD")
        time.sleep(1)
        
        page.click(page.AD_SPEED_CURRENT)
        print("Speed current")
        time.sleep(1)
     
        # Click Auto (Speed Limit)
        page.click(page.AD_SPEED_AUTO)
        print("Speed auto")
        time.sleep(1)
        
        # Change Speed Offset (-5 to 5)
        target_offset = random.randint(-5, 5)
        print(f"Target Offset clicks: {target_offset}")
        
        # Determine strict direction and count
        x, y = 0, 0
        if page.is_displayed(page.AD_SPEED_TARGET):
            print("Speed target is 10km/h => 5회 감속")
            for _ in range(5):
                # Use page defined locator for Minus
                x, y = page.AD_IconBtn["AD_SPEED_MINUS"]
                driver.tap([(x*1920, y*1080)])
                time.sleep(0.5) 

        print(f"Decreasing speed offset by {target_offset}")
        for _ in range(abs(target_offset)):
            if target_offset < 0: x, y = page.AD_IconBtn["AD_SPEED_MINUS"]
            elif target_offset > 0: x, y = page.AD_IconBtn["AD_SPEED_PLUS"]
            driver.tap([(x*1920, y*1080)])
            time.sleep(0.5)

        page.click(page.AD_LANE_CHANGE_AUTO)
        print("Lane change auto")
        time.sleep(1)

        page.click(page.AD_LANE_CHANGE_CONFIRM)
        print("Lane change confirm")
        time.sleep(1)
