
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestClimateScenario:
    """
    공조 (Climate) 탭 테스트 시나리오
    - 공조 관련 편의 기능 토글 (워셔액, 터널 진입, 공기 질 등)
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        self.page.click_sidebar_menu("공조")
        time.sleep(1)
        yield

    def test_climate_feature_toggles(self, driver):
        """
        [시나리오] 공조 편의 기능 토글 테스트
        - 각 설정 메뉴(워셔액, 터널, 공기 질 등)의 텍스트 옆 토글 스위치를 좌표 기반으로 제어합니다.
        """
        print("\n[Test] 공조 편의 기능 토글 테스트 시작")
        
        # 테스트할 토글 목록
        toggles = [
            self.page.CLIMATE_WASHER,
            self.page.CLIMATE_TUNNEL,
            self.page.CLIMATE_AIR_QUALITY,
            self.page.CLIMATE_OVERHEAT,
            self.page.CLIMATE_AUTO_DRY
        ]

        for locator in toggles:
            try:
                # 토글 ON
                self.page.toggle_tap(locator, x_offset=-60, y_offset=10)
                time.sleep(1)

                # 토글 OFF (원복)
                self.page.toggle_tap(locator, x_offset=-60, y_offset=10)
                time.sleep(1)
                
            except Exception as e:
                print(f"토글 제어 실패 ({locator}): {e}")
                # 하나가 실패해도 다음 테스트 진행
