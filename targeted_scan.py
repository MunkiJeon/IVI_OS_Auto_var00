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

def targeted_scan():
    try:
        d = DriverFactory.get_driver()
        p = VehicleControlPage(d)
        
        # 1. Reset sidebar to top
        for _ in range(5): d.swipe(800, 200, 800, 800, 400)
        
        # 2. Targeted Menus (Final Set)
        menus = ['연결', '앱', '보안', '개인정보 보호', '하이패스', '일반 설정', '차량 정보']
        
        for menu in menus:
            print(f"\n>>>> TARGETED SCAN: {menu} <<<<")
            
            # Find and click menu in sidebar (scrolling up/down if needed)
            found = False
            for _ in range(15): # Max 15 scrolls for the sidebar
                source = d.page_source
                if menu in source:
                    p.click_sidebar_menu(menu)
                    found = True
                    break
                # Scroll sidebar down
                d.swipe(800, 800, 800, 300, 1000)
                time.sleep(1)
            
            if not found:
                print(f"FAILED TO FIND MENU: {menu}")
                continue
                
            time.sleep(3)
            # 3. Exhaustive Panel Scan
            items = []
            for s in range(6):
                source = d.page_source
                curr = get_clickable_elements(source, 1000)
                new_added = 0
                for it in curr:
                    id_str = f"{it['text']}|{it['desc']}|{it['bounds']}"
                    if id_str not in [f"{x['text']}|{x['desc']}|{x['bounds']}" for x in items]:
                        items.append(it)
                        new_added += 1
                
                print(f"  - Scroll {s}: Discovered {new_added} new elements. Total: {len(items)}")
                if new_added == 0 and s > 0: break
                d.swipe(1500, 850, 1500, 150, 1200)
                time.sleep(2)
            
            # Save report
            with open(f"targeted_scan_{menu}.txt", "w", encoding="utf-8") as f:
                for it in items:
                    f.write(f"Text: {it['text']} | Desc: {it['desc']} | Class: {it['class']} | Bounds: {it['bounds']}\n")
            
            d.save_screenshot(f"targeted_scan_{menu}.png")
            
        d.quit()
        print("TARGETED SCANS COMPLETED.")
        
    except Exception as e:
        print(f"Scan Error: {e}")

if __name__ == "__main__":
    targeted_scan()
