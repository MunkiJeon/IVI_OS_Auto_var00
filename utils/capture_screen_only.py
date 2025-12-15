import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "emulator-5554" 
options.app_package = "ai.umos.vehiclecontrol"
options.app_activity = "ai.umos.vehiclecontrol.MainActivity"
options.no_reset = True

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    print("Starting App...")
    time.sleep(5)
    
    # Click Screen (화면) - Using Coordinates as XPath failed
    # Bounds from XML: [731,716][771,744] -> Center approx (750, 730)
    print("Clicking Screen (화면) at coordinates (750, 730)...")
    driver.tap([(750, 730)])
    time.sleep(2)
    
    with open("source_screen.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("Saved source_screen.xml")

except Exception as e:
    print(f"Error: {e}")
finally:
    driver.quit()
