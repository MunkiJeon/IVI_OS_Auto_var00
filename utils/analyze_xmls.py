import os
import glob
import re

def parse_texts(xml_file):
    with open(xml_file, 'r', encoding='utf-8') as f:
        content = f.read()
    # Extract text attributes
    texts = re.findall(r'text="([^"]+)"', content)
    return [t for t in texts if t]

def analyze_all():
    files = glob.glob("captured_xmls/*.xml")
    data = {}
    
    # Filter for scrolled/unique content
    # We want to map Tab -> Texts found in Right Panel
    
    for f in files:
        basename = os.path.basename(f)
        # e.g. source_Apps_scrolled_3.xml -> Tab: Apps
        parts = basename.split('_')
        if len(parts) >= 2:
            tab = parts[1] # Apps, Sound, etc.
            if tab not in data:
                data[tab] = set()
            
            texts = parse_texts(f)
            # Filter out Left Menu items if possible (hard without bounds)
            # But we can list them and pick relevant ones.
            # Common menu items to ignore:
            ignore = ["빠른 설정", "라이트", "AD", "주행", "잠금", "시트 포지션", "공조", "충전", "내비게이션", "Gleo AI", "사운드", "프로필", "편의 기능", "연결", "앱", "보안", "개인정보 보호", "하이패스", "일반 설정", "차량 정보", "화면"]
            
            for t in texts:
                if t not in ignore and len(t) > 1:
                    data[tab].add(t)

    # Write results to file
    with open("analysis_report.txt", "w", encoding="utf-8") as f:
        for tab, texts in sorted(data.items()):
            f.write(f"\n--- {tab} ---\n")
            for t in sorted(texts):
                f.write(f"  {t}\n")
    print("Analysis saved to analysis_report.txt")

if __name__ == "__main__":
    analyze_all()
