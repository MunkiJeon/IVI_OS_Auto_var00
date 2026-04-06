import time
import os
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

def parse_elements(filename):
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        clickable = []
        for el in root.iter():
            if el.get('clickable') == 'true' or el.get('text'):
                clickable.append({
                    'text': el.get('text'),
                    'bounds': el.get('bounds'),
                    'class': el.get('class'),
                    'resource_id': el.get('resource-id'),
                    'content_desc': el.get('content-desc'),
                    'selected': el.get('selected')
                })
        return clickable
    except:
        return []

def deep_scan():
    try:
        d = DriverFactory.get_driver()
        udid = d.capabilities['udid']
        p = VehicleControlPage(d)
        
        tabs = ['빠른 설정', '라이트', 'AD', '주행', '잠금', '시트', '공조', '충전']
        
        report = []
        
        for t in tabs:
            print(f"--- Scanning Tab: {t} ---")
            p.click_sidebar_menu(t)
            time.sleep(3)
            
            # 1. Initial State
            xml_pre = f"scan_{t}_pre.xml"
            get_xml_dump(xml_pre, udid)
            elements = parse_elements(xml_pre)
            
            # 2. Scroll and Discover
            print(f"[Scan] Scrolling {t} for more elements...")
            # Swipe right-side panel (x: 1000 to 1800)
            d.swipe(1500, 800, 1500, 200, 1000)
            time.sleep(2)
            xml_post_scroll = f"scan_{t}_scrolled.xml"
            get_xml_dump(xml_post_scroll, udid)
            
            # 3. Identify and Log
            report.append({
                'tab': t,
                'initial_elements': elements,
                'scrolled_xml': xml_post_scroll
            })
            
            # Back to top for next tab
            d.swipe(1500, 200, 1500, 800, 1000)
            time.sleep(1)

        d.quit()
        
        # Save discovery report
        with open("ui_discovery_report.txt", "w", encoding="utf-8") as f:
            for r in report:
                f.write(f"Tab: {r['tab']}\n")
                for el in r['initial_elements']:
                    f.write(f"  - {el['text']} {el['bounds']} (ID: {el['resource_id']})\n")
                f.write("\n")
                
    except Exception as e:
        print(f"Deep Scan failed: {e}")

if __name__ == "__main__":
    deep_scan()
