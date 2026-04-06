import xml.etree.ElementTree as ET

def dump_labels(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        results = []
        for el in root.iter():
            txt = el.get('text')
            if txt:
                results.append(f"'{txt}' {el.get('bounds')}")
        return results
    except:
        return []

if __name__ == "__main__":
    import sys
    fname = sys.argv[1] if len(sys.argv) > 1 else 'ui_dump_clean.xml'
    labels = dump_labels(fname)
    print("\n".join(labels))
