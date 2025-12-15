import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

@pytest.mark.order(4)
def test_ad_scenario(driver):
    """
    Test AD (Autonomous Driving) Screen Scenarios
    """
    vehicle_page = VehicleControlPage(driver)
    
    # 1. Start and Navigate to AD
    vehicle_page.start()
    vehicle_page.click(vehicle_page.MENU_AD)
    time.sleep(2)
    
    # 2. AD Mode: Pro vs Max
    # Check default (Pro might be selected)
    # Click Max
    vehicle_page.click(vehicle_page.AD_MODE_MAX)
    print("Selected AD Mode: Max")
    time.sleep(1)
    # Click Pro
    vehicle_page.click(vehicle_page.AD_MODE_PRO)
    print("Selected AD Mode: Pro")
    time.sleep(1)
    
    # 3. AD Speed: Auto vs Current
    vehicle_page.click(vehicle_page.AD_SPEED_CURRENT)
    print("Selected AD Speed: Current")
    time.sleep(1)
    vehicle_page.click(vehicle_page.AD_SPEED_AUTO)
    print("Selected AD Speed: Auto")
    time.sleep(1)
    
    # 4. Lane Change: Auto vs Confirm
    vehicle_page.click(vehicle_page.AD_LANE_CHANGE_CONFIRM)
    print("Selected Lane Change: Confirm")
    time.sleep(1)
    vehicle_page.click(vehicle_page.AD_LANE_CHANGE_AUTO)
    print("Selected Lane Change: Auto")
    time.sleep(1)

    print("AD Scenario Test Completed")
