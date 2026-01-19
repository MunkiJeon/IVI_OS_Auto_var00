import os
import time
import subprocess
import xml.etree.ElementTree as ET

ADB_CMD = "adb -s 192.168.0.183:5555"

def run_adb(cmd):
    return subprocess.check_output(f"{ADB_CMD} {cmd}", shell=True).decode('utf-8')

def dump_ui():
    try:
        run_adb("shell uiautomator dump /sdcard/window_dump.xml")
        run_adb("pull /sdcard/window_dump.xml .")
        return True
    except Exception as e:
        print(f"Dump failed: {e}")
        return False

def find_center(text_to_find, file_path='window_dump.xml'):
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        for node in root.iter('node'):
            text = node.get('text') or ""
            desc = node.get('content-desc') or ""
            if text_to_find in text or text_to_find in desc:
                bounds = node.get('bounds')
                if bounds:
                    coords = bounds.replace('][', ',').replace('[', '').replace(']', '').split(',')
                    x1, y1, x2, y2 = map(int, coords)
                    return (x1 + x2) // 2, (y1 + y2) // 2
    except:
        pass
    return None

def tap(x, y):
    print(f"Tapping {x}, {y}")
    run_adb(f"shell input tap {x} {y}")

steps = [
    {"target": "시작하기", "action": "tap", "next_wait": "닫기"},
    {"target": "닫기", "action": "tap", "next_wait": "나중에 하기"},
    {"target": "나중에 하기", "action": "tap", "next_wait": "발급받기"},
    {"target": "발급받기", "action": "tap", "next_wait": "닫기"},
    {"target": "닫기", "action": "tap", "next_wait": "나중에 하기"},
    {"target": "나중에 하기", "action": "tap", "next_wait": "건너뛰기"},
    {"target": "건너뛰기", "action": "tap", "next_wait": None}
]

def run_flow():
    current_step_idx = 0
    max_retries = 10
    
    while current_step_idx < len(steps):
        step = steps[current_step_idx]
        target = step["target"]
        print(f"\nSearching for: {target}")
        
        found = False
        for i in range(max_retries):
            dump_ui()
            center = find_center(target)
            
            if center:
                print(f"Found {target} at {center}")
                tap(*center)
                found = True
                time.sleep(3) # Wait for transition
                break
            else:
                print(f"Not found {target}, retrying {i+1}/{max_retries}...")
                time.sleep(2)
        
        if found:
            current_step_idx += 1
        else:
            # Special handling: if we lost track, maybe we are already at the next screen?
            # Or maybe the tap didn't work.
            # But for now, let's just retry looking for the SAME target infinitely? 
            # Or assume we might need to check the NEXT target?
            # For simplicity, if we fail to find the target after retries, we stop.
            print(f"Failed to find {target} after retries. Stopping.")
            return

    print("Flow completed successfully!")

if __name__ == "__main__":
    run_flow()
