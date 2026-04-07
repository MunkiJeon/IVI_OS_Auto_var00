import xml.etree.ElementTree as ET
import glob

for f in ["lights_page1.xml", "lights_page2.xml", "lights_page3.xml"]:
    try:
        tree = ET.parse(f)
        root = tree.getroot()
        print(f"--- {f} ---")
        for elem in root.iter():
            text = elem.get('text', '')
            if text in ['끄기', '켜기', '자동', '미등', '전조등', '프렁크등', '트렁크등', '에스코트 조명', '운전석', '동승석', '모든 좌석', '뒷좌석 좌측', '뒷좌석 우측', '실내등']:
                bounds = elem.get('bounds')
                print(f"{text}: {bounds}")
    except Exception as e:
        print(f"Error {f}: {e}")
