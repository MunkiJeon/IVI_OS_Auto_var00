import sys
import os
sys.path.append(os.getcwd())

from utils.device_manager import DeviceManager
from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage

def verify_connection():
    print("=== Testing Dynamic Connection with Server Check ===")
    udid = DeviceManager.get_target_device()
    if udid:
        print(f"Target UDID found: {udid}")
        is_inst = DeviceManager.is_server_installed(udid)
        print(f"Appium Server installed on {udid}: {is_inst}")
    return udid

if __name__ == "__main__":
    udid = verify_connection()
    if udid:
        print("Connection test passed.")
    else:
        print("Connection test failed (No device found).")
