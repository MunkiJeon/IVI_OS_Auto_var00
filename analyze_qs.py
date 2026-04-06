import xml.etree.ElementTree as ET

def analyze_all_clickable(xml_file):
    try:
        with open(xml_file, "r", encoding="utf-8") as f:
            root = ET.fromstring(f.read().encode("utf-8"))
            
        print("--- Clickable Elements ---")
        for el in root.iter():
            clickable = el.get('clickable')
            if clickable == 'true':
                txt = el.get('text', '')
                desc = el.get('content-desc', '')
                bounds = el.get('bounds', '')
                print(f"[{el.get('index')}] | Text: '{txt}' | Desc: '{desc}' | Class: {el.get('class')} | Bounds: {bounds}")
                
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    analyze_all_clickable("quick_settings_dump.xml")
