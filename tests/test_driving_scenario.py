
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
        self.page.click_sidebar_menu("주행")
        time.sleep(1)
        self.toggles = [
            self.page.DRIVING_SNOW_RAIN_ASSIST,
            self.page.DRIVING_ESC,
            self.page.DRIVING_AUTO_HOLD,
            self.page.DRIVING_BLIND_SPOT_CAMERA,
        ]
        yield

    def test_driving_convenience_toggles(self, driver):
        """
        [시나리오] 주행 편의 기능 토글 및 모드 변경
        1. 가속 페달 모드 변경 (부드럽게, 표준, 빠르게)
        2. 눈/빗길 보조 모드 토글 (좌표 기반 Tap)
        3. 스티어링 모드 변경
        4. ESC 토글 및 팝업 확인
        5. 크립 모드 / 원페달 모드 전환
        6. 오토 홀드 토글 및 팝업 확인
        """
        print("\n[Test] 주행 편의 기능 테스트 시작")
        
        # 가속 페달 모드 (Group Click 사용)
        # 가계산 규격: 가로 652, 세로 71, 간격 14
        for i in range(3):
            self.page.click_grouped_button("가속 모드", i, 3, 652, 71, 14)
            time.sleep(1)

        # 눈/빗길 보조 모드 (좌표 Tap)
        for i in range(2):
            self.page.toggle_tap(self.toggles[0], x_offset=-60, y_offset=10)
            time.sleep(1)
        
        # 조향 반응 (Relative Click 사용)
        for i in range(2):
            self.page.click_after_text("조향 반응", "표준" if i == 0 else "가볍게")
            time.sleep(1)

        # ESC 토글
        for i in range(2):
            self.page.toggle_tap(self.toggles[1], x_offset=-60, y_offset=10)
            time.sleep(1)


        self.page.popup_find_tap(self.page.DRIVING_ESC_POPUP_ON_BUTTON)
        time.sleep(1)
        self.page.toggle_tap(self.toggles[1], x_offset=-60, y_offset=10)
        time.sleep(1)
        self.page.popup_find_tap(self.page.DRIVING_ESC_POPUP_OFF_BUTTON)
        time.sleep(1)

        self.page.scroll_content_down()
        # 크립 모드 / 원페달 모드
        if not self.page.scroll_and_find(self.page.DRIVING_ACCEL_PEDAL_MODE):
             pytest.fail("가속 페달 모드 메뉴를 찾을 수 없습니다.")
        
        self.page.click_after_text("가속 페달 모드", "원페달 모드")
        time.sleep(1)
        self.page.click_after_text("가속 페달 모드", "크립 모드")
        time.sleep(1)

        # 오토 홀드
        self.page.toggle_tap(self.toggles[2], x_offset=-60, y_offset=10)
        time.sleep(1)
        if self.page.is_displayed(self.page.DRIVING_AUTO_HOLD_CONFIRM_BUTTON):
            try:
                self.page.popup_find_tap(self.page.DRIVING_AUTO_HOLD_CONFIRM_BUTTON)
                time.sleep(1)
            except NoSuchElementException:
                print("오토 홀드 팝업 없음")
        else:
            self.page.toggle_tap(self.toggles[2], x_offset=-60, y_offset=10)
            time.sleep(1)
            try:
                self.page.popup_find_tap(self.page.DRIVING_AUTO_HOLD_CONFIRM_BUTTON)
                time.sleep(1)
            except NoSuchElementException:
                print("오토 홀드 팝업 없음")

        

    def test_driving_safety_settings(self, driver):
        """
        [시나리오] 주행 안전 설정 테스트
        1. 전방 충돌 경고 모드 (늦게/보통/일찍)
        2. 차선 이탈 경고 모드 (끄기/경고만/경고와 제어)
        3. 사각지대 충돌 경고 모드 (끄기/경고만/경고와 제어)
        """
        print("\n[Test] 주행 안전 설정 테스트 시작")
        
        # 전방 충돌 경고 (Relative Click 사용)
        if not self.page.scroll_and_find(self.page.DRIVING_FORWARD_COLLISION_WARNING):
             pytest.fail("전방 충돌 경고 메뉴를 찾을 수 없습니다.")
        
        for i in range(3):
            self.page.click_after_text("전방 충돌 경고", "늦게" if i == 0 else "보통" if i == 1 else "일찍")
            time.sleep(1)
        time.sleep(1)
        
        # 차선 이탈 경고 (Relative Click 사용)
        if not self.page.scroll_and_find(self.page.DRIVING_LANE_DEPARTURE_WARNING):
             pytest.fail("차선 이탈 경고 메뉴를 찾을 수 없습니다.")
        
        for i in range(3):
            self.page.click_after_text("차선 이탈 경고", "끄기" if i == 0 else "경고만" if i == 1 else "경고와 제어")
            time.sleep(1)

        # 사각지대 충돌 경고 (Relative Click 사용)
        if not self.page.scroll_and_find(self.page.DRIVING_BLIND_SPOT_COLLISION_WARNING):
             pytest.fail("사각지대 충돌 경고 메뉴를 찾을 수 없습니다.")
        
        for i in range(3):
            self.page.click_after_text("사각지대 충돌 경고", "끄기" if i == 0 else "경고만" if i == 1 else "경고와 제어")
            time.sleep(1)

        """
        [시나리오] 사각지대 화면(카메라) 토글 테스트
        - '사각지대 카메라' 텍스트 레이블을 기준으로 상대 좌표를 계산하여 토글 스위치를 클릭합니다.
        """
        print("\n[Test] 사각지대 카메라 토글 테스트 시작")
        
        # 가장 아래쪽일 수 있으므로 스크롤
        if not self.page.scroll_and_find(self.page.DRIVING_BLIND_SPOT_CAMERA):
             pytest.fail("사각지대 카메라 버튼을 찾을 수 없습니다.")
        
        for i in range(2):
            self.page.toggle_tap(self.toggles[3], x_offset=-60, y_offset=10)
            time.sleep(1)

    def test_driving_parking_brake(self, driver):
        """
        [시나리오] 전자식 파킹 브레이크 테스트
        - 파킹 브레이크 버튼을 2초간 롱프레스(Long Press)합니다.
        """
        print("\n[Test] 파킹 브레이크 롱프레스 테스트 시작")
        
        if not self.page.scroll_and_find(self.page.DRIVING_EPB_BTN):
             pytest.fail("파킹 브레이크 버튼을 찾을 수 없습니다.")
        
        print("파킹 브레이크 버튼 롱프레스 수행 (2초)...")
        # BasePage의 common method 활용 가능하지만, 2초 delay 명시를 위해 직접 호출하거나
        # BasePage에 long_press(duration) 추가된 것을 사용
        self.page.long_press_element(self.page.DRIVING_EPB_BTN, duration=2000)
        print("롱프레스 완료")
        time.sleep(1)
