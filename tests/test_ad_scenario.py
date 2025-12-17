
import pytest
import time
import random
from appium.webdriver.common.appiumby import AppiumBy

class TestADScenario:
    def test_ad_speed_offset(self, page):
        print("\n[Test] AD: Speed Offset Adjustment")
        page.reset_sidebar()
        page.click_sidebar_menu("AD")
        time.sleep(1)
        
        # Click Auto (Speed Limit)
        page.click(page.AD_SPEED_AUTO)
        time.sleep(1)
        
        # Change Speed Offset (-5 to 5)
        # We need to click Minus or Plus buttons.
        # We'll use the approximate locators we defined: preceding/following sibling of '10km/h'
        # Or if that fails, use bounds derived from XML analysis.
        
        target_offset = random.randint(-5, 5)
        print(f"Target Offset clicks: {target_offset}")
        
        # Locate the Value Text to use as anchor
        try:
             # Try to find the "10km/h" element or similar
             anchor = page.find_element(page.AD_SPEED_VALUE_10)
        except:
             # Fallback: search for any "km/h"
             anchor = page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'km/h')]")

        # Define button locations relative to anchor or use the defined Locators
        # Let's try using the Page Object locators first
        
        if target_offset < 0:
            for _ in range(abs(target_offset)):
                page.click(page.AD_SPEED_MINUS)
                time.sleep(0.5)
        elif target_offset > 0:
             for _ in range(target_offset):
                page.click(page.AD_SPEED_PLUS)
                time.sleep(0.5)
        
        print(f"Adjusted speed by {target_offset}")
