import sys
import os

# Add project root
sys.path.append(os.getcwd())

from pages.vehicle_control_page import VehicleControlPage
from appium.webdriver.common.appiumby import AppiumBy

print("Imported VehicleControlPage")
print("Attributes:")
for attr in dir(VehicleControlPage):
    if attr.startswith("QS_"):
        print(f"{attr}: {getattr(VehicleControlPage, attr)}")

print("\nSpecific Attribute Check:")
try:
    print(f"QS_DOOR_LOCK: {VehicleControlPage.QS_DOOR_LOCK}")
except AttributeError:
    print("QS_DOOR_LOCK is missing!")
