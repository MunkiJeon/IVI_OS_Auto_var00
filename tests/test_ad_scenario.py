
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
        
        page.reset_sidebar()
        page.click_sidebar_menu("AD")
        time.sleep(1)
        
        page.click(page.AD_SPEED_CURRENT)
        time.sleep(1)
     
        # Click Auto (Speed Limit)
        page.click(page.AD_SPEED_AUTO)
        time.sleep(1)
        
        # Change Speed Offset (-5 to 5)
        target_offset = random.randint(-5, 5)
        print(f"Target Offset clicks: {target_offset}")
        
        # Determine strict direction and count
        x, y = 0, 0
        if target_offset < 0:
            print("Decreasing speed offset...")
            for _ in range(abs(target_offset)):
                # Use page defined locator for Minus
                x, y = page.AD_IconBtn["AD_SPEED_MINUS"]
                driver.tap([(x*1920, y*1080)])
                time.sleep(0.5)
        elif target_offset > 0:
            print("Increasing speed offset...")
            for _ in range(target_offset):
                # Use page defined locator for Plus
                x, y = page.AD_IconBtn["AD_SPEED_PLUS"]
                driver.tap([(x*1920, y*1080)])
                time.sleep(0.5)
        
        print(f"Adjusted speed by {target_offset}")
