
import pytest
import time
import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

class TestHiPassScenario:
    def test_hi_pass_scenario(self, driver):
        self.page = VehicleControlPage(driver)
        
        # Start Activity
        print("\n[Step] Starting Vehicle Control App...")
        self.page.start()
        time.sleep(3)
        
        # Test Screen: Hi-Pass (하이패스)
        print("\n[Step] Testing 'Hi-Pass' Screen...")
        self.page.click_sidebar_menu("하이패스")
        time.sleep(1)
        
        assert self.page.is_displayed(self.page.HIPASS_TITLE), "Hi-Pass Title not found"
        assert self.page.is_displayed(self.page.PAYMENT_INFO), "Payment Info section not found"
        assert self.page.is_displayed(self.page.PAYMENT_DISPLAY), "Payment Display toggle not found"
        print(" - Hi-Pass Screen Verified.")
