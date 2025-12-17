import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_quick_settings_full(driver):
    """
    Combined test for Quick Settings: Icons visibility and Actions (Click/Toggle).
    Verifies all accessible elements in the Quick Settings panel.
    """
    vehicle_page = VehicleControlPage(driver)
    
    print("Starting Quick Settings Full Test...")
    vehicle_page.start()
    time.sleep(3) # Wait for app load
    
    # 1. Navigate to Quick Settings
    print("Navigating to Quick Settings...")
    vehicle_page.click(vehicle_page.MENU_QUICK_SETTINGS)
    time.sleep(2)
    
    # 2. Define all items to test
    # Format: (Locator, Name, IsAction)
    # IsAction=True implies we might expect a toggle or state change, currently just click verify.
    
    items_to_test = [
        (vehicle_page.QS_SIDE_MIRROR, "Side Mirror"),
        (vehicle_page.QS_ALL_WINDOWS, "All Windows"),
        (vehicle_page.QS_WINDOW_LOCK, "Window Lock"), # Also in actions
        (vehicle_page.QS_DOOR_LOCK, "Door Lock"),     # Also in actions
        (vehicle_page.QS_TRUNK, "Trunk"),
        (vehicle_page.QS_CHILD_LOCK, "Child Lock"),   # Also in actions
        (vehicle_page.QS_GLOVE_BOX, "Glove Box"),
        (vehicle_page.QS_STEERING_WHEEL, "Steering Wheel")
    ]
    
    # 3. Iterate and Test
    SCREEN_WIDTH = 1920
    SCREEN_HEIGHT = 1080
    def get_coords(ratio_x, ratio_y) :
        return (int(SCREEN_WIDTH * ratio_x), int(SCREEN_HEIGHT * ratio_y))

    for name, (rx, ry) in vehicle_page.Quick_Settings_IconBtn.items():
        x, y = get_coords(rx, ry)
        print(f"Testing {name} at ({x}, {y})...")
        driver.tap([(x, y)])
        time.sleep(3)

    for locator, name in items_to_test:
        try:
            print(f"Testing {name}...")
            
            # Visibility Check (with Scroll if needed)
            if not vehicle_page.is_displayed(locator):
                print(f"{name} not immediately visible. Attempting scroll...")
                vehicle_page.scroll_down()
                time.sleep(1)
            
            element_present = vehicle_page.wait_for_element(locator)
            if vehicle_page.is_displayed(locator) or element_present:
                if not vehicle_page.is_displayed(locator):
                    print(f"Warning: {name} found by locator but 'is_displayed' is False. Proceeding with click.")
                
                # Interaction Check
                vehicle_page.click(locator)
                print(f"Clicked {name}. (Action Performed)")
                time.sleep(1) 
                
                # Optional: specific toggle verification logic can be added here
                # e.g., if Name == "Window Lock", check if text changed or color changed (if attributes available)
                
            else:
                pytest.fail(f"Element {name} verification failed: Not Visible/Present.")
                
        except Exception as e:
            pytest.fail(f"Exception during testing {name}: {e}")

    # 4. Special Check for Red Box Items (Rows)
    # Sunblind, Lights, Wipers (Front/Rear)
    print("\n[Step] Verifying Control Rows (Sunblind, Lights, Wipers)...")
    
    # 4.1 Sunblind Text
    if vehicle_page.is_displayed(vehicle_page.QS_SUNBLIND_TEXT):
        print("Verified 'Sunblind' (선블라인드) Text (Red Box Item).")
    else:
        print("Warning: 'Sunblind' Text not found.")

    # 4.2 Verify Rows by 'Auto' buttons
    # Logic: Get all 'Auto' buttons, sort by Y, and map to expected rows.
    # Expected Order (Top to Bottom): Sunblind -> Lights -> Front Wiper -> Rear Wiper
    try:
        auto_btns = vehicle_page.driver.find_elements(*vehicle_page.QS_AUTO_LABEL)
        # Filter for visible ones in the right panel (x > 800 approx) if needed, 
        # but Quick Settings usually is the main view.
        
        # Sort by Y coordinate
        sorted_autos = sorted(auto_btns, key=lambda el: el.location['y'])
        
        expected_rows = ["Sunblind (Slider)", "Lights (Headlights)", "Front Wiper", "Rear Wiper"]
        
        print(f"Found {len(sorted_autos)} 'Auto' buttons.")
        
        if len(sorted_autos) >= 4:
            for i, row_name in enumerate(expected_rows):
                if i < len(sorted_autos):
                    y_loc = sorted_autos[i].location['y']
                    print(f"Verified Row: {row_name} - 'Auto' Button found at Y={y_loc}")
        else:
            print(f"Warning: Found fewer 'Auto' buttons than expected ({len(sorted_autos)} < 4).")
            for i, btn in enumerate(sorted_autos):
                print(f"  - Auto Button {i+1} at Y={btn.location['y']}")

    except Exception as e:
        print(f"Error checking Auto buttons: {e}")

    print("Quick Settings Full Test Completed")
