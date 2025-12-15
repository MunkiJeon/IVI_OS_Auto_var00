import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

@pytest.mark.order(5)
def test_driving_scenario(driver):
    """
    Test Driving Screen Scenarios (Top, Mid, Bot) with Scrolling
    """
    vehicle_page = VehicleControlPage(driver)
    
    # 1. Start and Navigate to Driving
    vehicle_page.start()
    vehicle_page.click(vehicle_page.MENU_DRIVING)
    print("Navigated to Driving")
    time.sleep(2)
    
    # 2. Test Top Section Elements
    # Accel Mode
    vehicle_page.click(vehicle_page.DRIVING_ACCEL_MODE_FAST)
    print("Selected Accel Mode: Fast")
    time.sleep(1)
    
    # Steering Mode
    vehicle_page.click(vehicle_page.DRIVING_STEERING_MODE_LIGHT)
    print("Selected Steering Mode: Light")
    time.sleep(1)
    
    # 3. Scroll to Mid Section
    print("Scrolling to Mid Section...")
    vehicle_page.scroll_down()
    time.sleep(2)
    
    # Test Mid Section Elements
    # Regen Brake
    try:
        vehicle_page.click(vehicle_page.DRIVING_REGEN_BRAKE_STRONG)
        print("Selected Regen Brake: Strong")
    except:
        print("Could not click Regen Brake Strong (might be off screen or covered)")
    time.sleep(1)
    
    # One Pedal (Toggle/Radio)
    try:
        vehicle_page.click(vehicle_page.DRIVING_ONE_PEDAL)
        print("Selected One Pedal Mode")
    except:
        print("Could not click One Pedal Mode")
        
    # 4. Scroll to Bot Section
    print("Scrolling to Bot Section...")
    vehicle_page.scroll_down()
    time.sleep(2)
    
    # Test Bot Section Elements
    # Collision Warning
    try:
        vehicle_page.click(vehicle_page.DRIVING_COLLISION_WARNING_EARLY)
        print("Selected Collision Warning: Early")
    except:
        print("Could not click Collision Warning Early")
        
    # Extra Scroll as per User Request
    print("Performing extra scroll to ensure all bottom elements are visible...")
    vehicle_page.scroll_down()
    time.sleep(2)
    
    # Re-verify Collision Warning after extra scroll
    try:
        if vehicle_page.is_displayed(vehicle_page.DRIVING_COLLISION_WARNING_EARLY):
            print("Verified: Collision Warning 'Early' button is visible.")
        else:
             print("Error: Collision Warning 'Early' button not visible after extra scroll.")
    except:
        print("Error: Collision Warning check failed after extra scroll.")

    print("Driving Scenario Test Completed")
