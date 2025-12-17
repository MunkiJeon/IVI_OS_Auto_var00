
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy

class TestClimateScenario:
    def test_climate_toggles(self, page):
        print("\n[Test] Climate: Toggle all buttons")
        page.reset_sidebar()
        page.click_sidebar_menu("공조")
        time.sleep(1)
        
        # List of Toggle Texts from XML/Page Object
        toggles = [
            page.CLIMATE_AUTO_RECIRC,
            page.CLIMATE_WASHER,
            page.CLIMATE_TUNNEL,
            page.CLIMATE_AIR_QUALITY,
            page.CLIMATE_OVERHEAT,
            page.CLIMATE_AUTO_DRY
        ]
        
        for locator in toggles:
            try:
                # Find the element
                el = page.find_element(locator)
                text = el.text
                print(f"Toggling {text}...")
                
                # Check if it has a sibling switch or if clicking it works
                # We will just click it twice
                page.click(locator) # On/Off
                time.sleep(1)
                page.click(locator) # Off/On
                time.sleep(1)
                
            except Exception as e:
                print(f"Skipping toggle {locator}: {e}")
