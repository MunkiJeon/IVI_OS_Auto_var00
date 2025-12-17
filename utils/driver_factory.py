from appium import webdriver
from appium.options.android import UiAutomator2Options
from config import DeviceConfig

class DriverFactory:
    @staticmethod
    def get_driver():
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        # Using TCP/IP device by default as requested
        options.udid = DeviceConfig.TCP_DEVICE_ID
        options.no_reset = True
        
        # Stability settings
        options.set_capability("settings[allowInvisibleElements]", True)
        options.set_capability("settings[ignoreUnimportantViews]", False)
        options.set_capability("settings[waitForIdleTimeout]", 500)
        
        # Optional: Set a default app to launch via capabilities if needed, 
        # but often in IVI we just want to connect to the system.
        # We can leave appPackage/appActivity empty here and start them in tests,
        # or set a default one. For now, we keep it generic to just connect.
        
        driver = webdriver.Remote(DeviceConfig.APPIUM_SERVER_URL, options=options)
        return driver
