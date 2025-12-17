from appium import webdriver
from appium.options.android import UiAutomator2Options
import time
import os

# Configuration matches config.py
APPIUM_SERVER_URL = "http://127.0.0.1:4723"
DEVICE_ID = "192.168.0.111:5555"
APP_PACKAGE = "ai.umos.vehiclecontrol"
APP_ACTIVITY = "ai.umos.vehiclecontrol.VehicleControlActivity"

def get_page_source():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.udid = DEVICE_ID
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.no_reset = True
    options.new_command_timeout = 300

    driver = webdriver.Remote(APPIUM_SERVER_URL, options=options)
    
    try:
        print("Explicitly launching Vehicle Control Activity...")
        try:
            driver.terminate_app(APP_PACKAGE)
        except:
            pass
            
        driver.execute_script('mobile: startActivity', {
            'component': f"{APP_PACKAGE}/{APP_ACTIVITY}"
        })
        
        print("App launched. Waiting 8s for UI to settle...")
        time.sleep(8)
        
        source = driver.page_source
        output_file = os.path.abspath("current_ui_source.xml")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(source)
        print(f"Page source saved to: {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    get_page_source()
