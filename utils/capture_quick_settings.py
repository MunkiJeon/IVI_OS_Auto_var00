
import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# Configuration
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.udid = "192.168.0.204:5555" # DeviceConfig.TCP_DEVICE_ID
options.app_package = "ai.umos.vehiclecontrol"
options.app_activity = "ai.umos.vehiclecontrol.VehicleControlActivity"
options.no_reset = True

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

try:
    print("Starting Vehicle Control App...")
    # Click 'Quick Settings' (빠른 설정)
    time.sleep(3)
    try:
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='빠른 설정']").click()
        print("Clicked 'Quick Settings'...")
        time.sleep(2)
    except:
        print("Could not click 'Quick Settings'. Assuming already there or sidebar issue.")

    # Capture Source
    print("Capturing source...")
    source = driver.page_source
    with open("source_quick_settings_new.xml", "w", encoding="utf-8") as f:
        f.write(source)
    print("Saved source_quick_settings_new.xml")

finally:
    driver.quit()
