import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestNavigationScenario:
    """
    내비게이션 (Navigation) 탭 테스트 시나리오
    - 내비게이션 상/하단 레이아웃 및 버튼 점검
    - EV 경로 탐색 스위치 토글 동작 확인
    - 내비게이션 초기화 팝업 동작 확인 (열기/닫기/수행)
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 내비게이션 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(3)
        if not self.page.is_loaded():
            pytest.fail("오류: 앱이 로드되지 않았습니다.")
        
        print("내비게이션 메뉴로 이동 중...")
        self.page.click_sidebar_menu("내비게이션")
        time.sleep(2)

        self.toggles = [
            self.page.NAV_EV_ROUTE,
            self.page.NAV_AVOID_TOLLS,
            self.page.NAV_AVOID_SCHOOL_ZONES,
            self.page.NAV_VOICE_GUIDANCE,
            self.page.NAV_NOTIFICATIONS_SOUND,
            self.page.NAV_OVERSPEED_WARNING_SOUND,
        ]
        yield

    def test_ev_route_switch_flow(self, driver):
        """
        [시나리오] EV 경로 탐색 스위치 토글 동작 확인
        """
        print("\n[Test] EV 경로 탐색 스위치 테스트 시작")
        
        # EV 스위치 클릭 및 상태 확인
        self.page.scroll_content_down()
        print("EV 스위치 클릭 중...")
        for i in self.toggles:
            self.page.scroll_and_find(i)
            self.page.toggle_tap(i,x_offset=-40, y_offset=20)
            time.sleep(1)
            self.page.toggle_tap(i,x_offset=-40, y_offset=20)
            time.sleep(1)


    def test_initialize_popup_flow(self, driver):
        """
        [시나리오] 내비게이션 초기화 팝업 동작 확인
        """
        print("\n[Test] 내비게이션 초기화 팝업 테스트 시작")
        
        # 아래로 스크롤
        print("아래로 스크롤 중...")
        self.page.scroll_and_find(self.page.NAV_DATA)
        self.page.scroll_content_down() 
        time.sleep(2)

        # 초기화 버튼 클릭 (팝업 열기)
        print("Clear Search History 초기화")
        self.page.click_after_text("Clear Search History", "초기화")
        time.sleep(1)
        self.page.click(self.page.NAV_POPUP_BUTTON)
        time.sleep(1)

        print("Clear Driving History 초기화")
        self.page.click_after_text("Clear Driving History", "초기화")
        time.sleep(1)
        self.page.click(self.page.NAV_POPUP_BUTTON)
        time.sleep(1)

        print("Delete All Data 초기화")
        self.page.click_after_text("Delete All Data", "초기화")
        time.sleep(1)
        self.page.click(self.page.NAV_POPUP_BUTTON)
        time.sleep(1)
    
        print("내비게이션 시나리오 테스트 완료")
