import xml.etree.ElementTree as ET

root = ET.parse('lights_bottom_test.xml').getroot()
with open('parsed_lights.txt', 'w', encoding='utf-8') as f:
    for elem in root.iter():
        if elem.get('text') in ['무드 조명', '사운드 연동 조명', '항상 켜기', '주차시', '끄기', '켜기', '자동', '색상']:
            f.write(elem.get('text') + ': ' + str(elem.get('bounds')) + '\n')

root2 = ET.parse('lights_color_popup.xml').getroot()
with open('parsed_popup.txt', 'w', encoding='utf-8') as f:
    for elem in root2.iter():
        if elem.get('text') or 'Button' in elem.get('class'):
            f.write(elem.get('class') + ' | ' + elem.get('text', '') + ' | ' + str(elem.get('bounds')) + '\n')
