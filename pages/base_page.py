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
        # XPath 2.0 issue fix: enforce XPath 1.0
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

    def click_sidebar_menu(self, menu_text):
        """
        좌측 사이드바 메뉴를 클릭합니다.
        메뉴가 보일 때까지 스크롤하며 찾습니다.
        """
        print(f"\n[Sidebar] '{menu_text}' 메뉴 탐색 및 클릭 시도...")
        
        # 사이드바 X좌표: 800 (사용자 확인)
        sidebar_x = 800
        max_scrolls = 5
        
        for i in range(max_scrolls + 1):
            try:
                # 존재 여부 확인 (is_displayed 대신 presence_of_element_located 사용)
                locator = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{menu_text}']")
                if self.is_displayed(locator):
                    print(f"[Sidebar] '{menu_text}' 발견. 클릭합니다.")
                    self.click(locator)
                    return True
            except:
                pass
                
            if i < max_scrolls:
                print(f"[Sidebar] 스크롤 진행 ({i+1}/{max_scrolls})...")
                # 아래서 위로 (컨텐츠는 위로)
                self.swipe(sidebar_x, 800, sidebar_x, 300, 1200)
                time.sleep(1.5)
                
        print(f"[Sidebar] '{menu_text}' 메뉴를 결국 찾지 못했습니다.")
        raise Exception(f"Sidebar menu '{menu_text}' not found after {max_scrolls} scrolls")

    def scroll_content_down(self):
        """
        우측 콘텐츠 영역을 아래로 길게 스크롤합니다.
        80% 칭 -> 20% 위치로 이동하여 더 많은 영역을 커버합니다.
        """
        size = self.driver.get_window_size()
        # 콘텐츠 영역 X좌표: 대략 1440 (1920의 75%)
        # 시작/종료 Y좌표를 70% -> 30%로 조정 (너무 길면 건너뛰고, 너무 짧으면 답답함)
        start_x = int(size['width'] * 0.90)
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)
        print(f"[Scroll] Content Down: ({start_x}, {start_y}) -> ({start_x}, {end_y})")
        self.swipe(start_x, start_y, start_x, end_y, 1500) 
        time.sleep(1.5)
        
    def scroll_and_find(self, locator, max_scrolls=3): 
        """
        요소가 보일 때까지 우측 콘텐츠 영역을 스크롤합니다.
        이미 보이면 즉시 반환합니다.
        """
        # 시작 전 최상단으로 이동 (옵션 - 여기서는 일단 현재 위치에서 시작)
        print(f"요소 탐색 시작: {locator}")
        
        for i in range(max_scrolls + 1):
            if self.is_displayed(locator):
                print(f"{self.title_split(locator)} 발견 ({i}회 스크롤)")
                return True
            
            if i < max_scrolls:
                print(f"스크롤 진행 ({i+1}/{max_scrolls})...")
                self.scroll_content_down()
        
        print("최대 스크롤 횟수 초과. 요소를 찾지 못했습니다.")
        return False

    def find_element(self, locator):
        """
        요소를 찾습니다. (Explicit Wait 10초 적용)
        """
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """
        요소를 찾아 클릭합니다.
        """
        element = self.find_element(locator)
        element.click()

    def get_text(self, locator):
        """
        요소의 텍스트를 가져옵니다.
        """
        element = self.find_element(locator)
        return element.text

    def is_displayed(self, locator):
        """
        요소가 화면에 표시되는지 확인합니다.
        안정성을 위해 presence_of_all_elements_located 검사로 대체 시도 (스크롤 중 감지력 향상)
        """
        try:
            # 존재만 하면 일단 True (스크롤 중에는 완전히 안 보일 수도 있음)
            elements = self.driver.find_elements(*locator)
            return len(elements) > 0
        except:
            return False

    def get_texts(self, locator, timeout=None, exclude_texts=None, min_y=None, min_x=None):
        """
        여러 요소의 텍스트를 읽어 리스트(배열)로 반환합니다.
        exclude_texts: 제외할 텍스트 리스트
        min_y: 해당 Y 좌표 이상(화면 아래쪽)에 위치한 요소만 포함
        min_x: 해당 X 좌표 이상(화면 오른쪽)에 위치한 요소만 포함
        """
        if exclude_texts is None:
            exclude_texts = []
        try:
            elements = self.driver.find_elements(locator, timeout=timeout)
            results = []
            for element in elements:
                text = element.text
                if not text or text in exclude_texts:
                    continue
                
                # 좌표 필터링 (min_y 이상만 추출)
                if min_y is not None:
                    if element.rect['y'] < min_y:
                        continue

                # 좌표 필터링 (min_x 이상만 추출)
                if min_x is not None:
                    if element.rect['x'] < min_x:
                        continue
                
                results.append(text)
            return results
        except:
            return []

    def get_all_texts(self, timeout=None, exclude_texts=None, min_y=None, min_x=None):
        """
        화면 전체에서 텍스트를 읽어 리스트로 반환합니다.
        exclude_texts: 결과에서 제외할 텍스트 리스트
        min_y: 해당 Y 좌표 이상(화면 아래쪽)에 위치한 요소만 포함
        min_x: 해당 X 좌표 이상(화면 오른쪽)에 위치한 요소만 포함
        """
        # 모든 요소를 찾는 일반적인 XPath
        # Android: //* (또는 //android.widget.TextView 등 더 구체적으로 지정 가능하나 전체 탐색은 //*)
        locator = (AppiumBy.XPATH, "//*")
        return self.get_texts(locator, timeout=timeout, exclude_texts=exclude_texts, min_y=min_y, min_x=min_x)

    def scroll_to_element(self, locator):
        """
        화면을 스크롤하여 요소를 찾습니다. (UiScrollable 사용)
        주의: locator는 텍스트 기반 검색에 최적화된 로직으로 대체될 수 있습니다.
        """
        try:
            # 텍스트가 locator에 포함된 경우 UiScrollable 시도 (간단한 예시)
            # 실제로는 UiScrollable 구문을 조립해야 함. 여기서는 Swipe로 대체하거나
            # text 속성이 있는 경우 scroll_to_text 사용 권장.
            return self.find_element(locator)
        except:
            return None

    def scroll_to_text(self, text):
        """
        텍스트를 포함하는 요소가 보일 때까지 스크롤합니다. (Android UiScrollable 사용)
        """
        try:
            self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,
                f'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("{text}").instance(0))'
            )
            return True
        except Exception as e:
            print(f"스크롤 실패 ({text}): {e}")
            return False
            
    def scroll_down(self, duration=1000):
        """
        화면을 아래로 스크롤합니다. (콘텐츠가 위로 이동)
        """
        size = self.driver.get_window_size()
        start_x = int(size['width'] * 0.90)
        start_y = int(size['height'] * 0.8)
        end_y = int(size['height'] * 0.2)
        self.swipe(start_x, start_y, start_x, end_y, duration)

    def scroll_up(self, duration=500):
        """
        화면을 위로 스크롤합니다. (콘텐츠가 아래로 이동)
        """
        size = self.driver.get_window_size()
        start_x = int(size['width'] * 0.90)
        start_y = int(size['height'] * 0.2)
        end_y = int(size['height'] * 0.8)
        self.swipe(start_x, start_y, start_x, end_y, duration)

    def swipe(self, start_x, start_y, end_x, end_y, duration=800):
        """
        지정된 좌표로 스와입 동작을 수행합니다.
        기본 driver.swipe를 사용하여 최대한의 안정성을 확보합니다.
        """
        try:
            print(f"[Swipe] ({start_x}, {start_y}) -> ({end_x}, {end_y}), dur={duration}ms")
            self.driver.swipe(start_x, start_y, end_x, end_y, duration)
        except Exception as e:
            print(f"[Critical Error] Swipe failed: {e}")

    def long_press_element(self, locator, duration=2000):
        """
        요소를 길게 누릅니다. (Long Press)
        """
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.click_and_hold(element).pause(duration / 1000).release().perform()

    def long_press_coordinates(self, x, y, duration=2000):
        """
        특정 좌표를 길게 누릅니다.
        1. mobile: longClickGesture (UiAutomator2 Native) 시도
        2. 실패 시 ADB Shell Input Swipe (H/W Level) 시도
        3. 최후의 수단으로 W3C Actions 시도
        """
        # 1. Try mobile: longClickGesture
        try:
            self.driver.execute_script('mobile: longClickGesture', {
                'x': int(x),
                'y': int(y),
                'duration': int(duration)
            })
            print(f"[Long Press] ({x}, {y}) for {duration}ms (via mobile: longClickGesture)")
            return
        except Exception as e:
            print(f"[Long Press] mobile: longClickGesture failed: {e}")

        # 2. Try ADB Swipe (Input Keyevent logic)
        try:
            # Determine Device ID Dynamicallly
            device_id = None
            
            # Method 1: Check 'udid' capability (Standard)
            try:
                device_id = self.driver.capabilities.get('udid')
            except:
                pass

            # Method 2: Check 'deviceName' capability (Often contains IP:Port)
            if not device_id:
                try:
                    name = self.driver.capabilities.get('deviceName')
                    if name and ':' in name: # Looks like an IP:Port
                        device_id = name
                except:
                    pass

            # Method 3: Parsing Command Executor URL (e.g., http://127.0.0.1:4723/wd/hub -> check active sessions or config)
            # Since we can't easily get the remote device ID from just the URL if it's not in caps,
            # we will rely on what the user provided as 'connected' context.
            # However, for robustness, if we still don't have an ID, we loop through ADB devices 
            # and pick the one that matches the TCP_IP pattern if only one is connected via TCP,
            # or failover to the one defined in Config if it matches an active device.
            
            if not device_id:
                # Get list of connected stats
                try:
                    output = subprocess.check_output("adb devices", shell=True).decode('utf-8')
                    lines = [line.strip() for line in output.split('\n') if line.strip() and 'device' in line and 'List' not in line]
                    
                    # If only 1 device is connected, use it.
                    if len(lines) == 1:
                        device_id = lines[0].split('\t')[0]
                    else:
                        # If multiple, try to find one that matches our Config.TCP_IP as a hint, 
                        # but ideally 'udid' should have been present. 
                        # As a fallback, check if any line matches the known IPs mentioned by user or config.
                        # This part is tricky without an explicit link, but typically 'udid' is reliable in 99% cases for Appium.
                        # Fallback to config if all else fails.
                        device_id = DeviceConfig.TCP_DEVICE_ID
                except:
                    device_id = DeviceConfig.TCP_DEVICE_ID

            print(f"[Long Press] Falling back to ADB on device: {device_id}")
            cmd = f"adb -s {device_id} shell input swipe {int(x)} {int(y)} {int(x)} {int(y)} {int(duration)}"
            subprocess.run(cmd, shell=True, check=True)
            print(f"[Long Press] Executed ADB command: {cmd}")
            return
        except Exception as e:
            print(f"[Long Press] ADB fallback failed: {e}")

        # 3. Last Resort: W3C Actions
        print("[Long Press] Falling back to W3C Actions (Likely to fail on Overlays)")
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
        actions.w3c_actions.pointer_action.move_to_location(x, y)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.pause(duration / 1000)
        actions.w3c_actions.pointer_action.release()
        actions.perform()

    def tap_coordinates(self, x, y):
        """
        특정 좌표를 탭합니다.
        """
        try:
            self.driver.execute_script('mobile: clickGesture', {'x': int(x), 'y': int(y)})
        except:
            # Fallback to ActionChains if script execution fails
            actions = ActionChains(self.driver)
            actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, 'touch'))
            actions.w3c_actions.pointer_action.move_to_location(x, y)
            actions.w3c_actions.pointer_action.pointer_down()
            actions.w3c_actions.pointer_action.pause(0.1)
            actions.w3c_actions.pointer_action.release()
            actions.perform()

    def random_area_interaction(self, x1, y1, x2, y2, interaction_type='tap', duration=1000):
        """
        지정된 영역(x1, y1) ~ (x2, y2) 내에서 랜덤한 좌표로 탭하거나 드래그합니다.
        """
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        
        # 시작 좌표 랜덤 생성
        start_x = random.randint(min_x, max_x)
        start_y = random.randint(min_y, max_y)
        
        if interaction_type == 'tap':
            print(f"[Random Area] Tapping at ({start_x}, {start_y}) within ({min_x}, {min_y})~({max_x}, {max_y})")
            self.tap_coordinates(start_x, start_y)
        elif interaction_type == 'drag':
            # 종료 좌표 랜덤 생성
            end_x = random.randint(min_x, max_x)
            end_y = random.randint(min_y, max_y)
            print(f"[Random Area] Dragging from ({start_x}, {start_y}) to ({end_x}, {end_y}) within box")
            self.swipe(start_x, start_y, end_x, end_y, duration)

    def wait_for_element_visible(self, locator, timeout=10):
        """
        요소가 보일 때까지 기다립니다.
        """
        try:
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        except:
            return None

    def toggle_tap(self, locator, x_offset, y_offset):
        """
        토글 버튼을 탭합니다.
        """
        element = self.find_element(locator)
        rect = element.rect
        toggle_x = rect['x'] + x_offset
        toggle_y = rect['y'] + y_offset
        # print(f"{self.title_split(locator)} 좌표: ({toggle_x}, {toggle_y})")
        self.tap_coordinates(toggle_x, toggle_y)

    def popup_find_tap(self, locator):
        """
        팝업 버튼을 찾아 클릭합니다. (없으면 넘어감)
        """
        try:
            popup_off = self.find_element(locator)
            popup_off.click()
            print(f"{self.title_split(locator)} 탭")
        except NoSuchElementException:
            print(f"{self.title_split(locator)} 없음")

    def click_after_text(self, anchor_text, target_text):
        """
        anchor_text 뒤의 target_text를 클릭합니다.
        이미 anchor_text를 찾은 상태라고 가정(scroll_and_find 호출됨)하며, 
        실패시에만 추가 스크롤을 시도합니다.
        """
        anchor_text = anchor_text
        target_text = target_text
        if isinstance(anchor_text,tuple):
            anchor_text = self.title_split(anchor_text)
        if isinstance(target_text,tuple):
            target_text = self.title_split(target_text)
        
        xpath = f"//android.widget.TextView[@text='{anchor_text}']/following::android.widget.TextView[@text='{target_text}'][1]"
        print(f"[Relative Click] '{anchor_text}' -> '{target_text}' 클릭 시도...")
        
        try:
            # 즉시 클릭 시도
            self.click((AppiumBy.XPATH, xpath))
        except Exception:
            print(f"[Relative Click] 실패. 한 번 더 스크롤 후 재시도...")
            self.scroll_content_down()
            self.click((AppiumBy.XPATH, xpath))

    def get_grouped_button_coordinates(self, anchor_text, button_count, group_width, group_height, y_offset=15):
        """
        anchor_text 아래에 가로로 나열된 버튼 그룹의 좌표를 계산합니다.
        가이드: 버튼 그룹의 시작 X는 anchor_text의 시작 X와 같다고 가정합니다.
        """
        anchor = self.find_element((AppiumBy.XPATH, f"//android.widget.TextView[@text='{anchor_text}']"))
        rect = anchor.rect
        
        # 그룹 시작점 계산
        group_x_start = rect['x']
        group_y_start = rect['y'] + rect['height'] + y_offset
        
        button_width = group_width / button_count
        coords = []
        
        for i in range(button_count):
            center_x = group_x_start + (i + 0.5) * button_width
            center_y = group_y_start + (group_height / 2)
            coords.append((int(center_x), int(center_y)))
            
        return coords

    def click_grouped_button(self, anchor_text, button_index, button_count, group_width, group_height, y_offset=15):
        """
        계산된 좌표를 기반으로 버튼 그룹 내의 특정 인덱스 버튼을 클릭합니다.
        """
        coords = self.get_grouped_button_coordinates(anchor_text, button_count, group_width, group_height, y_offset)
        if 0 <= button_index < len(coords):
            x, y = coords[button_index]
            print(f"[Group Click] '{anchor_text}' 그룹의 {button_index}번 버튼 클릭: ({x}, {y})")
            self.tap_coordinates(x, y)
        else:
            print(f"[Error] 잘못된 버튼 인덱스: {button_index}")

    def title_split(self, locator):
        return locator[1].split("//android.widget.TextView[@text='")[1].rsplit("']")[0]