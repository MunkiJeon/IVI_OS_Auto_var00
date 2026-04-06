import xml.etree.ElementTree as ET

def find_scrollables(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for el in root.iter():
            cls = el.get('class', '')
            if any(s in cls for s in ['ScrollView', 'ListView', 'RecyclerView', 'ViewGroup']):
                # Some ViewGroups are scrollable even if not explicitly named
                if el.get('scrollable') == 'true':
                    print(f"Scrollable: {cls}, Bounds: {el.get('bounds')}, ID: {el.get('resource-id')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    find_scrollables('ui_dump_clean.xml')
