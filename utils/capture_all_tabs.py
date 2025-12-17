from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import subprocess

# Configuration
APPIUM_SERVER_URL = "http://127.0.0.1:4723"
DEVICE_ID = "192.168.0.111:5555"
APP_PACKAGE = "ai.umos.vehiclecontrol"
APP_ACTIVITY = "ai.umos.vehiclecontrol.VehicleControlActivity"

# List of tabs to check in order
# (Menu Text, File Name Suffix)
TABS_TO_CHECK = [
    ("라이트", "lights"),
    ("AD", "ad"),
    ("주행", "driving"),
    ("잠금", "lock"),
    ("시트 포지션", "seat"),
    ("공조", "climate"),
    ("충전", "charging"),
    ("내비게이션", "navigation"),
    ("Gleo AI", "gleo_ai"),
    ("화면", "screen"),
    ("사운드", "sound"),
    ("프로필", "profile"),
    ("편의 기능", "convenience"),
    ("연결", "connection"),
    ("앱", "apps"),
    ("보안", "security"),
    ("개인정보 보호", "privacy"),
    ("하이패스", "hipass"),
    ("일반 설정", "general"),
    ("차량 정보", "vehicle_info"),
]

def capture_tabs():
    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.udid = DEVICE_ID
    options.app_package = APP_PACKAGE
    options.app_activity = APP_ACTIVITY
    options.no_reset = True
    options.new_command_timeout = 600
    
    # Stability settings
    options.set_capability("settings[allowInvisibleElements]", True)
    options.set_capability("settings[ignoreUnimportantViews]", False)

    print("Connecting to driver...")
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
        time.sleep(8)
        
        # Reset sidebar to top
        print("Resetting sidebar...")
        # Swipe down multiple times
        for _ in range(3):
            driver.swipe(816, 300, 816, 800, 500)
            time.sleep(1)

        wait = WebDriverWait(driver, 5)

        for menu_text, file_suffix in TABS_TO_CHECK:
            print(f"\n--- Processing: {menu_text} ---")
            
            # Find and Click Logic with Scrolling
            clicked = False
            for attempt in range(5): # Max 5 scrolls
                try:
                    # Try to find element
                    el = driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[@text='{menu_text}']")
                    # Check visibility if possible, or just click
                    # driver.find_element is enough if it exists
                    print(f"Found {menu_text}. Clicking...")
                    el.click()
                    clicked = True
                    break
                except Exception:
                    print(f"{menu_text} not found/visible. Scrolling (Swipe Up)...")
                    driver.swipe(816, 800, 816, 300, 1000)
                    time.sleep(1.5)
            
            if not clicked:
                print(f"Failed to find/click '{menu_text}'. Skipping capture.")
                continue
                
            # Wait for content load
            time.sleep(3)
            
            # Capture using ADB (reliable)
            filename = f"source_{file_suffix}.xml"
            remote_path = f"/data/local/tmp/{filename}"
            local_path = os.path.abspath(f"captured_xmls/{filename}")
            
            # Create local dir
            os.makedirs("captured_xmls", exist_ok=True)
            
            print(f"Capturing dump for {menu_text}...")
            # Cleanup old
            subprocess.run(f"adb -s {DEVICE_ID} shell rm {remote_path}", shell=True)
            
            # Dump
            subprocess.run(f"adb -s {DEVICE_ID} shell uiautomator dump {remote_path}", shell=True)
            
            # Verify existence
            check = subprocess.run(f"adb -s {DEVICE_ID} shell ls {remote_path}", shell=True, capture_output=True, text=True)
            if "No such file" in check.stderr or "No such file" in check.stdout:
                print(f"Dump failed for {menu_text}. Retrying...")
                time.sleep(2)
                subprocess.run(f"adb -s {DEVICE_ID} shell uiautomator dump {remote_path}", shell=True)
            
            # Pull
            print(f"Pulling to {local_path}...")
            subprocess.run(f"adb -s {DEVICE_ID} pull {remote_path} \"{local_path}\"", shell=True)
            
            if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
                print(f"Successfully saved: {local_path}")
            else:
                print(f"Failed to save local file for {menu_text}")

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    capture_tabs()
