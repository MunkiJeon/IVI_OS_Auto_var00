import time
import os
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
                if x_min < x1 < x_max:
                    found.append({'text': txt, 'bounds': bounds, 'clickable': el.get('clickable') == 'true'})
    except: pass
    return found

def run_deep_discovery():
    try:
        d = DriverFactory.get_driver()
        p = VehicleControlPage(d)
        menus = ['빠른 설정', '라이트', 'AD', '주행', '잠금', '시트', '공조', '충전', '내비게이션', '스케줄', '하이패스', '편의', '개인정보 보호', '보안', '차량 정보']
        
        for menu in menus:
            print(f">>> SCANNING {menu} <<<")
            p.click_sidebar_menu(menu)
            time.sleep(3)
            
            panel_items = []
            for s in range(5): # Up to 5 scrolls per menu
                source = d.page_source
                curr = get_elements_from_source(source, 1000, 1920)
                new_added = 0
                for el in curr:
                    if el['text'] not in [it['text'] for it in panel_items]:
                        panel_items.append(el)
                        new_added += 1
                if new_added == 0 and s > 0: break
                d.swipe(1500, 800, 1500, 200, 1000)
                time.sleep(2)
            
            # Save individual inventory
            fname = f"inventory_{menu}.txt"
            with open(fname, "w", encoding="utf-8") as f:
                for item in panel_items:
                    f.write(f"{item['text']} {item['bounds']} (clickable:{item['clickable']})\n")
            
            print(f"  - Saved {len(panel_items)} items to {fname}")
            d.save_screenshot(f"capture_{menu}.png")
            
        d.quit()
        print("COMPREHENSIVE DISCOVERY FINISHED.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_deep_discovery()
