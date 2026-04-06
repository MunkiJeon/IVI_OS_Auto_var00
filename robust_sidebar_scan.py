import time
import subprocess
import xml.etree.ElementTree as ET
from utils.driver_factory import DriverFactory

def get_xml_dump(filename, udid):
    try:
        subprocess.run(["adb", "-s", udid, "shell", "uiautomator", "dump", "/sdcard/ui_temp.xml"], check=True)
        subprocess.run(["adb", "-s", udid, "pull", "/sdcard/ui_temp.xml", filename], check=True)
        return True
    except:
        return False

def get_sidebar_candidates(xml_file):
    candidates = []
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
                y1 = int(coords[1])
                # Sidebar is on the left half (x < 1000)
                # But it's after the dashboard (x > 500)
                # And it's a menu item (not a dashboard stat like 500km)
                if 600 < x1 < 950:
                    candidates.append((y1, txt))
    except Exception as e:
        print(f"Parse error in {xml_file}: {e}")
    
    # Sort by Y position
    candidates.sort()
    return [c[1] for c in candidates]

def discover_sidebar():
    try:
        d = DriverFactory.get_driver()
        udid = d.capabilities['udid']
        
        all_menus = []
        
        # Reset to top
        for _ in range(3):
            d.swipe(800, 200, 800, 800, 400)
            
        print("[Discovery] Scanning Sidebar...")
        
        for i in range(10):
            fname = f"sidebar_full_{i}.xml"
            get_xml_dump(fname, udid)
            current = get_sidebar_candidates(fname)
            
            added = 0
            for m in current:
                if m not in all_menus:
                    all_menus.append(m)
                    added += 1
            
            print(f"Scroll {i}: Found {len(current)} labels, {added} new. Total unique menus: {len(all_menus)}")
            
            if added == 0 and i > 0:
                print("End of sidebar reached.")
                break
                
            # Swipe Sidebar
            d.swipe(800, 850, 800, 150, 1500)
            time.sleep(2)
            
        print(f"DISCOVERED MENUS: {all_menus}")
        
        with open("final_sidebar_list.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(all_menus))
            
        d.quit()
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    discover_sidebar()
