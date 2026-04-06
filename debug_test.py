import traceback
import sys
import os

# Ensure the root directory is in the python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from utils.driver_factory import DriverFactory
from tests.test_quick_settings_scenario import TestQuickSettingsScenario

def debug_run():
    driver = None
    try:
        driver = DriverFactory.get_driver()
        test = TestQuickSettingsScenario()
        test.setup(driver)
        test.test_quick_settings_refactored(driver)
        print("Test Passed!")
    except Exception:
        print("\n" + "="*60)
        print("TEST FAILED - TRACEBACK:")
        print("="*60)
        traceback.print_exc()
        print("="*60)
    finally:
        if driver:
            driver.quit()

if __name__ == "__main__":
    debug_run()
