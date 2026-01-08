
import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestPrivacyScenario:
    """
    개인정보 보호 토글 테스트
    """
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        self.page.click_sidebar_menu("개인정보 보호")
        time.sleep(1)
        self.toggles = [
            self.page.PRIVACY_MIC_USAGE,
            self.page.PRIVACY_LOCATION_USAGE,
            self.page.PRIVACY_CAMERA_USAGE
        ]
        yield

    def test_mic_usage(self, driver):
        """
        [시나리오] 마이크 사용 토글 테스트
        """
        print("\n[Test] 마이크 사용 토글 테스트 시작")
        try:
            # 토글 OFF, 팝업
            self.page.toggle_tap(self.toggles[0], x_offset=-60, y_offset=10)
            print("마이크 사용 토글 OFF")
            time.sleep(1)
            # 팝업 취소
            self.page.popup_find_tap(self.page.PRIVACY_CANCEL_BUTTON)
            print("팝업 취소")
            time.sleep(1)
            # 토글 OFF, 팝업
            self.page.toggle_tap(self.toggles[0], x_offset=-60, y_offset=10)
            print("마이크 사용 토글 OFF")
            time.sleep(1)
            # 팝업 차단
            self.page.popup_find_tap(self.page.PRIVACY_BLOCK_BUTTON)
            print("팝업 차단")
            time.sleep(1)
        except Exception as e:
            print(f"마이크 사용 토글 테스트 실패: {e}")
            raise

    def test_location_usage(self, driver):
        """
        [시나리오] 위치 사용 토글 테스트
        """
        print("\n[Test] 위치 사용 토글 테스트 시작")
        try:
            # 토글 OFF, 팝업
            self.page.toggle_tap(self.toggles[1], x_offset=-60, y_offset=10)
            print("위치 사용 토글 OFF")
            time.sleep(1)
            # 팝업 취소
            self.page.popup_find_tap(self.page.PRIVACY_CANCEL_BUTTON)
            print("팝업 취소")
            time.sleep(1)
            # 토글 OFF, 팝업
            self.page.toggle_tap(self.toggles[1], x_offset=-60, y_offset=10)
            print("위치 사용 토글 OFF")
            time.sleep(1)
            # 팝업 차단
            self.page.popup_find_tap(self.page.PRIVACY_BLOCK_BUTTON)
            print("팝업 차단")
            time.sleep(1)
        except Exception as e:
            print(f"위치 사용 토글 테스트 실패: {e}")
            raise

    def test_camera_usage(self, driver):
        """
        [시나리오] 카메라 사용 토글 테스트
        """
        print("\n[Test] 카메라 사용 토글 테스트 시작")
        try:
            # 토글 OFF, 팝업
            self.page.toggle_tap(self.toggles[2], x_offset=-60, y_offset=10)
            print("카메라 사용 토글 OFF")
            time.sleep(1)
            # 팝업 취소
            self.page.popup_find_tap(self.page.PRIVACY_CANCEL_BUTTON)
            print("팝업 취소")
            time.sleep(1)
            # 토글 OFF, 팝업
            self.page.toggle_tap(self.toggles[2], x_offset=-60, y_offset=10)
            print("카메라 사용 토글 OFF")
            time.sleep(1)
            # 팝업 차단
            self.page.popup_find_tap(self.page.PRIVACY_BLOCK_BUTTON)
            print("팝업 차단")
            time.sleep(1)
        except Exception as e:
            print(f"카메라 사용 토글 테스트 실패: {e}")
            raise

    def test_use_reset(self, driver):
        """
        [시나리오] 테스트 후 초기화 
        """
        print("\n[Test] 테스트 후 초기화 시작")
        try:
            for toggle in self.toggles:
                self.page.toggle_tap(toggle, x_offset=-60, y_offset=10)
                time.sleep(1)

            if self.page.is_displayed(self.page.PRIVACY_CANCEL_BUTTON):
                self.page.popup_find_tap(self.page.PRIVACY_CANCEL_BUTTON)
                print("팝업 취소")
                time.sleep(1)
        except Exception as e:
            print(f"테스트 후 초기화 실패: {e}")
            raise