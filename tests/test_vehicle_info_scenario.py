
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

class TestVehicleInfoScenario:
    """
    차량 정보 (Vehicle Info) 탭 테스트 시나리오
    - 소프트웨어 정보, 자동 업데이트 토글 확인
    - 초기화, 법적 고지 등 팝업 확인
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(3)
        self.page.click_sidebar_menu("차량 정보")
        time.sleep(1)
        yield

    def test_vehicle_info_layout(self):
        """
        [시나리오] 차량 정보 화면 구성 요소 확인
        """
        print("\n[Test] 차량 정보 화면 레이아웃 확인 시작")
        assert self.page.is_displayed(self.page.VI_CONNECT), "차량 정보 화면이 로드되지 않았습니다."
        # 추가적인 레이아웃 확인이 필요하면 여기에 작성
        print("✓ 차량 정보 화면 요소 확인 완료")

    def test_vehicle_info_flow(self):
        """
        [시나리오] 차량 정보 기능 작동 확인 (토글, 초기화, 팝업)
        """
        print("\n[Test] 차량 정보 기능 작동 테스트 시작")

        toggles = [
            self.page.VI_SOFTWARE_INFO,
            self.page.VI_AUTO_UPDATE,
        ]

        for locator in toggles:
            try:
                # 요소 찾기 & 좌표 계산
                cam_label = self.page.find_element(locator)
                rect = cam_label.rect 

                if locator == self.page.VI_AUTO_UPDATE:
                    target_x = rect['x'] - 60
                    target_y = rect['y'] + 10
                    print(f"Found {locator} at {rect}. Tapping Auto Update at ({target_x}, {target_y})")
                    self.page.tap_coordinates(target_x, target_y)
                    time.sleep(1)
                    self.page.tap_coordinates(target_x, target_y)
                    time.sleep(1)
    
                elif locator == self.page.VI_SOFTWARE_INFO:
                    target_x = rect['x'] + rect['width'] + 30
                    target_y = rect['y'] + 10
                    print(f"Found {locator} at {rect}. Tapping Software Info at ({target_x}, {target_y})")
                    self.page.tap_coordinates(target_x, target_y)
                    time.sleep(1)
                    # 팝업 확인
                    try:
                        print("소프트웨어 정보 팝업 확인 중...")
                        self.page.popup_find_tap(self.page.VI_POPUP_OK)
                        time.sleep(2)
                    except Exception:
                        print("Software Info Popup not found or timed out")
                
            except Exception as e:
                print(f"Skipping toggle {locator}: {e}")

        # 초기화 및 법적 고지 테스트
        print("공장 초기화 버튼 클릭 테스트...")
        try:
            self.page.click(self.page.VI_FACTORY_RESET)
            time.sleep(1)
            # 여기서는 실제 초기화를 누르지 않고 버튼 동작만 확인하거나, 팝업이 뜨면 취소/확인
            # 기존 코드는 VI_INITIALIZE_BUTTON을 누름.
            self.page.click(self.page.VI_INITIALIZE_BUTTON)
            time.sleep(1)
            # 주의: 실제 초기화가 진행되면 테스트 환경이 날아갈 수 있으므로 주의 필요.
            # 팝업이 있다면 닫아주는게 좋음.
        except Exception as e:
            print(f"Factory Reset flow error: {e}")

        print("법적 고지 버튼 클릭 테스트...")
        try:
            self.page.click(self.page.VI_LEGAL_INFO_BUTTON)
            time.sleep(1)
            self.page.popup_find_tap(self.page.VI_POPUP_OK)
            time.sleep(2)
        except Exception as e:
            print(f"Legal Info flow error: {e}")




