from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from config import AppConfig

class AppGridPage(BasePage):
    # Placeholder Locators
    GRID_CONTAINER = (AppiumBy.ID, "ai.umos.applibrary:id/grid_container")
    
    def start(self):
        self.driver.execute_script('mobile: startActivity', {
            'component': f"{AppConfig.APP_GRID['package']}/{AppConfig.APP_GRID['activity']}"
        })

    def is_loaded(self):
        return self.driver.current_package == AppConfig.APP_GRID['package']
