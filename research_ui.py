import time
import os
from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage

def capture_all_tabs():
    try:
        print("[Research] Starting UI capture for all tabs...")
        d = DriverFactory.get_driver()
        p = VehicleControlPage(d)
        
        # Tabs from the user's request
        tabs = ['빠른 설정', '라이트', 'AD', '주행', '잠금', '시트', '공조', '충전']
        
        for t in tabs:
            print(f"[Research] Navigating to {t}...")
            p.click_sidebar_menu(t)
            time.sleep(3)
            
            # Save screenshot
            filename = f"ui_{t.replace(' ', '_')}.png"
            d.save_screenshot(filename)
            print(f"[Research] Saved {filename}")
            
            # Save page source
            with open(f"ui_{t.replace(' ', '_')}.xml", "w", encoding="utf-8") as f:
                f.write(d.page_source)
            print(f"[Research] Saved {t}.xml")
            
        d.quit()
        print("[Research] Completed UI capture.")
        
    except Exception as e:
        print(f"[Research] Error: {e}")

if __name__ == "__main__":
    capture_all_tabs()
