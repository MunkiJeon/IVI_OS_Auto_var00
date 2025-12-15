from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from config import AppConfig

class MainScreenPage(BasePage):
    # Placeholder Locators
    HOME_ICON = (AppiumBy.ACCESSIBILITY_ID, "Home")
    
    def start(self):
        self.driver.execute_script('mobile: startActivity', {
            'component': f"{AppConfig.MAIN_SCREEN['package']}/{AppConfig.MAIN_SCREEN['activity']}"
        })

    def is_loaded(self):
        return self.driver.current_package == AppConfig.MAIN_SCREEN['package']
