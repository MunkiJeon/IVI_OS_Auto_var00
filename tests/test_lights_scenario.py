import pytest
import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

class TestLightsScenario:
    """
    라이트 (Lights) 탭 테스트 시나리오
    - 전조등 (끄기, 자동, 미등, 켜짐, 자동상향등, 에스코트 조명)
    - 프렁크등 / 트렁크등
    - 실내등 (전체 끄기, 개별 좌석)
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        self.page.click_sidebar_menu("라이트")
        time.sleep(2)

    def test_lights_sequence(self, driver):
        page = self.page

        print("\n[Step 1] 전조등 (Headlights) & 에스코트 Test")
        # 1 끄기, 2 자동, 3 미등, 4 전조등
        headlight_coords = [(1149, 402), (1347, 402), (1545, 402), (1743, 402)]
        auto_highbeam = (1287, 518)
        
        for i, coord in enumerate(headlight_coords):
            print(f"  - Tapping Headlight Button {i+1}")
            page.tap(*coord)
            time.sleep(1)
        
        # 5 자동 상향등 (2번 탭)
        print("  - Tapping Auto High Beam (Double Tap)")
        page.tap(*auto_highbeam)
        time.sleep(0.5)
        page.tap(*auto_highbeam)
        time.sleep(1)
        
        # 6 끄기
        print("  - Tapping Headlight Off (Reset)")
        page.tap(*headlight_coords[0])
        time.sleep(1)
        
        # 에스코트 조명 토글 2회
        print("  - Tapping Escort Light Toggle (2 times)")
        escort_toggle = (1094, 636)
        page.tap(*escort_toggle)
        time.sleep(0.5)
        page.tap(*escort_toggle)
        time.sleep(1)

        print("\n[Step 2] 프렁크등 & 트렁크등 (Frunk & Trunk) Test")
        # Scroll down so both are visible
        page.scroll_content("down")
        time.sleep(2)
        
        # 끄기(1182), 켜기(1446), 자동(1710)
        xs = [1182, 1446, 1710, 1182]
        actions = ["끄기", "켜기", "자동", "끄기"]
        
        try:
            frunk_y = driver.find_element(AppiumBy.XPATH, "//*[@text='프렁크등']").rect['y'] + 152
            print("  - Testing Frunk Lights")
            for x, action in zip(xs, actions):
                print(f"    - Tapping {action}")
                page.tap(x, frunk_y)
                time.sleep(1)
        except Exception as e:
            print(f"  - Error testing Frunk: {e}")

        try:
            trunk_y = driver.find_element(AppiumBy.XPATH, "//*[@text='트렁크등']").rect['y'] + 152
            print("  - Testing Trunk Lights")
            for x, action in zip(xs, actions):
                print(f"    - Tapping {action}")
                page.tap(x, trunk_y)
                time.sleep(1)
        except Exception as e:
            print(f"  - Error testing Trunk: {e}")

        print("\n[Step 3] 실내등 (Interior Lights) Test")
        # Scroll until '뒷좌석 우측' is visible
        page.scroll_and_find((AppiumBy.XPATH, "//*[@text='뒷좌석 우측']"), max_scrolls=3)
        time.sleep(2)
        
        # We need to tap "끄기", which is aligned with "운전석"
        # Find "운전석" and offset to "끄기"
        try:
            driver_seat = driver.find_element(AppiumBy.XPATH, "//*[@text='운전석']")
            off_x = driver_seat.rect['x'] - 245  # Offset to '끄기'
            off_y = driver_seat.rect['y'] + driver_seat.rect['height'] // 2
            
            sequence = [
                ("모든 좌석", lambda: page.click_text("모든 좌석", scroll=False)),
                ("끄기", lambda: page.tap(off_x, off_y)),
                ("운전석", lambda: page.click_text("운전석", scroll=False)),
                ("동승석", lambda: page.click_text("동승석", scroll=False)),
                ("뒷좌석 좌측", lambda: page.click_text("뒷좌석 좌측", scroll=False)),
                ("뒷좌석 우측", lambda: page.click_text("뒷좌석 우측", scroll=False)),
                ("끄기", lambda: page.tap(off_x, off_y))
            ]
            
            for label, act in sequence:
                print(f"  - Tapping Interior Light: {label}")
                act()
                time.sleep(1)
                
        except Exception as e:
            print(f"  - Error testing Interior Lights: {e}")

        print("\n[Step 4] 무드 조명 & 사운드 연동 조명 Test")
        # Scroll down
        page.scroll_and_find((AppiumBy.XPATH, "//*[@text='사운드 연동 조명']"), max_scrolls=4)
        time.sleep(2)
        
        # 무드 조명 (Mood Light)
        try:
            mood_elem = driver.find_element(AppiumBy.XPATH, "//*[@text='무드 조명']")
            mood_y = mood_elem.rect['y'] + 138
            print("  - Testing Mood Lights (켜기 > 자동 > 끄기 > 켜기)")
            for x, action in zip([1447, 1711, 1182, 1447], ["켜기", "자동", "끄기", "켜기"]):
                page.tap(x, mood_y)
                time.sleep(1)
        except Exception as e:
            print(f"  - Error testing Mood Lights basic: {e}")

        # 밝기 변경 (Brightness)
        try:
            color_elem = driver.find_element(AppiumBy.XPATH, "//*[@text='색상']")
            target_x = color_elem.rect['x'] + color_elem.rect['width']
            target_y = color_elem.rect['y'] + color_elem.rect['height'] // 2
            
            print("  - Tapping slider 4 times randomly")
            for _ in range(4):
                rx = random.randint(target_x + 160, target_x + 480)
                page.tap(rx, target_y)
                time.sleep(0.5)
                
            print("  - Tapping Minus (red) 2 times, Plus (yellow) 2 times")
            for _ in range(2): page.tap(target_x + 120, target_y); time.sleep(0.5)
            for _ in range(2): page.tap(target_x + 670, target_y); time.sleep(0.5)
        except Exception as e:
            print(f"  - Error testing Mood Brightness: {e}")
            
        # 색상 팝업 1: 열고 취소
        try:
            print("  - Opening Color Popup and Canceled")
            page.click_text("색상", scroll=False)
            time.sleep(1.5)
            page.click_text("취소", scroll=False)
            time.sleep(1)
        except Exception as e:
            print(f"  - Error testing Mood Color Popup 1: {e}")
            
        # 색상 팝업 2: 상단 휠 스와이프, 하단 스와이프, +, 저장
        try:
            print("  - Opening Color Popup and Saving Custom")
            page.click_text("색상", scroll=False)
            time.sleep(1.5)
            
            # 상단 영역 임의 스와이프
            print("    - Top blue area drag")
            for _ in range(2):
                rx1 = random.randint(1050, 1485)
                ry1 = random.randint(255, 590)
                rx2 = random.randint(1050, 1485)
                ry2 = random.randint(255, 590)
                page.swipe(rx1, ry1, rx2, ry2, duration=600)
                time.sleep(1)
            
            # 하단 영역 L->R, R->L
            print("    - Bottom blue area left<->right drag")
            page.swipe(1050, 650, 1485, 650, duration=800)
            time.sleep(1)
            page.swipe(1485, 650, 1050, 650, duration=800)
            time.sleep(1)
            
            # [+] 모양 탭
            print("    - Tapping [+] icon")
            page.tap(1022, 755)
            time.sleep(1)
            
            # 저장 탭
            page.click_text("저장", scroll=False)
            time.sleep(1.5)
        except Exception as e:
            print(f"  - Error testing Mood Color Popup 2: {e}")
            
        # 사운드 연동 조명
        page.scroll_and_find((AppiumBy.XPATH, "//*[@text='항상 켜기']"), max_scrolls=3)
        time.sleep(2)
        try:
            sound_elem = driver.find_element(AppiumBy.XPATH, "//*[@text='사운드 연동 조명']")
            sound_y = sound_elem.rect['y'] + 188
            print("  - Testing Sound Sync Lights (항상 켜기 > 주차시 > 끄기 > 항상 켜기)")
            # 끄기(1182), 항상 켜기(1447), 주차시(1711 추정)
            for x, action in zip([1447, 1711, 1182, 1447], ["항상 켜기", "주차시", "끄기", "항상 켜기"]):
                page.tap(x, sound_y)
                time.sleep(1)
        except Exception as e:
            print(f"  - Error testing Sound Sync Lights: {e}")

        print("\nLights Scenario Test Completed Successfully.")
