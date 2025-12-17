
import pytest
import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

class TestLightsScenario:
    
    def test_lights_switching(self, driver):
        """
        Navigate to Lights screen and toggle various light settings.
        """
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)
        
        print("Navigating to Lights tab...")
        page.click(page.MENU_LIGHTS)
        
        # Verify presence of key sections with Wait
        print("Waiting for Escort Light option...")
        if not page.wait_for_element(page.LIGHT_ESCORT):
            print("Escort Light not found. Dumping source for debug...")
            print(driver.page_source[:500]) # Print first 500 chars
            pytest.fail("Failed to switch to Lights tab or find Escort Light")
            
        assert page.is_displayed(page.LIGHT_ESCORT), "Escort Light option not found"
        
        # Scenario: Frunk Light Toggle (Off -> On -> Auto)
        print("Testing Frunk Light Toggles...")
        actions = [
            (page.LIGHT_FRUNK_ON, "Frunk Light ON"),
            (page.LIGHT_FRUNK_AUTO, "Frunk Light AUTO"),
            (page.LIGHT_FRUNK_OFF, "Frunk Light OFF")
        ]
        
        for locator, name in actions:
            print(f"Selecting {name}...")
            # Check if visible before clicking to be safe (handling scroll if needed later)
            if page.is_displayed(locator):
                page.click(locator)
                time.sleep(1)
            else:
                print(f"Warning: {name} not visible (might need scroll)")

        # Scenario: Trunk Light Toggle (Off -> On -> Auto)
        print("Testing Trunk Light Toggles...")
        trunk_actions = [
            (page.LIGHT_TRUNK_ON, "Trunk Light ON"),
            (page.LIGHT_TRUNK_AUTO, "Trunk Light AUTO"),
            (page.LIGHT_TRUNK_OFF, "Trunk Light OFF")
        ]

        for locator, name in trunk_actions:
            print(f"Selecting {name}...")
            if page.is_displayed(locator):
                page.click(locator)
                time.sleep(1)
            else:
                 print(f"Warning: {name} not visible")
        
        # Scenario: Scroll down to reveal Interior/Mood Lights
        print("Scrolling down to find Interior/Mood Lights...")
        page.scroll_down()
        time.sleep(2)

        # check Interior Lights
        print("Testing Interior Lights...")
        if page.is_displayed(page.LIGHT_INTERIOR_ALL_SEATS):
            page.click(page.LIGHT_INTERIOR_ALL_SEATS)
            time.sleep(1)
            page.click(page.LIGHT_INTERIOR_DRIVER) # Toggle Driver Seat
            time.sleep(1)
        else:
            print("Error: Interior Lights 'All Seats' button not found after scroll.")

        # Check Mood Lights
        print("Testing Mood Lights...")
        if page.is_displayed(page.LIGHT_MOOD_ON):
            page.click(page.LIGHT_MOOD_ON)
            time.sleep(1)
            
            # Try to adjust brightness if visible
            if page.is_displayed(page.LIGHT_MOOD_BRIGHTNESS):
                print("Adjusting Mood Light Brightness...")
                # Simple tap on the bar (center) or logic to slide could be added
                # For now just checking presence
                page.is_displayed(page.LIGHT_MOOD_BRIGHTNESS)
        else:
             print("Error: Mood Light 'On' button not found after scroll.")

        # Extra Scroll as per User Request
        print("Performing extra scroll to ensure all bottom elements are visible...")
        page.scroll_down()
        time.sleep(2)
        
        # Re-verify Mood Lights after extra scroll
        print("Re-verifying Mood Lights after extra scroll...")
        if page.is_displayed(page.LIGHT_MOOD_ON):
             print("Verified: Mood Light 'On' button is visible.")
        else:
             print("Error: Mood Light 'On' button not visible after extra scroll.")

        print("Lights scenario completed.")

        if not page.scroll_to_element(page.LIGHTS_MOOD, max_scrolls=3):
            pytest.fail("Mood Light not found")
        
        try:
            # Click Mood Light to enter/expand
            page.click(page.LIGHTS_MOOD)
            time.sleep(1)
            
            # Click "On" (Assuming generic 'On' text locator for now)
            try:
                on_xpath = "//android.widget.TextView[@text='색상']"
                page.click((AppiumBy.XPATH, on_xpath))
                print("Clicked 'On'")
            except:
                 print("Could not find 'On' button, checking Color button directly.")

            time.sleep(1)

            # Click 'Color'
            # If not found, swipe up?
            try:
                page.click(page.LIGHTS_COLOR_BTN)
                print("Clicked 'Color'")
            except:
                print("'Color' button not found. Dumping source...")
                # Try finding any TextView that looks like color?
                # Dump source to stdout for debugging
                # print(page.driver.page_source)
                pytest.fail("'Color' button not found.")
                
            time.sleep(1)
            
            # Pick Random Color
            dims = page.driver.get_window_size()
            x = dims['width'] // 2
            y = dims['height'] // 2
            page.driver.tap([(x, y)]) 
            print("Tapped Center (Random Color)")
            time.sleep(1)
            
            # Click Save
            page.click(page.LIGHTS_SAVE_BTN)
            print("Clicked Save")
            time.sleep(1)
            
        except Exception as e:
            print(f"Error in Lights Test: {e}")
            from datetime import datetime
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            with open(f"error_source_lights_{timestamp}.xml", "w", encoding='utf-8') as f:
                f.write(page.driver.page_source)
            pytest.fail(f"Test failed: {e}")
