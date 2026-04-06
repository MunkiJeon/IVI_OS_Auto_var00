import xml.etree.ElementTree as ET

def find_car_icons(xml_file):
    try:
        with open(xml_file, "r", encoding="utf-8") as f:
            root = ET.fromstring(f.read().encode('utf-8'))
            
        found = []
        for el in root.iter():
            bounds = el.get('bounds')
            clickable = el.get('clickable')
            if bounds and clickable == 'true':
                # Parse bounds [x1,y1][x2,y2]
                coords = bounds.replace('[', '').replace(']', ',').split(',')
                x1 = int(coords[0])
                y1 = int(coords[1])
                x2 = int(coords[2])
                y2 = int(coords[3])
                
                # Car graphic area is generally on the left half (x < 900)
                if x2 < 900:
                    text = el.get('text', '')
                    desc = el.get('content-desc', '')
                    # Center of icon
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2
                    found.append((cy, cx, text, desc, bounds))
        
        # Sort by Y (top to bottom)
        found.sort()
        for cy, cx, txt, d, b in found:
            print(f"Icon at ({cx}, {cy}): Text='{txt}' | Desc='{d}' | Bounds='{b}'")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_car_icons("sidebar_page_1.xml")
