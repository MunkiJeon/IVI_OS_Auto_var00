import inspect
from pages.vehicle_control_page import VehicleControlPage
from pages.base_page import BasePage

try:
    v = VehicleControlPage(None)
    print(f"VehicleControlPage file: {inspect.getfile(VehicleControlPage)}")
    print(f"BasePage file: {inspect.getfile(BasePage)}")
    
    method = v.tap_coordinates
    print(f"tap_coordinates defined in: {inspect.getfile(method)}")
    print(f"tap_coordinates source: \n{inspect.getsource(method)[:100]}")
    
except Exception as e:
    print(f"Error: {e}")
