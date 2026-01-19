from appium import webdriver
from appium.options.android import UiAutomator2Options
from config import DeviceConfig

class DriverFactory:
    @staticmethod
    def get_driver():
        options = UiAutomator2Options()
        options.platform_name = "Android"
        options.automation_name = "UiAutomator2"
        options.udid = DeviceConfig.TCP_DEVICE_ID
        options.no_reset = True
        
        # =====================================================
        # IVI 시스템 연결 설정 (Appium Settings 앱 설치 우회)
        # =====================================================
        # IVI 시스템은 외부 APK 설치가 제한되어 있어서
        # Appium Settings 앱과 UiAutomator2 서버 설치를 건너뛰도록 설정
        options.set_capability("skipServerInstallation", True)
        options.set_capability("skipDeviceInitialization", True)
        options.set_capability("skipUnlock", True)
        options.set_capability("disableWindowAnimation", True)
        
        # 타임아웃 설정 증가 (IVI 시스템은 응답이 느릴 수 있음)
        options.set_capability("newCommandTimeout", 300)
        options.set_capability("uiautomator2ServerLaunchTimeout", 60000)
        options.set_capability("uiautomator2ServerInstallTimeout", 60000)
        
        # 안정성 설정
        options.set_capability("settings[allowInvisibleElements]", True)
        options.set_capability("settings[ignoreUnimportantViews]", False)
        options.set_capability("settings[waitForIdleTimeout]", 500)
        
        driver = webdriver.Remote(DeviceConfig.APPIUM_SERVER_URL, options=options)
        return driver
