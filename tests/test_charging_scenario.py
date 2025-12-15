import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_charging_scenario(driver):
    vehicle_page = VehicleControlPage(driver)
    
    print("Starting Charging Scenario Test...")
    vehicle_page.start()
    time.sleep(3) 
    
    if not vehicle_page.is_loaded():
        print("Error: App not loaded.")
        return

    # Navigate to Charging Screen
    print("Navigating to Charging Screen...")
    vehicle_page.click(vehicle_page.MENU_CHARGING)
    time.sleep(2)
    
    # Verify Top Elements
    if vehicle_page.is_displayed(vehicle_page.CHARGING_START):
        print("Verified: Charging Start visible.")
    else:
        print("Error: Charging Start not visible.")
        
    if vehicle_page.is_displayed(vehicle_page.CHARGING_UNLOCK_CONNECTOR):
        print("Verified: Unlock Connector visible.")
        
    # Scroll down
    print("Scrolling down...")
    vehicle_page.scroll_down()
    time.sleep(2)
    
    # Verify Bottom Elements
    if vehicle_page.is_displayed(vehicle_page.CHARGING_SLOW_CHARGING):
        print("Verified: Slow Charging visible.")
        vehicle_page.click(vehicle_page.CHARGING_SLOW_CHARGING) # Interact
    else:
        print("Error: Slow Charging not visible.")

    # Swipe Battery Limit (Red Area) - User Interaction Request
    # Based on XML: 0% at x=1043, 100% at x=1809. Y is around 432 (text), so bar is likely above.
    # We will swipe from ~20% (x=1200) to ~90% (x=1700) at y=350.
    print("Swiping Battery Limit (20% -> 90%)...")
    start_x = 1200
    end_x = 1700
    y_loc = 350 # Estimated based on text at 432
    
    vehicle_page.driver.swipe(start_x, y_loc, end_x, y_loc, 1000)
    time.sleep(2)
    print("Swipe action performed.")
        
    # Extra Scroll
    print("Performing extra scroll...")
    vehicle_page.scroll_down()
    time.sleep(1)

    print("Charging Scenario Test Completed")
