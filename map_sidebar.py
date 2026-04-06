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

def get_sidebar_items(xml_file):
    sidebar_items = []
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        # Look for elements in the sidebar region (x: 330 to 525 approx)
        for el in root.iter():
            text = el.get('text')
            bounds = el.get('bounds')
            # Only consider elements with text a specific area
            # Format “[x1,y1][x2,y2]”
            if text and bounds:
                # Basic parsing [x1,y1][x2,y2]
                coords = bounds.replace('[', '').replace(']', ',').split(',')
                x1 = int(coords[0])
                # Sidebar is generally on the left side but after the dashboard
                if 250 < x1 < 600:
                    sidebar_items.append(text)
    except:
        pass
    return sidebar_items

def map_sidebar():
    try:
        d = DriverFactory.get_driver()
        udid = d.capabilities['udid']
        
        all_menus = []
        last_menus = []
        
        print("[Discovery] Mapping Sidebar...")
        
        for i in range(10): # Max 10 scrolls for sidebar
            xml_file = f"sidebar_page_{i}.xml"
            get_xml_dump(xml_file, udid)
            current_menus = get_sidebar_items(xml_file)
            
            # Add only new menus
            new_found = False
            for m in current_menus:
                if m not in all_menus:
                    all_menus.append(m)
                    new_found = True
            
            if not new_found and i > 0:
                print("[Discovery] Reached the end of the sidebar.")
                break
                
            # Scroll Sidebar (approx x: 400)
            print(f"[Discovery] Scrolling Sidebar (found {len(all_menus)} items so far)...")
            d.swipe(400, 800, 400, 200, 1000)
            time.sleep(2)
            
        print(f"[Discovery] Full Sidebar Map: {all_menus}")
        
        with open("sidebar_map.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(all_menus))
            
        d.quit()
        
    except Exception as e:
        print(f"Discovery failed: {e}")

if __name__ == "__main__":
    map_sidebar()
