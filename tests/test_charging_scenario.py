import pytest
import time
import random
from pages.vehicle_control_page import VehicleControlPage
from appium.webdriver.common.appiumby import AppiumBy

class TestChargingScenario:
    """
    충전 (Charging) 탭 테스트 시나리오
    - 충전 시작/커넥터 잠금 해제 버튼 및 레이아웃 점검
    - 커넥터 잠금 설정 (항상 잠금, 충전 중 잠금, 사용 안함)
    - 충전 목표 배터리량 설정 (20% ~ 100%)
    - 충전 전류 조절 (5A ~ 20A)
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 충전 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(3)
        if not self.page.is_loaded():
            pytest.fail("오류: 앱이 로드되지 않았습니다.")
        
        print("충전 메뉴로 이동 중...")
        self.page.click_sidebar_menu("충전")
        time.sleep(2)
        yield

    def test_charging_limits_flow(self, driver):
        """
        [시나리오] 충전 목표 배터리량 설정 테스트
        """
        print("\n[Test] 충전 목표 설정 테스트 시작")
        limit_configs = [
            (self.page.CHARGING_20),
            (self.page.CHARGING_40),
            (self.page.CHARGING_60),
            (self.page.CHARGING_80),
            (self.page.CHARGING_100)
        ]

        loop = 0
        for text_locator in limit_configs:
            self.page.click_grouped_button("0%",loop, 5, 852, 71, -100) 
            time.sleep(1)
            if loop == 4: # 100% 설정 시 추가 텍스트 확인
                if self.page.is_displayed(self.page.CHARGING_100_TEXT):
                    print("확인됨: 100% 권장 텍스트가 표시됩니다.")
                else:
                    pytest.fail("오류: 100% 권장 텍스트가 표시되지 않습니다.")
                    
            if self.page.is_displayed(text_locator):
                print(f"확인됨: {text_locator} ")
            else:
                pytest.fail(f"오류: {text_locator}가 표시되지 않습니다.")
            loop += 1

    def test_charging_connector_flow(self, driver):
        """
        [시나리오] 커넥터 잠금 설정 및 표시 옵션 변경
        """
        print("\n[Test] 커넥터 잠금 설정 테스트 시작")
        self.page.click(self.page.CHARGING_START)
        time.sleep(1)
        self.page.click(self.page.CHARGING_UNLOCK_CONNECTOR)
        time.sleep(1)
        self.page.click_grouped_button("충전 잔량 표시",0, 2, 652, 71) 
        time.sleep(1)
        self.page.click_grouped_button("충전 잔량 표시",1, 2, 652, 71) 
        time.sleep(1)

    def test_charging_current_flow(self, driver):
        """
        [시나리오] 충전 전류 조절 및 증감 확인
        """
        print("\n[Test] 충전 전류 조절 테스트 시작")
        self.page.scroll_content_down()
        time.sleep(2)

        # Change charging limit Offset (-5 to 5)
        target_offset = random.randint(-5, 5)
        print(f"Target Offset clicks: {target_offset}")
        
        # Determine strict direction and count
        x, y = 0, 0
        if self.page.is_displayed(self.page.CHARGING_CHARGING_MAX):
            print("charging limit is 20 => 5회 감소")
            for _ in range(5):
                # Use page defined locator for Minus
                x, y = self.page.Charging_IconBtn["MINUS"]
                self.page.tap_coordinates(x*1920, y*1080)
                time.sleep(0.5) 
        elif self.page.is_displayed(self.page.CHARGING_CHARGING_MIN):
            print("charging limit is 5 => 5회 증가")
            for _ in range(5):
                # Use page defined locator for Plus
                x, y = self.page.Charging_IconBtn["PLUS"]
                self.page.tap_coordinates(x*1920, y*1080)
                time.sleep(0.5)

        print(f"Decreasing charging limit offset by {target_offset}")
        for _ in range(abs(target_offset)):
            if target_offset < 0: x, y = self.page.Charging_IconBtn["MINUS"]
            elif target_offset > 0: x, y = self.page.Charging_IconBtn["PLUS"]
            self.page.tap_coordinates(x*1920, y*1080)
            time.sleep(0.5)
                    
    def test_connector_lock_flow(self, driver):
        """
        [시나리오] 커넥터 잠금 설정 및 옵션 확인
        """
        print("\n[Test] 커넥터 잠금 설정 테스트 시작")
        self.page.scroll_and_find(self.page.CHARGING_CONNECTOR)
        time.sleep(1)

        self.page.click_grouped_button("커넥터 잠금 설정", 0, 3, 652, 71, 20) #상시잠금 
        time.sleep(1)
        self.page.click_grouped_button("커넥터 잠금 설정", 1, 3, 652, 71, 20) #충전중잠금
        time.sleep(1)
        self.page.click_grouped_button("커넥터 잠금 설정", 2, 3, 652, 71, 20) #사용안함
        time.sleep(1)

        action_items = [
            (self.page.CHARGING_ALWAYS_LOCK, self.page.CHARGING_ALWAYS_LOCK_TEXT, "항상 잠금"),
            (self.page.CHARGING_LOCKING_CHARGING, self.page.CHARGING_LOCKING_CHARGING_TEXT, "충전 중 잠금"),
            (self.page.CHARGING_DISABLED, self.page.CHARGING_DISABLED_TEXT, "사용 안함")
        ]
        for click_locator, text_locator, label in action_items:
            print(f"'{label}' 클릭 중...")
            self.page.click(click_locator)
            time.sleep(1)
            if self.page.is_displayed(text_locator):
                print(f"확인됨: {label} 텍스트가 표시됩니다.")
            else:
                pytest.fail(f"오류: {label} 텍스트가 표시되지 않습니다.")

    