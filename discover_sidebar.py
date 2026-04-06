import time
import subprocess
import xml.etree.ElementTree as ET
from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage

def get_xml_dump(filename, udid):
    try:
        subprocess.run(["adb", "-s", udid, "shell", "uiautomator", "dump", "/sdcard/ui_temp.xml"], check=True)
        subprocess.run(["adb", "-s", udid, "pull", "/sdcard/ui_temp.xml", filename], check=True)
        return True
    except:
        return False

def get_elements_in_range(xml_file, x_min, x_max):
    found_texts = []
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for el in root.iter():
            txt = el.get('text')
            bounds = el.get('bounds')
            if txt and bounds:
                # [x1,y1][x2,y2]
                coords = bounds.replace('[', '').replace(']', ',').split(',')
                x1 = int(coords[0])
                if x_min < x1 < x_max:
                    found_texts.append(txt)
    except:
        pass
    return found_texts

def deep_sidebar_discovery():
    try:
        d = DriverFactory.get_driver()
        udid = d.capabilities['udid']
        
        all_menus = []
        
        # Reset sidebar to top (scroll up multiple times)
        for _ in range(5):
            d.swipe(800, 200, 800, 800, 500)
            
        print("[Discovery] Starting Sidebar Mapping...")
        
        for i in range(15): # Max 15 scrolls
            # Capture
            xml_file = f"sidebar_scan_{i}.xml"
            get_xml_dump(xml_file, udid)
            
            # Sidebar area: x between 650 and 950
            current_menus = get_elements_in_range(xml_file, 650, 950)
            
            new_added = 0
            for m in current_menus:
                if m not in all_menus:
                    all_menus.append(m)
                    new_added += 1
            
            print(f"[Discovery] Scroll {i}: Found {len(current_menus)} elements in range, {new_added} new. Total: {len(all_menus)}")
            
            if new_added == 0 and i > 0:
                print("[Discovery] No new menu items found. Reached end of sidebar.")
                break
                
            # Scroll sidebar down
            # Using Center of sidebar roughly [800, 500]
            d.swipe(820, 850, 820, 150, 1200) # Long slow swipe
            time.sleep(2)
            
        print(f"[Discovery] FINAL SIDEBAR MAP: {all_menus}")
        
        with open("master_sidebar_map.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(all_menus))
            
        d.quit()
        
    except Exception as e:
        print(f"Discovery failed: {e}")

if __name__ == "__main__":
    deep_sidebar_discovery()
