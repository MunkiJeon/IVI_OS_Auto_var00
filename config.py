class DeviceConfig:
    # USB Connection
    USB_DEVICE_ID = "bb60ed15853"
    
    # TCP/IP Connection (Primary)
    TCP_IP = "192.168.0.183" #"192.168.0.204", "192.168.0.183"
    TCP_PORT = 5555
    TCP_DEVICE_ID = f"{TCP_IP}:{TCP_PORT}"
    
    # Appium Server
    APPIUM_SERVER_URL = "http://127.0.0.1:4723"

class AppConfig:
    # Packages and Activities
    VEHICLE_CONTROL = {
        "package": "ai.umos.vehiclecontrol",
        "activity": "ai.umos.vehiclecontrol.VehicleControlActivity"
    }
    
    APP_GRID = {
        "package": "ai.umos.applibrary",
        "activity": "ai.umos.applibrary.AppGridActivity"
    }
    
    MAIN_SCREEN = {
        "package": "ai.umos.callandmessage",
        "activity": "ai.umos.mainscreen.MainScreenActivity"
    }
    # Main package for capabilities if needed
    BASE_PACKAGE = "ai.umos"
