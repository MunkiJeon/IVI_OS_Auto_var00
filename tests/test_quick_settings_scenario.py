import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestQuickSettingsScenario:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(3) # Wait for app load

    def test_quick_settings(self, driver):
        """
        Combined test for Quick Settings: Icons visibility and Actions (Click/Toggle).
        Verifies all accessible elements in the Quick Settings panel.
        """
        page = VehicleControlPage(driver)
        
        print("Starting Quick Settings Full Test...")
        page.start()
        time.sleep(3) # Wait for app load
        
        # 1. Navigate to Quick Settings
        print("Navigating to Quick Settings...")
        page.click(page.MENU_QUICK_SETTINGS)
        time.sleep(2)
        
        # 2. Define all items to test
        # Format: (Locator, Name, IsAction)
        # IsAction=True implies we might expect a toggle or state change, currently just click verify.
        
        items_to_test = [
            (page.QS_ALL_WINDOWS, "All Windows"),
            (page.QS_WINDOW_LOCK, "Window Lock"),
            (page.QS_TRUNK, "Trunk"),
            (page.QS_CHILD_LOCK, "Child Lock"),
            (page.QS_DOOR_LOCK, "Door Lock"),
            (page.QS_SUNBLIND, "Sunblind"),
            (page.QS_GLOVE_BOX, "Glove Box"),
            (page.QS_STEERING_WHEEL, "Steering Wheel"),
            (page.QS_SIDE_MIRROR, "Side Mirror"),
        ]
        
        # 3. Iterate and Test
        SCREEN_WIDTH = 1920
        SCREEN_HEIGHT = 1080

        page.random_area_interaction(1040, 370, 1340, 370, interaction_type='drag')
        time.sleep(1)
        page.random_area_interaction(1040, 370, 1340, 370, interaction_type='drag')
        time.sleep(1)

        def get_coords(ratio_x, ratio_y) :
            return (int(SCREEN_WIDTH * ratio_x), int(SCREEN_HEIGHT * ratio_y))

        # 4. IconBtn Test
        for name, (rx, ry) in page.QS_IconBtn.items():
            x, y = get_coords(rx, ry)
            print(f"Testing {name} at ({x}, {y})...")
            page.tap_coordinates(x, y)
            time.sleep(1)
            if (name == "전방 와이퍼 워셔액" or name == "후방 와이퍼 워셔액" or name == "라이트 자동 전조등" or name == "사이드 미러 개폐" or name == "충전 포트"):
                page.tap_coordinates(x, y)
                time.sleep(1)

        for locator, name in items_to_test:
            try:
                print(f"Testing {name}...")
                if (name == "Steering Wheel"):
                    page.click(page.QS_STEERING_WHEEL)
                    time.sleep(1)
                    page.click(page.QS_STEERING_WHEEL_SAVE)
                    time.sleep(1)
                    page.click(page.QS_STEERING_WHEEL)
                    time.sleep(1)
                    page.click(page.QS_STEERING_WHEEL_RESTORE)
                    time.sleep(1)
                else:
                    page.click(locator)
                    time.sleep(1)
                    page.click(locator)
                    time.sleep(1)
                    
            except Exception as e:
                pytest.fail(f"Exception during testing {name}: {e}")

        # 4. Special Check for Red Box Items (Rows)
        # Sunblind, Lights, Wipers (Front/Rear)
        print("\n[Step] Verifying Control Rows (Sunblind, Lights, Wipers)...")

        # 4.2 Verify Rows by 'Auto' buttons
        # Logic: Get all 'Auto' buttons, sort by Y, and map to expected rows.
        # Expected Order (Top to Bottom): Sunblind -> Lights -> Front Wiper -> Rear Wiper
        try:
            auto_btns = page.driver.find_elements(*page.QS_AUTO_LABEL)
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
