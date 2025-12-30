
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from pages.vehicle_control_page import VehicleControlPage

class TestGeneralSettingsScenario:
    def test_general_settings_full(self, driver):
        print("\n[Test] General Settings: Font, Language, Date/Time, Interactions")
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)

        # Go to General Settings
        page.reset_sidebar()
        page.click_sidebar_menu("일반 설정")
        time.sleep(1)
        FONT_SETTINGS = [
            page.FONT_SETTING_HYUNDAI,
            page.FONT_SETTING_KIA,
            page.FONT_SETTING_BASIC,
            page.FONT_SETTING_GENESIS
        ]

        # --- 1. Font Settings ---
        print("[Step] Font Settings Test")
        for font in FONT_SETTINGS:
            page.click(page.FONT_DROPDOWN)
            time.sleep(1)
            page.click(font)
            time.sleep(1)
        
        print("Checking Apply (Font) button state...")
        
        # Check if enabled (converting to boolean just in case)
        if driver.find_element(*page.FONT_SETTING_APPLY).is_enabled(): 
            print("Apply button is enabled. Clicking...")
            driver.find_element(*page.FONT_SETTING_APPLY).click()
            time.sleep(1)

            try:
                popup_save = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='확인']")
                popup_save.click()
                time.sleep(1)
                print("Confirmed Font popup")

                page.click_sidebar_menu("일반 설정")
                time.sleep(3)
            except NoSuchElementException:
                print("Font Popup not found")
        else:
            print("Apply button is disabled. Skipping popup check.")

        # # --- 2. Language Settings ---

        page.click(page.LANGUAGE_DROPDOWN)
        time.sleep(1)
        
        # Verify 'English' and '한국어' exist
        assert page.is_displayed(page.LANGUAGE_SETTING_EN), "English option not found"
        assert page.is_displayed(page.LANGUAGE_SETTING_KO), "Korean option not found"
        
        # Select English
        print("Switching to English...")
        page.click(page.LANGUAGE_SETTING_EN)
        time.sleep(1) # Wait for UI update (increased)
        try:
            popup_save = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
            popup_save.click()
            time.sleep(1)
            print("Confirmed Language popup")
        except NoSuchElementException:
            print("Language Popup not found")

        page.click(page.LANGUAGE_DROPDOWN)
        time.sleep(1)

        page.click(page.LANGUAGE_SETTING_KO)
        time.sleep(1)
        try:
            popup_save = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Save']")
            popup_save.click()
            time.sleep(1)
            print("Confirmed Language popup")
        except NoSuchElementException:
            print("Language Popup not found")
             
        # --- 3. Date & Time ---
        print("[Step] Date & Time Test")
     
        if not page.is_displayed(page.DATE_TIME_SETTING):
            auto_time_label = driver.find_element(*page.AUTO_TIME_SETTING)
            rect = auto_time_label.rect # {'x': 100, 'y': 200, 'width': 50, 'height': 20}
            
            # Logic: X - 60, Y + 10    
            target_x = rect['x'] - 60
            target_y = rect['y'] + 10
            print(f"Found {page.AUTO_TIME_SETTING} at {rect}. Tapping at ({target_x}, {target_y})")
                
            driver.tap([(target_x, target_y)])
            time.sleep(1)

            if page.is_displayed(page.MANUAL_TIME_SETTING):
                print("Manual Time Setting found.")
            else:
                pytest.fail("Manual Time Setting not found")

        page.scroll_down()
        time.sleep(1)
        page.click(page.MANUAL_TIME_SETTING)
        time.sleep(1)
            
        # --- Popup Interaction (Date/Time Picker) ---
        print("Popup detected. Interacting with Date/Time Pickers...")
        
        # Robust Interaction Strategy:
        # 1. Try to find 'EditText' elements (often the center selected value of a picker).
        # 2. If valid count (5), swipe them.
        # 3. If not, use the '날짜' and '시간' text headers to calculate column positions.
        
        headers_found = False
        pickers = []
        
        # Strategy 1: Find EditTexts (Year, Month, Day, Hour, Minute)
        try:
            pickers = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
            if len(pickers) != 5:
                    # Check for NumberPicker again just in case
                    pickers = driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.NumberPicker")
        except:
            pass
            
        if len(pickers) == 5:
            print(f"Found {len(pickers)} Interactable Elements (EditText/NumberPicker). Swiping...")
            for i, picker in enumerate(pickers):
                try:
                    rect = picker.rect
                    cx = rect['x'] + rect['width'] // 2
                    cy = rect['y'] + rect['height'] // 2
                    # Swipe Up (Drag down) to change value
                    driver.swipe(cx, cy, cx, cy + 100, 300) 
                    time.sleep(0.5)
                    print(f"Swiped picker {i+1}/5")
                except:
                    print(f"Failed to swipe picker {i+1}")
        else:
            print("Specific Picker elements not found. Using Header-Relative Coordinates...")
            # Strategy 2: Header-Relative Swiping
            # We expect '날짜' and '시간' headers to be visible.
            try:
                # Find Headers
                date_header = None
                time_header = None
                
                # Try Korean Headers first
                try:
                    date_header = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='날짜']")
                    time_header = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='시간']")
                except:
                    # Try English Headers
                    date_header = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Date')]")
                    time_header = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Time')]")
                    
                # Find Save Button for Y-bound (Bottom reference)
                save_btn = driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='저장' or @text='Save' or @text='확인' or @text='OK']")
                
                if date_header and time_header and save_btn:
                    # Calculated Y center for swipe: Midpoint between Header and Save Button
                    header_bottom = date_header.rect['y'] + date_header.rect['height']
                    save_top = save_btn.rect['y']
                    swipe_cy = (header_bottom + save_top) // 2
                    
                    # Date Columns (Year, Month, Day) under "Date" Header
                    dr = date_header.rect
                    # Estimated X positions: 20%, 50%, 80% of Date Header Width
                    d_x1 = dr['x'] + dr['width'] * 0.20 # Year
                    d_x2 = dr['x'] + dr['width'] * 0.50 # Month
                    d_x3 = dr['x'] + dr['width'] * 0.80 # Day
                    
                    # Time Columns (Hour, Minute) under "Time" Header
                    tr = time_header.rect
                    # Estimated X positions: 30%, 70% of Time Header Width
                    t_x1 = tr['x'] + tr['width'] * 0.30 # Hour
                    t_x2 = tr['x'] + tr['width'] * 0.70 # Minute
                    
                    swipe_points = [d_x1, d_x2, d_x3, t_x1, t_x2]
                    
                    for i, sx in enumerate(swipe_points):
                        driver.swipe(sx, swipe_cy, sx, swipe_cy + 100, 300) # Swipe Down
                        time.sleep(0.5)
                        print(f"Swiped Column {i+1}/5 (Coordinate)")
                        
                else:
                    print("Critical: Headers or Save button not found for coordinate calculation.")
                    
            except Exception as e:
                print(f"Fallback Coordinate Swipe Failed: {e}")

        # Click Save '저장'
        print("Clicking Save (저장)...")
        try:
            driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='저장' or @text='Save']").click()
            time.sleep(2)
            print("Date/Time Settings Saved.")
        except:
            print("Save button click failed.")

        auto_time_label = driver.find_element(*page.AUTO_TIME_SETTING)
        rect = auto_time_label.rect # {'x': 100, 'y': 200, 'width': 50, 'height': 20}
            
        # Logic: X - 60, Y + 10    
        target_x = rect['x'] - 60   
        target_y = rect['y'] + 10
        print(f"Found {page.AUTO_TIME_SETTING} at {rect}. Tapping at ({target_x}, {target_y})")
            
        driver.tap([(target_x, target_y)])
        time.sleep(1)

        page.MANUAL_TIME_TYPE_12.click()
        time.sleep(1)
        page.MANUAL_TIME_TYPE_24.click()
        time.sleep(1)
        
    
