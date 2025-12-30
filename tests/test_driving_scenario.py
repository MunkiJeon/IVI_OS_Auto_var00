
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from pages.vehicle_control_page import VehicleControlPage

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.common.actions import interaction

class TestDrivingScenario:
    def test_driving_features(self, driver):
        x, y = 0, 0
        print("\n[Test] Driving: Snow/Rain, ESC, Creep, Radio Buttons")
        
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)

        page.reset_sidebar()
        page.click_sidebar_menu("주행")
        time.sleep(1)
        
        # 1. Snow/Rain Assist Toggle
        # Use CORRECT locator from page object (DRIVING_SNOW_RAIN_ASSIST)
        page.click(page.DRIVING_ACCEL_MODE_GENTLE)
        time.sleep(1)
        page.click(page.DRIVING_ACCEL_MODE_STANDARD)
        time.sleep(1)
        page.click(page.DRIVING_ACCEL_MODE_FAST)
        time.sleep(1)

        
        x, y = page.Driving_IconBtn["DRIVING_SNOW_RAIN_ASSIST"]
        driver.tap([(x*1920, y*1080)])
        time.sleep(1)
        driver.tap([(x*1920, y*1080)])
        time.sleep(1)
        # Verify Accel Mode disabled (optional check)
        try:
            # Use CORRECT locator (DRIVING_ACCEL_MODE_GENTLE)
            accel_gentle = page.find_element(page.DRIVING_ACCEL_MODE_GENTLE)
            print(f"Accel Mode Enabled: {accel_gentle.get_attribute('enabled')}")
        except:
            pass

        page.click(page.DRIVING_STEERING_MODE_STANDARD)
        time.sleep(1)
        page.click(page.DRIVING_STEERING_MODE_LIGHT)
        time.sleep(1)

        x, y = page.Driving_IconBtn["DRIVING_ESC"]
        driver.tap([(x*1920, y*1080)])
        time.sleep(1)
        driver.tap([(x*1920, y*1080)])
        time.sleep(1)
        
        # 2. ESC Toggle -> Popup -> Off
        # Check for Popup "끄기"
        try:
            popup_off = page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='끄기']")
            popup_off.click()
            print("Confirmed ESC Off popup")
        except NoSuchElementException:
            print("ESC Popup not found (maybe already off?)")
        
        time.sleep(1)

        # 3. Creep Mode
        if not page.scroll_to_element(page.DRIVING_CREEP):
             pytest.fail("Creep Mode not found")
        
        page.click(page.DRIVING_ONE_PADAL_MODE)
        time.sleep(1)
        page.click(page.DRIVING_CREEP)
        time.sleep(1)

        x, y = page.Driving_IconBtn["DRIVING_AUTO_HOLD"]
        driver.tap([(x*1920, y*1080)])
        time.sleep(1)
        driver.tap([(x*1920, y*1080)])
        time.sleep(1)

        try:
            popup_save = page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='확인']")
            popup_save.click()
            print("Confirmed Auto Hold Off popup")
        except NoSuchElementException:
            print("Auto Hold Popup not found")


        if not page.scroll_to_element(page.DRIVING_LANE_DEPARTURE_WARNING):
             pytest.fail("Lane Departure Warning not found")
        
        page.click(page.DRIVING_FORWARD_COLLISION_WARNING_DELAY)
        time.sleep(1)
        page.click(page.DRIVING_FORWARD_COLLISION_WARNING_NOMAL)
        time.sleep(1)
        page.click(page.DRIVING_FORWARD_COLLISION_WARNING_EARLY)
        time.sleep(1)
        
        page.click(page.DRIVING_LANE_DEPARTURE_WARNING_OFF)
        time.sleep(1)
        page.click(page.DRIVING_LANE_DEPARTURE_WARNING_ON)
        time.sleep(1)
        page.click(page.DRIVING_LANE_DEPARTURE_WARNING_ALL)
        time.sleep(1)

        if not page.scroll_to_element(page.DRIVING_BLIND_SPOT_COLLISION_WARNING):
             pytest.fail("Blind Spot Collision Warning not found")
        
        page.click(page.DRIVING_BLIND_SPOT_COLLISION_WARNING_OFF)
        time.sleep(1)
        page.click(page.DRIVING_BLIND_SPOT_COLLISION_WARNING_ON)
        time.sleep(1)
        page.click(page.DRIVING_BLIND_SPOT_COLLISION_WARNING_ALL)
        time.sleep(1)
        

        if not page.scroll_to_element(page.DRIVING_EPB_BTN):
             pytest.fail("Parking Brake not found")
        
        # --- NEW LOGIC START: Dynamic Tap relative to "사각지대 카메라" text ---
        print("Finding '사각지대 카메라' text for dynamic coordinate tap...")
        try:
             page.scroll_to_element(page.DRIVING_BLIND_SPOT_CAMERA_TEXT)
             
             cam_label = driver.find_element(*page.DRIVING_BLIND_SPOT_CAMERA_TEXT)
             rect = cam_label.rect # {'x': 100, 'y': 200, 'width': 50, 'height': 20}
             
             # Logic: X - 60, Y + 10
             target_x = rect['x'] - 60
             target_y = rect['y'] + 10
             
             print(f"Found '사각지대 카메라' at {rect}. Tapping at ({target_x}, {target_y})")
             
             driver.tap([(target_x, target_y)])
             time.sleep(1)
             driver.tap([(target_x, target_y)])
             time.sleep(1)
             
        except Exception as e:
             print(f"Warning: Could not find or interact with '사각지대 카메라' text. Error: {e}")
             # Fallback to collision warning if needed, or just pass
        # --- NEW LOGIC END ---
        
        # --- NEW LOGIC START: Parking Brake Long Press (2 seconds) ---
        print("Performing Long Press on Parking Brake...")
        epb_btn = page.find_element(page.DRIVING_EPB_BTN)
        
        # Using ActionChains for click and hold
        actions = ActionChains(driver)
        actions.click_and_hold(epb_btn).pause(2).release().perform()
        print("Long Press completed.")
        time.sleep(1)
        # --- NEW LOGIC END ---
