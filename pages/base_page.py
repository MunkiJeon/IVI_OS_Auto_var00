from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import TYPE_CHECKING, List, Optional, Tuple, cast
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.common.exceptions import NoSuchElementException
import time
import random
import subprocess
import cv2
import numpy as np
import os
from config import AppConfig, DeviceConfig

if TYPE_CHECKING:
    from appium.webdriver.webdriver import WebDriver

class BasePage:
    """
    모든 페이지 객체(Page Object)의 부모 클래스입니다.
    공통적으로 사용되는 모바일 동작(클릭, 스와입, 스크롤 등)을 정의합니다.
    """
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        try:
            self.driver.update_settings({"enforceXPath1": True})
        except:
            pass

    def start(self):
        """차량 제어 액티비티를 시작합니다."""
        try:
            self.driver.terminate_app(AppConfig.VEHICLE_CONTROL['package'])
        except:
            pass
        self.driver.execute_script('mobile: startActivity', {
            'component': f"{AppConfig.VEHICLE_CONTROL['package']}/{AppConfig.VEHICLE_CONTROL['activity']}"
        })

    def is_loaded(self):
        """페이지 로드 여부를 확인합니다."""
        return self.is_displayed(self.TITLE)

    # --- 헬퍼 메소드 (기능 정의) ---

    def tap(self, x, y):
        """특정 좌표를 탭합니다. (Native clickGesture 시도 후 ActionChains Fallback)"""
        try:
            self.driver.execute_script('mobile: clickGesture', {'x': int(x), 'y': int(y)})
        except:
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
            actions.w3c_actions.pointer_action.move_to_location(x, y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

    def swipe(self, start_x, start_y, end_x=1880, end_y=100, duration=800):
        """지정된 좌표로 스와입 동작을 수행합니다."""
        try:
            print(f"[Swipe] ({start_x}, {start_y}) -> ({end_x}, {end_y}), dur={duration}ms")
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        except Exception as e:
            print(f"[Critical Error] Swipe failed: {e}")

    def scroll_content(self, direction="down", duration=1200):
        """우측 콘텐츠 영역을 스크롤합니다."""
        size = self.driver.get_window_size()
        x = int(size['width'] * 0.90)
        y_start, y_end = (int(size['height'] * 0.8), int(size['height'] * 0.2)) if direction == "down" else (int(size['height'] * 0.2), int(size['height'] * 0.8))
        self.swipe(x, y_start, x, y_end, duration)
        time.sleep(1.2)

    def scroll_and_find(self, locator, max_scrolls=3):
        """요소가 보일 때까지 우측 콘텐츠 영역을 스크롤합니다."""
        for i in range(max_scrolls + 1):
            if self.is_displayed(locator):
                return True
            if i < max_scrolls:
                self.scroll_content("down")
        return False

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        self.find_element(locator).click()

    def is_displayed(self, locator):
        try:
            return len(self.driver.find_elements(*locator)) > 0
        except:
            return False

    def get_texts(self, locator, exclude_texts=None, min_y=None, min_x=None):
        """요소들의 텍스트를 리스트로 반환하며 필터링합니다."""
        if exclude_texts is None: exclude_texts = []
        try:
            elements = self.driver.find_elements(*locator)
            results = []
            for el in elements:
                t = el.text
                if not t or t in exclude_texts: continue
                if min_y and el.rect['y'] < min_y: continue
                if min_x and el.rect['x'] < min_x: continue
                results.append(t)
            return results
        except:
            return []

    def click_text(self, text, scroll=True):
        """텍스트를 기반으로 요소를 찾아 클릭합니다."""
        locator = (AppiumBy.XPATH, f"//*[@text='{text}']")
        if scroll and self.scroll_and_find(locator):
            self.click(locator)
            return True
        elif not scroll:
            try:
                self.click(locator)
                return True
            except: pass
        return False

    def click_image(self, image_name, threshold=0.8):
        """이미지 매칭을 통해 클릭합니다."""
        template_path = os.path.join("resources", "images", f"{image_name}.png")
        if not os.path.exists(template_path): return False
        self.driver.save_screenshot("current_screen.png")
        screen, template = cv2.imread("current_screen.png"), cv2.imread(template_path)
        res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        if max_val >= threshold:
            h, w = template.shape[:2]
            self.tap(max_loc[0] + w // 2, max_loc[1] + h // 2)
            return True
        return False

    def toggle_tap(self, locator, x_offset, y_offset):
        rect = self.find_element(locator).rect
        self.tap(rect['x'] + x_offset, rect['y'] + y_offset)

    def popup_find_tap(self, locator):
        try:
            self.find_element(locator).click()
        except:
            pass

    def click_sidebar_menu(self, menu_text):
        sidebar_x = 800
        for i in range(15):
            locator = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{menu_text}']")
            if self.is_displayed(locator):
                self.click(locator)
                return True
            self.swipe(sidebar_x, 800, sidebar_x, 300, 1200)
            time.sleep(1.2)
        raise Exception(f"Menu '{menu_text}' not found")

    def title_split(self, locator):
        try:
            return locator[1].split("@text='")[1].split("'")[0]
        except:
            return str(locator)
