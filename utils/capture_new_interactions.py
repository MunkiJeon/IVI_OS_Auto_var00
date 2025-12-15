import time
import os
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy

# App Config
options = UiAutomator2Options()
options.platform_name = "Android"
options.automation_name = "UiAutomator2"
options.device_name = "emulator-5554" 
options.app_package = "ai.umos.vehiclecontrol"
options.app_activity = "ai.umos.vehiclecontrol.MainActivity"
options.no_reset = True

driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

def save_xml(filename):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print(f"Saved {filename}")

try:
    print("Starting App...")
    time.sleep(5)
    
    # 1. Navigation
    print("Navigating to Navigation...")
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='내비게이션']").click()
    time.sleep(2)
    save_xml("source_navigation.xml")
    
    # 2. Gleo AI
    print("Navigating to Gleo AI...")
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Gleo AI']").click()
    time.sleep(2)
    save_xml("source_gleo_ai.xml")
    
    # 3. Swipe Sidebar Up to reveal more items
    print("Swiping Sidebar Up...")
    # Sidebar is on the left, let's swipe from bottom-left up
    # x ~ 800, y_start ~ 900 -> y_end ~ 200
    driver.swipe(800, 900, 800, 200, 1000)
    time.sleep(2)
    
    # 4. Screen (화면) - Check if visible, might need locators or visual check?
    # Assuming '화면' text appears after swipe or was already there but lower
    try:
        print("Navigating to Screen (화면)...")
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='화면']").click()
        time.sleep(2)
        save_xml("source_screen.xml")
    except:
        print("Could not find '화면' menu.")

    # 5. Sound (사운드)
    try:
        print("Navigating to Sound (사운드)...")
        driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='사운드']").click()
        time.sleep(2)
        save_xml("source_sound.xml")
    except:
        print("Could not find '사운드' menu.")

    # 6. Profile (프로필)
    try:
         print("Navigating to Profile (프로필)...")
         driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='프로필']").click()
         time.sleep(2)
         save_xml("source_profile.xml")
    except:
         print("Could not find '프로필' menu.")

except Exception as e:
    print(f"Error: {e}")

finally:
    driver.quit()
