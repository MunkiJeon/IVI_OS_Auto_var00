import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestSecurityScenario:
    """
    보안 (Security) 탭 테스트 시나리오
    - 보안 메뉴 진입 및 기본 UI 레이아웃 점검
    - 주행/주차 녹화 토글 동작 확인
    - 이벤트/상시 녹화 탭 전환 및 안내 텍스트 확인
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 보안 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        if not self.page.is_loaded():
            pytest.fail("오류: 앱이 로드되지 않았습니다.")
        
        print("보안 메뉴로 이동 중...")
        self.page.click_sidebar_menu("보안")
        time.sleep(2)
        yield

    def test_recording_toggles_flow(self, driver):
        """
        [시나리오] 주행 및 주차 녹화 토글 ON/OFF 동작 확인
        """
        print("\n[Test] 녹화 토글 동작 테스트 시작")

        print("주행 중 토글 클릭 시도 (OFF -> ON 반복)...")
        # 토글 On/Off 토글 동작 수행
        to = [(self.page.SECURITY_DRIVING_RECORDING),(self.page.SECURITY_PARKING_RECORDING)]
        for i in to:
            for j in range(2):
                self.page.toggle_tap(i, x_offset=-60, y_offset=10)
                time.sleep(1)
        
        tab_flow = [
            (self.page.SECURITY_EVENT_RECORDING, "이벤트 녹화 탭", self.page.SECURITY_PARKING_RECORDING_TEXT),
            (self.page.SECURITY_CONST_RECORDING, "상시 녹화 탭", self.page.SECURITY_PARKING_RECORDING_TEXT2),
            (self.page.SECURITY_EVENT_RECORDING, "이벤트 녹화 탭(복귀)", self.page.SECURITY_PARKING_RECORDING_TEXT)
        ]
        for locator, label, expected_text_locator in tab_flow:
            print(f"'{label}' 클릭 중...")
            self.page.click(locator)
            time.sleep(1)
            
            # 탭 전환에 따라 표시되는 안내문구가 올바른지 확인
            if self.page.is_displayed(expected_text_locator, timeout=1):
                print(f"성공: {label} 활성화 시 기대 문구가 노출됩니다.")
            else:
                self.page.toggle_tap(self.page.SECURITY_PARKING_RECORDING, x_offset=-60, y_offset=10)
                time.sleep(1)
                self.page.click(locator)
                time.sleep(1)
                if self.page.is_displayed(expected_text_locator, timeout=1):
                    print(f"성공: {label} 활성화 시 기대 문구가 노출됩니다.")
                else:
                    pytest.fail(f"오류: {label} 클릭 후 기대되는 안내 문구가 표시되지 않습니다.")

        print("보안 시나리오 테스트 완료!")
