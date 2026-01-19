import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestDisplayScenario:
    """
    화면 (Display) 탭 테스트 시나리오
    - 화면 레이아웃 및 상/하단 버튼 점검
    - 테마 설정 (자동/밝게/어둡게) 상호작용 확인
    - 밝기 조절 (스와이프/버튼) 및 자동 밝기 토글 확인
    - 화면 닦기 모드 진입 및 종료 (단일 클릭 vs 롱클릭) 확인
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 화면 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        if not self.page.is_loaded():
            pytest.fail("오류: 앱이 로드되지 않았습니다.")
        
        print("화면(Display) 메뉴로 이동 중...")
        self.page.click_sidebar_menu("화면")
        time.sleep(2)
        yield

    def test_theme_interactions_flow(self, driver):
        """
        [시나리오] 테마 설정(자동/밝게/어둡게) 상호작용 확인
        """
        print("\n[Test] 테마 설정 상호작용 테스트 시작")
    

        # 자동 테마 토글 2회 반복
        for i in range(2):
            self.page.toggle_tap(self.page.DIS_AUTO_TEXT, x_offset=-60, y_offset=-20)
            time.sleep(1)

        # 밝게/어둡게 모드 전환 테스트
            menu = [
                self.page.DIS_LIGHT,
                self.page.DIS_DARK,
                self.page.DIS_LIGHT,
        ]
            for locator in menu:
                try:
                    self.page.toggle_tap(locator, x_offset=-65, y_offset=10)
                    time.sleep(1)
                except Exception as e:
                    print(f"메뉴 클릭 건너뜀 {locator}: {e}")

    def test_brightness_adjustments_flow(self, driver):
        """
        [시나리오] 밝기 조절(스와이프 및 버튼) 동작 확인
        """
        print("\n[Test] 밝기 조절 테스트 시작")
        
        # 아래로 스크롤하여 밝기 영역 확보
        print("아래로 스크롤 중...")
        self.page.scroll_content_down()
        time.sleep(2)
        BIR = 0
        BIR2 = 20

        # 밝기 스와이프 테스트
        print("밝기 높이기 (우측 스와이프)...")
        self.page.swipe(0.579*1920, 0.463*1080, 0.805*1920, 0.463*1080, 1000)
        time.sleep(1)
        
        print("밝기 낮추기 (좌측 스와이프)...")
        self.page.swipe(0.787*1920, 0.463*1080, 0.550*1920, 0.463*1080, 1000)  
        time.sleep(1)

        # 밝기 조절 버튼 테스트 (+/-)
        print("밝기 조절 버튼 (+/-) 클릭 테스트 중...")
        button = [
            self.page.DIS_IconBtn["DIS_UP"],
            self.page.DIS_IconBtn["DIS_DOWN"],
        ]
        for locator in button:
            try:
                for i in range(10):
                    x, y = locator
                    self.page.tap_coordinates(x*1920, y*1080)
                    BIR += 1
                    BIR2 -= 1
                    # 로그 출력 (한국어로 변경하지 않고 포맷 유지하되 내용은 식별 가능)
                    if BIR <= 10:
                        print(f"밝기 조절 중 (Up): {BIR}")
                    else:
                        print(f"밝기 조절 중 (Down): {BIR2}")
                    time.sleep(0.5)
            except Exception as e:
                print(f"버튼 클릭 건너뜀 {locator}: {e}")  

        # 밝기 자동 조절 토글 테스트
        print("밝기 자동 조절 토글 테스트 중...")
        for i in range(1, 3):
            self.page.toggle_tap(self.page.DIS_BRIGHTNESS_AUTO_TEXT, x_offset=-60, y_offset=-20)
            time.sleep(1)

    def test_cleaning_mode_flow(self, driver):
        """
        [시나리오] 화면 닦기 모드 진입 및 종료 로직 확인
        """
        print("\n[Test] 화면 닦기 모드 테스트 시작")
        
        # 스크롤 다운 상태 유지
        print("아래로 스크롤 중...")
        self.page.scroll_content_down()
        time.sleep(2)
        print("화면 닦기 모드 버튼 클릭...")
        self.page.click(self.page.DIS_CLEENING_MODE)
        time.sleep(2)


        # 종료 버튼 짧게 클릭 (종료 방지 확인)
        print("종료 버튼 짧게 클릭 (종료 방지 테스트)...")
        self.page.click(self.page.DIS_CLEENING_MODE_END)
        time.sleep(2)

    
        # 종료 버튼 길게 클릭 (3.5초, 실제 종료 확인)
        print("종료 버튼 길게 클릭 (3.5초) 시작...")
        self.page.long_press_element(self.page.DIS_CLEENING_MODE_END, duration=2000)
        
        # 좌표 기반 롱프레스 사용 (Overlay 요소 호환성 문제 해결)
        if "DIS_CLEENING_MODE_END" in self.page.DIS_IconBtn:
            x_ratio, y_ratio = self.page.DIS_IconBtn["DIS_CLEENING_MODE_END"]
            # 해상도 하드코딩 대신 driver window size 사용 권장되지만, 여기선 기존 패턴(1920x1080) 따름
            # 필요시 self.page.driver.get_window_size() 사용 가능
            target_x = x_ratio * 1920
            target_y = y_ratio * 1080
            print(f"좌표 기반 롱프레스 실행: ({target_x}, {target_y})")
            self.page.long_press_coordinates(target_x, target_y, duration=3500)
        else:
            # Fallback
            self.page.long_press_element(self.page.DIS_CLEENING_MODE_END, duration=3500)

        time.sleep(1)

        print("화면(Display) 시나리오 테스트 완료!")

