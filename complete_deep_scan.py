import time
import xml.etree.ElementTree as ET
from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage

def get_clickable_elements(source, x_min=500):
    found = []
    try:
        root = ET.fromstring(source.encode('utf-8'))
        for el in root.iter():
            bounds = el.get('bounds')
            if el.get('clickable') == 'true' and bounds:
                coords = bounds.replace('[', '').replace(']', ',').split(',')
                x1 = int(coords[0])
                if x1 > x_min:
                    found.append({
                        'text': el.get('text', ''),
                        'bounds': bounds,
                        'desc': el.get('content-desc', ''),
                        'class': el.get('class', '')
                    })
    except: pass
    return found

def finish_discovery():
    try:
        d = DriverFactory.get_driver()
        p = VehicleControlPage(d)
        
        # Remaining 5 menus
        menus = ['하이패스', '편의', '개인정보 보호', '보안', '차량 정보']
        
        for menu in menus:
            print(f">>> FINAL SCAN: {menu} <<<")
            p.click_sidebar_menu(menu)
            time.sleep(3)
            
            p_items = []
            for s in range(5):
                source = d.page_source
                curr = get_clickable_elements(source)
                new_c = 0
                for el in curr:
                    id_str = f"{el['text']}|{el['desc']}|{el['bounds']}"
                    if id_str not in [f"{i['text']}|{i['desc']}|{i['bounds']}" for i in p_items]:
                        p_items.append(el)
                        new_c += 1
                if new_c == 0 and s > 0: break
                d.swipe(1500, 800, 1500, 200, 1000)
                time.sleep(2)
            
            # Save results
            with open(f"final_inventory_{menu}.txt", "w", encoding="utf-8") as f:
                for it in p_items:
                    f.write(f"Item: {it['text']} | Desc: {it['desc']} | Class: {it['class']} | Bounds: {it['bounds']}\n")
            
            print(f"  - Captured {len(p_items)} clickable items.")
            d.save_screenshot(f"final_capture_{menu}.png")
            
        d.quit()
        print("ALL RESEARCH DATA CAPTURED successfully.")
        
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    finish_discovery()
