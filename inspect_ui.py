import xml.etree.ElementTree as ET

def inspect(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        for el in root.iter():
            txt = el.get('text')
            if txt:
                print(f"'{txt}' {el.get('bounds')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    inspect('ui_dump_clean.xml')
