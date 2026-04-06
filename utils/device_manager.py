import subprocess
import time
import re
from config import DeviceConfig

class DeviceManager:
    @staticmethod
    def get_connected_devices():
        """Returns a list of currently connected device IDs."""
        try:
            output = subprocess.check_output(["adb", "devices"]).decode("utf-8")
            devices = []
            for line in output.splitlines():
                if "\tdevice" in line:
                    devices.append(line.split("\t")[0])
            return devices
        except Exception as e:
            print(f"[DeviceManager] Error running adb devices: {e}")
            return []

    @staticmethod
    def connect_device(ip):
        """Attempts to connect to a device via TCP/IP."""
        try:
            target = f"{ip}:{DeviceConfig.TCP_PORT}"
            print(f"[DeviceManager] Attempting to connect to {target}...")
            subprocess.run(["adb", "connect", target], capture_output=True)
            time.sleep(2)  # Wait for connection to stabilize
            devices = DeviceManager.get_connected_devices()
            if target in devices:
                print(f"[DeviceManager] Successfully connected to {target}")
                return target
        except Exception as e:
            print(f"[DeviceManager] Failed to connect to {ip}: {e}")
        return None

    @staticmethod
    def is_server_installed(device_id):
        """Checks if Appium UiAutomator2 Server is installed on the device."""
        try:
            output = subprocess.check_output(
                ["adb", "-s", device_id, "shell", "pm", "list", "packages", "io.appium.uiautomator2.server"],
                stderr=subprocess.STDOUT
            ).decode("utf-8")
            return "io.appium.uiautomator2.server" in output
        except:
            return False

    @staticmethod
    def get_target_device():
        """
        Finds and returns the best available device UDID.
        Priority: USB (Serial) -> Configured IPs (LAN/WIFI)
        Must have Appium Server installed for IVI system.
        """
        connected = DeviceManager.get_connected_devices()
        
        # 1. Check for USB devices (usually don't contain '.')
        for device in connected:
            if "." not in device:
                if DeviceManager.is_server_installed(device):
                    print(f"[DeviceManager] Found USB device with server: {device}")
                    return device
                else:
                    print(f"[DeviceManager] Skipping USB device {device} (No Appium server)")
        
        # 2. Check for already connected TCP devices
        for ip in DeviceConfig.TARGET_IPS:
            target = f"{ip}:{DeviceConfig.TCP_PORT}"
            if target in connected:
                if DeviceManager.is_server_installed(target):
                    print(f"[DeviceManager] Using connected TCP device with server: {target}")
                    return target
                else:
                    print(f"[DeviceManager] Skipping TCP device {target} (No Appium server)")

        # 3. Try connecting to configured IPs
        for ip in DeviceConfig.TARGET_IPS:
            target = DeviceManager.connect_device(ip)
            if target:
                if DeviceManager.is_server_installed(target):
                    print(f"[DeviceManager] Successfully connected to {target} (with server)")
                    return target
                else:
                    print(f"[DeviceManager] Connected to {target} but server missing. Skipping.")
                
        # 4. Fallback: return the first connected device if any (with server)
        for device in connected:
            if DeviceManager.is_server_installed(device):
                print(f"[DeviceManager] Falling back to first available with server: {device}")
                return device
            
        print("[DeviceManager] Critical: No devices found or NO device has Appium server installed!")
        # return the first available anyway as a last resort, maybe it's just slow to respond?
        return connected[0] if connected else None

