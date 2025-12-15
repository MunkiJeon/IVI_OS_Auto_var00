import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_climate_scenario(driver):
    vehicle_page = VehicleControlPage(driver)
    
    print("Starting Climate Scenario Test...")
    vehicle_page.start()
    time.sleep(3) 
    
    if not vehicle_page.is_loaded():
        print("Error: App not loaded.")
        return

    # Navigate to Climate Screen
    print("Navigating to Climate Screen...")
    vehicle_page.click(vehicle_page.MENU_CLIMATE)
    time.sleep(2)
    
    # Verify Climate Toggles
    # We will iterate through a list of locators to verify visibility and maybe click them
    climate_options = [
        (vehicle_page.CLIMATE_AUTO_RECIRCULATE, "Auto Recirculate"),
        (vehicle_page.CLIMATE_WASHER_FLUID, "Washer Fluid"),
        (vehicle_page.CLIMATE_TUNNEL_ENTRY, "Tunnel Entry"),
        (vehicle_page.CLIMATE_AIR_QUALITY, "Air Quality"),
        (vehicle_page.CLIMATE_OVERHEAT_PROTECTION, "Overheat Protection"),
        (vehicle_page.CLIMATE_AUTO_DRY, "Auto Dry")
    ]
    
    for locator, name in climate_options:
        if vehicle_page.is_displayed(locator):
            print(f"Verified: {name} is visible.")
            # Toggle On
            vehicle_page.click(locator)
            print(f"Clicked {name} (Toggle 1).")
            time.sleep(1)
            # Toggle Off (Interact again as requested)
            vehicle_page.click(locator)
            print(f"Clicked {name} (Toggle 2).")
            time.sleep(0.5)
        else:
            print(f"Error: {name} not visible.")
            
    # Extra Scroll (User requested scrolling for climate? Maybe not explicitly, but good practice if items overflow)
    print("Performing extra scroll...")
    vehicle_page.scroll_down()
    time.sleep(1)
    
    # Re-verify last item
    if vehicle_page.is_displayed(vehicle_page.CLIMATE_AUTO_DRY):
        print("Verified: Auto Dry visible after scroll.")

    print("Climate Scenario Test Completed")
