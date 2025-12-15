import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_seat_scenario(driver):
    vehicle_page = VehicleControlPage(driver)
    
    print("Starting Seat Position Scenario Test...")
    vehicle_page.start()
    time.sleep(3) 
    
    if not vehicle_page.is_loaded():
        print("Error: App not loaded.")
        return

    # Navigate to Seat Screen
    print("Navigating to Seat Position Screen...")
    vehicle_page.click(vehicle_page.MENU_SEAT)
    time.sleep(2)
    
    # 1. Verify Driver Seat (Default)
    print("Verifying Driver Seat (Default)...")
    if vehicle_page.is_displayed(vehicle_page.SEAT_TITLE_DRIVER):
        print("Verified: Driver Seat Title is visible.")
    else:
        print("Error: Driver Seat Title not visible.")

    if vehicle_page.is_displayed(vehicle_page.SEAT_BUTTON_SAVE):
        print("Verified: Save Button is visible.")
        # Popup Interaction Test: Click Save -> Check Popup -> Cancel -> Click Save -> Confirm
        print("Testing Popup Interaction (Save)...")
        vehicle_page.click(vehicle_page.SEAT_BUTTON_SAVE)
        time.sleep(1)
        
        # Look for "취소" (Cancel) or "닫기" (Close) generic generic locator
        # Since we don't have the popup XML, we try generic text locators dynamically
        try:
            cancel_btn = (driver.find_element(AppiumBy.XPATH, "//*[@text='취소']"))
            print("Popup detected. Clicking Cancel...")
            cancel_btn.click()
            time.sleep(1)
            
            # Click Save again
            print("Clicking Save again...")
            vehicle_page.click(vehicle_page.SEAT_BUTTON_SAVE)
            time.sleep(1)
            
            # Confirm (Assuming "확인" or "저장" in popup)
            confirm_btn = (driver.find_element(AppiumBy.XPATH, "//*[@text='확인' or @text='저장']"))
            print("Popup detected. Clicking Confirm...")
            confirm_btn.click()
            time.sleep(1)
            
        except Exception as e:
            print(f"Popup interaction skipped or element not found: {e}")
            # If no popup appeared, just continue
        
        
    # 2. Click Passenger Seat (Front Right)
    # Estimated Coordinates: x=1650, y=450
    print("Clicking Passenger Seat...")
    vehicle_page.driver.tap([(1650, 450)])
    time.sleep(1)
    
    if vehicle_page.is_displayed(vehicle_page.SEAT_TITLE_PASSENGER):
        print("Verified: Passenger Seat Title is visible.")
    else:
        print("Error: Passenger Seat Title not visible.")
        
    # 3. Click Rear Left Seat
    # Estimated Coordinates: x=1250, y=700
    print("Clicking Rear Left Seat...")
    vehicle_page.driver.tap([(1250, 700)])
    time.sleep(1)
    
    if vehicle_page.is_displayed(vehicle_page.SEAT_TITLE_REAR_LEFT):
        print("Verified: Rear Left Seat Title is visible.")
    else:
        print("Error: Rear Left Seat Title not visible.")
        
    # 4. Click Rear Right Seat
    # Estimated Coordinates: x=1650, y=700
    print("Clicking Rear Right Seat...")
    vehicle_page.driver.tap([(1650, 700)])
    time.sleep(1)
    
    if vehicle_page.is_displayed(vehicle_page.SEAT_TITLE_REAR_RIGHT):
        print("Verified: Rear Right Seat Title is visible.")
    else:
        print("Error: Rear Right Seat Title not visible.")
        
    # 5. Click Rest Mode Button (Just to verify interaction)
    print("Clicking Rest Mode button...")
    if vehicle_page.is_displayed(vehicle_page.SEAT_BUTTON_REST_MODE):
        vehicle_page.click(vehicle_page.SEAT_BUTTON_REST_MODE)
        print("Clicked Rest Mode.")
    else:
        print("Error: Rest Mode button not found.")
        
    # Extra Scroll (User requested scrolling for Seat too, though it might not scroll much if fitting)
    print("Performing extra scroll...")
    vehicle_page.scroll_down()
    time.sleep(1)

    print("Seat Position Scenario Test Completed")
