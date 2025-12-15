import sys
import os

# Add project root to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.driver_factory import DriverFactory
import time

def dump_source():
    print("Connecting to device to dump page source...")
    try:
        driver = DriverFactory.get_driver()
        # Wait briefly to ensure we capture the rendered state
        time.sleep(2)
        
        source = driver.page_source
        
        output_file = "current_source.xml"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(source)
            
        print(f"Successfully dumped page source to {output_file}")
        
    except Exception as e:
        print(f"Error dumping source: {e}")
    finally:
        if 'driver' in locals():
            driver.quit()

if __name__ == "__main__":
    dump_source()
