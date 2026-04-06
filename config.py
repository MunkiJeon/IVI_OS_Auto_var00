class DeviceConfig:
    # Priority connection list (USB -> LAN -> WLAN)
    # USB connection (Serial Number)
    USB_DEVICE_IDS = ["a8d4f4f2453", "bb60ed15853"] 
    
    # TCP/IP Target list (LAN/WLAN)
    TARGET_IPS = [
        "192.168.0.183", 
        "192.168.0.204",
        "192.168.0.111", 
        "192.168.0.164"
    ]
    TCP_PORT = 5555

    
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
