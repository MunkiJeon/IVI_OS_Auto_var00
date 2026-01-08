
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage
from selenium.common.exceptions import NoSuchElementException

class TestSeatScenario:
    """
    시트 포지션 (Seat Position) 탭 테스트 시나리오
    - 시트 부위별 선택 (운전석, 콘솔, 동승석 등)
    - 시트 편의 미세 조절 (운전대 등)
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(3)
        self.page.click_sidebar_menu("시트 포지션")
        time.sleep(2)
        yield

    def test_seat_part_selection(self, driver):
        """
        [시나리오] 시트 부위별 선택 테스트
        - 편안한 승차 아이콘 클릭
        - 차량 이미지 위의 각 시트 부위(콘솔, 동승석, 뒷좌석 등)를 좌표로 탭하여 선택
        """
        print("\n[Test] 시트 부위 선택 테스트 시작")
        
        # '편안한 승차' 모드 토글
        rx, ry = self.page.SEAT_IconBtn["COMFORTABLE_RIDE"]
        # Screen size assumption 1920x1080 (or fetch)
        x = int(1920 * rx)
        y = int(1080 * ry)
        
        print(f"'편안한 승차' 토글 (좌표: {x}, {y})...")
        self.page.tap_coordinates(x, y)
        time.sleep(1)
        self.page.tap_coordinates(x, y) # 원복
        time.sleep(1)

        # 시트 부위 순차 선택
        sequence = [
            "이동식 콘솔",
            "동승석",
            "뒷좌석 우측",
            "뒷좌석 좌측",
            "운전석"
        ]
        
        for target_name in sequence:
            print(f"'{target_name}' 선택 시도...")
            if target_name not in self.page.SEAT_TOUCH_POINTS:
                print(f"경고: {target_name} 좌표가 정의되지 않음")
                continue
                
            rx, ry = self.page.SEAT_TOUCH_POINTS[target_name]
            x = int(1920 * rx)
            y = int(1080 * ry)
            
            print(f"좌표 탭: ({x}, {y})")
            self.page.tap_coordinates(x, y)
            time.sleep(1) 

    def test_seat_detail_adjustment(self, driver):
        """
        [시나리오] 시트 상세 조절 테스트 (운전대)
        - 스크롤하여 하단 메뉴 확인
        - '운전대' 메뉴 진입 및 저장 팝업 확인
        """
        print("\n[Test] 시트 상세 조절(운전대) 테스트 시작")
        
        # 운전대 메뉴 찾기 (스크롤)
        if not self.page.scroll_and_find(self.page.SEAT_HANDLE):
            pytest.fail("운전대 설정을 찾을 수 없습니다.")

        print("'운전대' 메뉴 클릭...")
        self.page.click(self.page.SEAT_HANDLE)
        time.sleep(1)

        try:
            popup_save = self.page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
            popup_save.click()
            print("설정 저장 팝업 확인")
        except NoSuchElementException:
            print("저장 팝업 없음 (설정이 변경되지 않았거나 이미 저장됨)")
            
