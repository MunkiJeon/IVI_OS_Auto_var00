from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import TYPE_CHECKING, List, Optional, Tuple, cast
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.pointer_input import PointerInput
from typing_extensions import Self

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        element = self.find_element(locator)
        element.click()

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text

    def is_displayed(self, locator):
        try:
            element = self.find_element(locator)
            if element.is_displayed():
                return True
            # Fallback: check if element has visible dimensions
            # This handles cases where displayed="false" but element is visible on screen
            size = element.size
            return size['width'] > 0 and size['height'] > 0
        except:
            return False

    def wait_for_element(self, locator, timeout=10):
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except:
            return None

    def tap(self, positions: List[Tuple[int, int]], duration: Optional[int] = None) -> Self:
        """Taps on an particular place with up to five fingers, holding for a
        certain time
        Args:
            positions: an array of tuples representing the x/y coordinates of
                the fingers to tap. Length can be up to five.
            duration: length of time to tap, in ms
        Usage:
            driver.tap([(100, 20), (100, 60), (100, 100)], 500)
        Returns:
            Union['WebDriver', 'ActionHelpers']: Self instance
        """
        if len(positions) == 1:
            actions = ActionChains(cast('WebDriver', self))
            actions.w3c_actions = ActionBuilder(self, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
            x = positions[0][0]
            y = positions[0][1]
            actions.w3c_actions.pointer_action.move_to_location(x, y)
            actions.w3c_actions.pointer_action.pointer_down()
            if duration:
                actions.w3c_actions.pointer_action.pause(duration / 1000)
            else:
                actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()
        else:
            finger = 0
            actions = ActionChains(cast('WebDriver', self))
            actions.w3c_actions.devices = []
            for position in positions:
                finger += 1
                x = position[0]
                y = position[1]
                # https://github.com/SeleniumHQ/selenium/blob/trunk/py/selenium/webdriver/common/actions/pointer_input.py
                new_input = actions.w3c_actions.add_pointer_input('touch', f'finger{finger}')
                new_input.create_pointer_move(x=x, y=y)
                new_input.create_pointer_down(button=MouseButton.LEFT)
                if duration:
                    new_input.create_pause(duration / 1000)
                else:
                    new_input.create_pause(0.1)
                new_input.create_pointer_up(MouseButton.LEFT)
            actions.perform()
        return self