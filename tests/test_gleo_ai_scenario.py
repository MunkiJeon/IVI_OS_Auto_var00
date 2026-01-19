import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

class TestGleoAIScenario:
    """
    Gleo AI 시나리오 테스트 클래스
    - Gleo AI 레이아웃 및 상/하단 요소 점검
    - 음성 타입 선택 동작 확인
    - Gleo Calling 활성화 팝업 및 토글 동작 확인
    - 스타일 및 좌석 제어 설정 확인
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 Gleo AI 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        if not self.page.is_loaded():
            pytest.fail("오류: 앱이 로드되지 않았습니다.")
        
        print("Gleo AI 메뉴로 이동 중...")
        self.page.click_sidebar_menu("Gleo AI")
        time.sleep(2)
        yield

    def test_voice_types_flow(self, driver):
        """
        [시나리오] 음성 타입(1~6) 선택 동작 확인
        """
        print("\n[Test] 음성 타입 선택 테스트 시작")
        
        # 음성 타입 1~6 클릭 테스트
        for i in range(1, 7):
            print(f"음성 타입 {i} 클릭 중...")
            locator = getattr(self.page, f"GLEO_VOICE_{i}")
            self.page.click(locator)
            time.sleep(1)

        # 초기 상태(음성 타입 1)로 복귀
        print("음성 타입 1로 복귀 클릭 중...")
        self.page.click(self.page.GLEO_VOICE_1)
        time.sleep(1)

    def test_gleo_calling_popup_flow(self, driver):
        """
        [시나리오] Gleo Calling 팝업 및 활성화 토글 동작 확인
        """
        print("\n[Test] Gleo Calling 팝업 테스트 시작")

        # 바로 대화 시작 토글 확인
        if self.page.is_displayed(self.page.GLEO_START):
            print("바로 대화 시작 토글 확인")
            self.page.toggle_tap(self.page.GLEO_START, x_offset=-60, y_offset=10)
            time.sleep(1)
            self.page.toggle_tap(self.page.GLEO_START, x_offset=-60, y_offset=10)
            time.sleep(1)
        else:
            print("글레오 호출 활성화")
            self.page.toggle_tap(self.page.GLEO_CALLING, x_offset=-60, y_offset=10)
            time.sleep(1)
            self.page.popup_find_tap(self.page.GLEO_CALLING_POPUP_ENABLE)
            time.sleep(1)
            print("바로 대화 시작 토글 확인")
            self.page.toggle_tap(self.page.GLEO_START, x_offset=-60, y_offset=10)
            time.sleep(1)
            self.page.toggle_tap(self.page.GLEO_START, x_offset=-60, y_offset=10)
            time.sleep(1)
            
        print("글레오 호출 비활성화")
        self.page.toggle_tap(self.page.GLEO_CALLING, x_offset=-60, y_offset=10)
        time.sleep(1)
        
        # "글레오"호출 활성화 팝업 동작 확인
        print("글레오 호출 활성화 팝업 확인")
        self.page.toggle_tap(self.page.GLEO_CALLING, x_offset=-60, y_offset=10)
        time.sleep(1)
        self.page.popup_find_tap(self.page.GLEO_CALLING_POPUP_CANCEL)
        time.sleep(1)
        self.page.toggle_tap(self.page.GLEO_CALLING, x_offset=-60, y_offset=10)
        time.sleep(1)
        self.page.popup_find_tap(self.page.GLEO_CALLING_POPUP_ENABLE)
        time.sleep(1)

        # 연속 대화 토글 확인
        print("연속 대화 토글 확인")
        self.page.toggle_tap(self.page.GLEO_CONTINUOUS, x_offset=-60, y_offset=10)
        time.sleep(1)
        self.page.toggle_tap(self.page.GLEO_CONTINUOUS, x_offset=-60, y_offset=10)
        time.sleep(1)

    def test_style_and_seats_flow(self, driver):
        """
        [시나리오] 스타일(정중함/친근함) 및 좌석 설정 동작 확인
        """
        print("\n[Test] 스타일 및 좌석 설정 테스트 시작")
        
        # 아래로 스크롤하여 영역 확보
        print("아래로 스크롤 중...")
        self.page.scroll_content_down()
        time.sleep(2)

        # 스타일 버튼 클릭 테스트
        print("스타일 버튼(정중한/친근한) 클릭 테스트 중...")
        style_locators = [
                self.page.GLEO_POLITE,
                self.page.GLEO_FRIENDLY,
                self.page.GLEO_POLITE,
            ]
        for locator in style_locators:
            try:
                print(f"{locator} 클릭...")
                self.page.toggle_tap(locator, x_offset=10, y_offset=10)
                time.sleep(5)
            except Exception as e:
                print(f"스타일 버튼 클릭 실패 {locator}: {e}")

        # 좌석 버튼 클릭 테스트
        print("좌석 버튼(조수석/뒷좌석) 클릭 테스트 중...")
        seat_locators = [
                self.page.GLEO_PASSENGER,
                self.page.GLEO_REAR_LEFT,
                self.page.GLEO_REAR_RIGHT,
            ]
        for locator in seat_locators:
            try:
                print(f"{locator} 클릭(On/Off)...")
                self.page.toggle_tap(locator, x_offset=10, y_offset=10)
                time.sleep(1)
                self.page.toggle_tap(locator, x_offset=10, y_offset=10)
                time.sleep(1)
            except Exception as e:
                print(f"좌석 버튼 클릭 실패 {locator}: {e}")

        print("Gleo AI 시나리오 테스트 완료!")

