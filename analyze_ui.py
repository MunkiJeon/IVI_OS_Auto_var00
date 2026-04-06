import xml.etree.ElementTree as ET

def analyze_ui(xml_file):
    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()
        clickable_elements = []
        
        for el in root.iter():
            if el.get('clickable') == 'true' or el.get('text'):
                clickable_elements.append({
                    'text': el.get('text'),
                    'bounds': el.get('bounds'),
                    'content_desc': el.get('content-desc'),
                    'resource_id': el.get('resource-id'),
                    'class': el.get('class')
                })
        
        for i, ce in enumerate(clickable_elements):
            text_str = ce['text'] if ce['text'] else f"[{ce['content_desc'] or ce['class']}]"
            print(f"{i}: {text_str} {ce['bounds']} (ID: {ce['resource_id']})")
            
    except Exception as e:
        print(f"Error analyzing UI: {e}")

if __name__ == "__main__":
    analyze_ui('ui_dump.xml')
