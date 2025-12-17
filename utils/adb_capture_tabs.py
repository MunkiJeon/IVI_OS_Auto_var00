import subprocess
import time
import os

DEVICE_ID = "192.168.0.111:5555"
PACKAGE = "ai.umos.vehiclecontrol"
ACTIVITY = "ai.umos.vehiclecontrol.VehicleControlActivity"

# Coordinates
MENU_X = 760
CONTENT_CENTER_X = 1400 # Right panel center approx
CONTENT_CENTER_Y = 600

# Page 1 Items
# Quick Settings: 123
# ...
# GleoAI: 915
# Screen: 1003 (Estimated)
PAGE_1_ITEMS = [
    ("QuickSettings", 123),
    ("Lights", 211),
    ("AD", 299),
    ("Driving", 387),
    ("Lock", 475),
    ("Seat", 563),
    ("Climate", 651),
    ("Charging", 739),
    ("Navigation", 827),
    ("GleoAI", 915),
    ("Screen", 1003), 
]

# Page 2 Items
PAGE_2_ITEMS = [
    ("Sound", 129),
    ("Profile", 217),
    ("Convenience", 305),
    ("Connection", 393),
    ("Apps", 481),
    ("Security", 569),
    ("Privacy", 657),
    ("Hipass", 745),
    ("General", 833),
    ("VehicleInfo", 921),
]

# Scroll Config
SCROLL_COUNTS = {
    "Apps": 3,
    "Sound": 3,
    "Screen": 2, # Just in case
    "default": 2
}

def adb_command(cmd):
    full_cmd = f"adb -s {DEVICE_ID} {cmd}"
    subprocess.run(full_cmd, shell=True)

def capture(filename):
    local_dir = "captured_xmls"
    os.makedirs(local_dir, exist_ok=True)
    remote_path = f"/data/local/tmp/{filename}"
    local_path = os.path.join(local_dir, filename)
    
    # Dump
    adb_command(f"shell rm {remote_path}")
    adb_command(f"shell uiautomator dump {remote_path}")
    # Pull
    adb_command(f"pull {remote_path} \"{local_path}\"")
    
    if os.path.exists(local_path) and os.path.getsize(local_path) > 0:
        print(f"[OK] Saved {filename}")
    else:
        print(f"[FAIL] Missing {filename}")

def capture_tab_content(tab_name):
    # Determine scroll count
    count = SCROLL_COUNTS.get(tab_name, SCROLL_COUNTS["default"])
    
    # 1. Capture Top
    print(f"  > Capturing {tab_name} (Top)...")
    capture(f"source_{tab_name}_top.xml")
    
    # 2. Scrolls
    for i in range(count):
        print(f"  > Swiping Content ({i+1}/{count})...")
        # Swipe from bottom of right panel to top
        adb_command(f"shell input swipe {CONTENT_CENTER_X} 900 {CONTENT_CENTER_X} 200 800")
        time.sleep(1.5)
        
        print(f"  > Capturing {tab_name} (Scrolled {i+1})...")
        capture(f"source_{tab_name}_scrolled_{i+1}.xml")

def main():
    print("Starting Robust ADB Capture Sequence (Multi-Scroll)...")
    
    # 1. Launch App
    print("Launching specific activity...")
    adb_command(f"shell am start -n {PACKAGE}/{ACTIVITY}")
    time.sleep(5)
    
    # 2. Reset Sidebar (Multiple Swipes Down)
    print("Resetting sidebar (Ensuring Top)...")
    for _ in range(3):
        adb_command("shell input swipe 760 300 760 900 300")
        time.sleep(1)
    time.sleep(1)
    
    # 3. Capture Page 1
    for name, y in PAGE_1_ITEMS:
        print(f"Processing Tab: {name}")
        adb_command(f"shell input tap {MENU_X} {y}")
        time.sleep(2) 
        capture_tab_content(name)
        
    # 4. robust Sidebar Scroll (Multiple Swipes Up)
    print("Swiping Sidebar Up (Ensuring Bottom)...")
    # Swipe from bottom area to top area multiple times to hit end of list
    for _ in range(3):
        adb_command("shell input swipe 760 900 760 100 800")
        time.sleep(1)
    time.sleep(2)
    
    # 5. Capture Page 2
    for name, y in PAGE_2_ITEMS:
        print(f"Processing Tab: {name}")
        adb_command(f"shell input tap {MENU_X} {y}")
        time.sleep(2)
        capture_tab_content(name)
        
    print("All captures completed.")

if __name__ == "__main__":
    main()
