
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import NoSuchElementException
from pages.vehicle_control_page import VehicleControlPage
from selenium.webdriver.common.action_chains import ActionChains

class TestDrivingScenario:
    """
    주행 (Driving) 탭 테스트 시나리오
    - 주행 편의 기능 (눈/빗길, ESC, 크립 등)
    - 주행 안전 (전방 충돌, 차선 이탈, 사각지대 등)
    - 주행 상세 설정 (파킹 브레이크 롱프레스, 사각지대 카메라)
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        # 사이드바 메뉴 클릭 (이미 텍스트 기반)
        self.page.click_sidebar_menu("주행")
        time.sleep(1)
        yield

    def test_driving_convenience_toggles(self, driver):
        """
        [시나리오] 주행 편의 기능 테스트 (텍스트 기반 리팩토링)
        """
        print("\n[Test] 주행 편의 기능 테스트 시작")
        
        # 1. 가속 모드 변경 (텍스트 기반 클릭)
        accel_modes = ["부드럽게", "표준", "빠르게"]
        for mode in accel_modes:
            print(f"가속 모드 변경 시도: {mode}")
            self.page.click_text(mode, scroll=False)
            time.sleep(1)

        # 2. 눈/빗길 보조 모드 토글
        print("눈/빗길 보조 모드 토글 테스트")
        for _ in range(2):
            self.page.click_text("눈/빗길 보조", scroll=False) 
            time.sleep(1)
        
        # 3. 조향 반응
        steering_modes = ["표준", "가볍게"]
        for mode in steering_modes:
            self.page.click_after_text("조향 반응", mode)
            time.sleep(1)

        # 4. ESC 활성화 및 팝업
        print("ESC 활성화 테스트")
        if self.page.click_text("ESC 활성화"):
            time.sleep(1)
            # 팝업 텍스트 관측 후 클릭
            if self.page.click_text("켜두기", scroll=False):
                print("ESC 켜두기 확인")
            elif self.page.click_text("끄기", scroll=False):
                print("ESC 끄기 확인")
        
        time.sleep(1)
        self.page.scroll_content_down()

        # 5. 가속 페달 모드 (크립/원페달)
        print("가속 페달 모드 변경 테스트")
        self.page.click_text("원페달 모드")
        time.sleep(1)
        self.page.click_text("크립 모드")
        time.sleep(1)

        # 6. 오토 홀드
        print("오토 홀드 토글 테스트")
        if self.page.click_text("오토 홀드"):
            time.sleep(1)
            self.page.click_text("확인", scroll=False)
            time.sleep(1)

        

    def test_driving_safety_settings(self, driver):
        """
        [시나리오] 주행 안전 설정 테스트 (텍스트 기반)
        """
        print("\n[Test] 주행 안전 설정 테스트 시작")
        
        # 전방 충돌 경고
        safety_configs = [
            ("전방 충돌 경고", ["늦게", "보통", "일찍"]),
            ("차선 이탈 경고", ["끄기", "경고만", "경고와 제어"]),
            ("사각지대 충돌 경고", ["끄기", "경고만", "경고와 제어"])
        ]
        
        for anchor, options in safety_configs:
            print(f"[{anchor}] 설정 변경 테스트")
            if self.page.click_text(anchor, scroll=True):
                for opt in options:
                    self.page.click_after_text(anchor, opt)
                    time.sleep(1)

        # 사각지대 카메라 토글
        print("사각지대 카메라 토글 테스트")
        self.page.click_text("사각지대 카메라")
        time.sleep(1)
        self.page.click_text("사각지대 카메라")

    def test_driving_parking_brake(self, driver):
        """
        [시나리오] 파킹 브레이크 롱프레스 테스트
        """
        print("\n[Test] 파킹 브레이크 롱프레스 테스트 시작")
        
        locator = (AppiumBy.XPATH, "//*[@text='파킹 브레이크']")
        if self.page.scroll_and_find(locator):
            element = self.page.find_element(locator)
            rect = element.rect
            cx = rect['x'] + rect['width'] // 2
            cy = rect['y'] + rect['height'] // 2
            
            print(f"파킹 브레이크 롱프레스 수행: ({cx}, {cy})")
            self.page.long_press_coordinates(cx, cy, duration=3000)
            time.sleep(1)

