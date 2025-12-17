
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException

class TestDrivingScenario:
    def test_driving_features(self, page):
        print("\n[Test] Driving: Snow/Rain, ESC, Creep, Radio Buttons")
        page.reset_sidebar()
        page.click_sidebar_menu("주행")
        time.sleep(1)
        
        # 1. Snow/Rain Assist Toggle
        # Assuming the text is the label, the toggle is likely a sibling or parent container click.
        # We'll try clicking the text label first, or look for a Toggle sibling.
        
        # Find Snow Assist label
        snow_assist = page.find_element(page.DRIVING_SNOW_ASSIST)
        # Click it (assuming clicking label toggles it, or locate sibling)
        snow_assist.click() 
        time.sleep(1)
        
        # Verify Accel Mode disabled (optional check)
        # generic check: find "Gentle" and check 'enabled' attribute
        try:
            accel_gentle = page.find_element(page.DRIVING_ACCEL_GENTLE)
            print(f"Accel Mode Enabled: {accel_gentle.get_attribute('enabled')}")
        except:
            pass

        # 2. ESC Toggle -> Popup -> Off
        page.click(page.DRIVING_ESC) # Click to deactivate?
        time.sleep(1)
        # Check for Popup "끄기"
        try:
            popup_off = page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='끄기']")
            popup_off.click()
            print("Confirmed ESC Off popup")
        except NoSuchElementException:
            print("ESC Popup not found (maybe already off?)")
        
        time.sleep(1)

        # 3. Creep Mode
        if not page.scroll_to_element(page.DRIVING_CREEP, max_scrolls=3):
             pytest.fail("Creep Mode not found")
        
        page.click(page.DRIVING_CREEP)
        time.sleep(1)
        
        # Verify Auto Hold appears
        if not page.scroll_to_element(page.DRIVING_AUTO_HOLD, max_scrolls=2):
             pytest.fail("Auto Hold did not appear after selecting Creep Mode (or not found)")
        print("Auto Hold appeared")
             
        # Toggle Auto Hold -> Popup?
        page.click(page.DRIVING_AUTO_HOLD)
        time.sleep(1)
        # Check for popup if disabling
        try:
            popup_off = page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='끄기']")
            popup_off.click()
            print("Confirmed Auto Hold Off popup")
        except:
            pass # Maybe checking logic was reversed or enabled

        # 4. Radio Buttons Loop
        # Find all radio buttons visible
        radios = page.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.RadioButton")
        print(f"Found {len(radios)} radio buttons. Clicking each...")
        for rb in radios:
            try:
                rb.click()
                time.sleep(0.5)
            except:
                pass
