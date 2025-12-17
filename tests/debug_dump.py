import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

def test_dump_source(driver):
    page = VehicleControlPage(driver)
    page.start()
    time.sleep(2)
    page.reset_sidebar()
    print("Clicking Lights...")
    try:
        page.click(page.MENU_LIGHTS)
        time.sleep(2)
    except Exception as e:
        print(f"Click failed: {e}")
    
    print("Dumping source...")
    with open("debug_source.xml", "w", encoding="utf-8") as f:
        f.write(driver.page_source)
    print("Dumped to debug_source.xml")
