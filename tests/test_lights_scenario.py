
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage
class TestLightsScenario:
    """
    라이트 (Lights) 탭 테스트 시나리오
    - 전조등 (끄기, 자동, 미등, 켜짐)
    - 프렁크등 / 트렁크등
    - 실내등 (전체, 개별 좌석)
    - 무드 조명 (색상 변경, 저장)
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(3)
        self.page.click_sidebar_menu("라이트")
        time.sleep(1)
        yield

    def test_headlights(self, driver):
        """
        [시나리오] 전조등 설정 테스트
        - 좌표 기반 버튼 클릭 (전조등 끄기, 자동, 미등, 켜짐 등)
        """
        print("\n[Test] 전조등 설정 테스트 시작")
        
        self.page.click_grouped_button("전조등", 0, 4, 652, 71, 14) # 부드럽게
        time.sleep(1)
        self.page.click_grouped_button("전조등", 1, 4, 652, 71, 14) # 표준
        time.sleep(1)
        self.page.click_grouped_button("전조등", 2, 4, 652, 71, 14) # 빠르게
        time.sleep(1)
        self.page.click_grouped_button("전조등", 3, 4, 652, 71, 14) # 빠르게
        time.sleep(1)

        #전조등 자동
        self.page.toggle_tap(self.page.LIGHT_HEADLIGHT, x_offset=0, y_offset=150)
        time.sleep(1)
        self.page.toggle_tap(self.page.LIGHT_HEADLIGHT, x_offset=0, y_offset=150)
        time.sleep(1)
        #에스코트 조명
        self.page.toggle_tap(self.page.LIGHT_ESCOOT_LIGHT, x_offset=-60, y_offset=10)
        time.sleep(1)
        self.page.toggle_tap(self.page.LIGHT_ESCOOT_LIGHT, x_offset=-60, y_offset=10)
        time.sleep(1)

    def test_frunk_trunk_lights(self, driver):
        """
        [시나리오] 프렁크등 및 트렁크등 테스트
        - 프렁크등 (켜기/자동/끄기)
        - 트렁크등 (켜기/자동/끄기)
        """
        print("\n[Test] 프렁크/트렁크등 테스트 시작")
        
        # 프렁크등
        self.page.click_after_text("프렁크등", "켜기")
        time.sleep(1)
        self.page.click_after_text("프렁크등", "자동")
        time.sleep(1)
        self.page.click_after_text("프렁크등", "끄기")
        time.sleep(1)

        # 트렁크등
        self.page.click_after_text("트렁크등", "켜기")
        time.sleep(1)
        self.page.click_after_text("트렁크등", "자동")
        time.sleep(1)
        self.page.click_after_text("트렁크등", "끄기")
        time.sleep(1)

    def test_interior_lights(self, driver):
        """
        [시나리오] 실내등 테스트
        - 하단 스크롤 후 실내등 메뉴 접근
        - 전체 끄기, 개별 좌석 제어 테스트
        """
        print("\n[Test] 실내등 테스트 시작")
        
        # 스크롤하여 실내등 섹션으로 이동
        if not self.page.scroll_and_find(self.page.LIGHT_INTERIOR_ALL_SEATS):
            pytest.fail("실내등 메뉴를 찾을 수 없습니다.")

        # 개별 좌석 토글
        seats = [
            self.page.LIGHT_INTERIOR_ALL_OFF,
            self.page.LIGHT_INTERIOR_DRIVER,
            self.page.LIGHT_INTERIOR_PASSENGER,
            self.page.LIGHT_INTERIOR_REAR_LEFT,
            self.page.LIGHT_INTERIOR_REAR_RIGHT,
            self.page.LIGHT_INTERIOR_ALL_SEATS,
            self.page.LIGHT_INTERIOR_ALL_OFF,
        ]
        
        for seat in seats:
            if not self.page.scroll_and_find(seat):
                pytest.fail(f"{seat}를 찾을 수 없습니다.")
            else:
                print(f"{seat} 클릭.")
                self.page.click(seat)
                time.sleep(1)

    def test_mood_lights(self, driver):
        """
        [시나리오] 무드 조명 테스트
        - 무드 조명 켜기
        - 색상 설정 팝업 진입
        - 색상 선택 및 저장
        """
        print("\n[Test] 무드 조명 테스트 시작")
        
        # 스크롤하여 무드 조명으로 이동
        if not self.page.scroll_and_find(self.page.LIGHT_MOOD_ON):
            pytest.fail("무드 조명 메뉴를 찾을 수 없습니다.")
            
        # 무드 조명 켜기
        self.page.click_after_text("무드 조명", "끄기")
        time.sleep(1)
        self.page.click_after_text("무드 조명", "자동")
        time.sleep(1)
        self.page.click_after_text("무드 조명", "켜기")
        time.sleep(1)

        # 조명 밝기 변경

        sw_rect = driver.find_element(*self.page.LIGHT_MOOD_COLOR).rect
        target_x = sw_rect['x'] + sw_rect['width']
        target_y = sw_rect['y'] + sw_rect['height']//2
        print(f"Found {self.page.LIGHT_MOOD_COLOR} at {sw_rect}. \nTapping at ({target_x}, {target_y})")

        self.page.random_area_interaction(target_x + 160, target_y, target_x + 480, target_y, interaction_type='drag')
        time.sleep(1)
        com = 120
        for i in range(2):
            for j in range(3):
                self.page.tap_coordinates(x=target_x + com, y=target_y) #밝기 감소
                if com == 120: print("밝기 감소") 
                elif com == 520: print("밝기 증가")
                time.sleep(1)
            com += 400

        self.page.tap_coordinates(x=target_x + 520, y=target_y) #밝기 증가_10@
        print("밝기 증가")
        time.sleep(1)

        # 색상 설정 진입
        if not self.page.scroll_and_find(self.page.LIGHT_MOOD_COLOR):
            pytest.fail("무드 조명 색상 버튼을 찾을 수 없습니다.")
            
        print("색상 설정 진입...")
        self.page.click(self.page.LIGHT_MOOD_COLOR)
        time.sleep(1)
        
        # 색상 휠 영역에서 랜덤 인터랙션 (탭 또는 드래그)
        print("색상 휠 영역에서 랜덤 인터랙션 수행...")
        self.page.random_area_interaction(1050, 255, 1485, 590, interaction_type='drag')
        time.sleep(1)
        self.page.random_area_interaction(1050, 695, 1485, 695, interaction_type='drag')
        time.sleep(1)

        # 저장
        print("저장 버튼 클릭...")
        self.page.click(self.page.LIGHT_MOOD_SAVE_BTN)
        time.sleep(1)
        
