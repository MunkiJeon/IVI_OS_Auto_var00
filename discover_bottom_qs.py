from utils.driver_factory import DriverFactory
from pages.vehicle_control_page import VehicleControlPage
import time

def find_all_qs():
    driver = None
    try:
        driver = DriverFactory.get_driver()
        page = VehicleControlPage(driver)
        page.start()
        time.sleep(3)
        page.click_sidebar_menu('빠른 설정')
        time.sleep(2)
        
        # Capture initial
        with open('qs_0.xml', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        
        # Scroll 1
        print("Scrolling 1...")
        driver.swipe(1400, 800, 1400, 200, 1000)
        time.sleep(2)
        with open('qs_1.xml', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        driver.save_screenshot('qs_1.png')

        # Scroll 2
        print("Scrolling 2...")
        driver.swipe(1400, 800, 1400, 200, 1000)
        time.sleep(2)
        with open('qs_2.xml', 'w', encoding='utf-8') as f:
            f.write(driver.page_source)
        driver.save_screenshot('qs_2.png')
        
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    find_all_qs()
