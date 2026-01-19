import xml.etree.ElementTree as ET
import sys

def find_bounds_center(text_to_find, file_path='window_dump.xml'):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        
        for node in root.iter('node'):
            text = node.get('text')
            content_desc = node.get('content-desc')
            
            # Check both text and content-desc
            if (text and text_to_find in text) or (content_desc and text_to_find in content_desc):
                bounds = node.get('bounds')
                if bounds:
                    # bounds format: [x1,y1][x2,y2]
                    coords = bounds.replace('][', ',').replace('[', '').replace(']', '').split(',')
                    x1, y1, x2, y2 = map(int, coords)
                    center_x = (x1 + x2) // 2
                    center_y = (y1 + y2) // 2
                    print(f"FOUND: {text_to_find}")
                    print(f"BOUNDS: {bounds}")
                    print(f"CENTER: {center_x} {center_y}")
                    return center_x, center_y
        print(f"NOT_FOUND: {text_to_find}")
        return None, None
    except Exception as e:
        print(f"ERROR: {e}")
        return None, None

if __name__ == "__main__":
    if len(sys.argv) > 1:
        find_bounds_center(sys.argv[1])
