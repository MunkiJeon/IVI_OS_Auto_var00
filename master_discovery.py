import time
import xml.etree.ElementTree as ET
from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage

def get_elements_from_source(source, x_min, x_max):
    found = []
    try:
        root = ET.fromstring(source.encode('utf-8'))
        for el in root.iter():
            txt = el.get('text')
            bounds = el.get('bounds')
            if txt and bounds:
                coords = bounds.replace('[', '').replace(']', ',').split(',')
                x1 = int(coords[0])
                y1 = int(coords[1])
                if x_min < x1 < x_max:
                    found.append((y1, txt, bounds))
    except:
        pass
    found.sort()
    return found

def master_discovery():
    try:
        d = DriverFactory.get_driver()
        p = VehicleControlPage(d)
        
        # 1. SIDEBAR INVENTORY
        print("[Discovery] Step 1: Mapping Sidebar...")
        all_sidebar_menus = []
        for _ in range(3): d.swipe(800, 200, 800, 800, 400) # Reset sidebar
        
        for i in range(10):
            source = d.page_source
            current = get_elements_from_source(source, 650, 950)
            new_added = 0
            for y, txt, b in current:
                if txt not in [m['text'] for m in all_sidebar_menus]:
                    all_sidebar_menus.append({'text': txt, 'bounds': b})
                    new_added += 1
            if new_added == 0 and i > 0: break
            d.swipe(820, 850, 820, 150, 1200)
            time.sleep(2)
            
        print(f"[Discovery] Sidebar Map ({len(all_sidebar_menus)} items): {[m['text'] for m in all_sidebar_menus]}")
        
        # 2. DETAIL PANEL INVENTORY
        results = {}
        for menu in all_sidebar_menus:
            menu_text = menu['text']
            print(f"\n--- Entering Menu: {menu_text} ---")
            p.click_sidebar_menu(menu_text)
            time.sleep(3)
            
            panel_items = []
            # Scan Right Panel with multiple scrolls
            for j in range(5):
                source = d.page_source
                # Panel is generally x > 1000
                current_panel = get_elements_from_source(source, 1000, 1920)
                new_p = 0
                for y, txt, b in current_panel:
                    if txt not in [item['text'] for item in panel_items]:
                        panel_items.append({'text': txt, 'bounds': b})
                        new_p += 1
                if new_p == 0 and j > 0: break
                d.swipe(1500, 850, 1500, 150, 1200)
                time.sleep(2)
            
            # 3. INTERACTIVE PROBE (Quick for now)
            # Click some icons in the car graphic area [516, 1000]
            print(f"[Discovery] Probing interactive items in {menu_text}...")
            # (In a real run, we'd click everything, but for discovery we capture one state change)
            
            results[menu_text] = panel_items
            d.save_screenshot(f"scan_{menu_text}.png")
            
        # Final Summary
        with open("ui_comprehensive_map.txt", "w", encoding="utf-8") as f:
            for k, items in results.items():
                f.writelines([f"MENU: {k}\n"] + [f"  - {i['text']} {i['bounds']}\n" for i in items] + ["\n"])
                
        d.quit()
        print("[Discovery] COMPLETED.")
        
    except Exception as e:
        print(f"Discovery Error: {e}")

if __name__ == "__main__":
    master_discovery()
