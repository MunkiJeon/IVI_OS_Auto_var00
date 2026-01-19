import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestConvenienceScenario:
    """
    편의 기능 (Convenience) 탭 테스트 시나리오
    - 편의 기능 메뉴 레이아웃 (상/하단) 점검
    - 각 모드(세차, 캠핑, 애완동물, 이중주차, 견인, 스탠바이) 진입 및 팝업 동작 확인
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 편의 기능 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        self.page.click_sidebar_menu("편의 기능")
        time.sleep(1)
        self.toggles = [
            self.page.CONVENIENCE_CAR_WASH_MODE,        # 세차 모드
            self.page.CONVENIENCE_VALET_MODE,           # 발렛 모드
            self.page.CONVENIENCE_CAMPING_MODE,          # 캠핑 모드
            self.page.CONVENIENCE_PET_CARE_MODE,         # 펫 케어 모드
            self.page.CONVENIENCE_DOUBLE_PARKING_MODE,   # 이중 주차 모드
            self.page.CONVENIENCE_TOWING_MODE,           # 견인 모드
        ]
        yield

    def test_car_wash_mode_flow(self, driver):
        """
        [시나리오] 각 모드 진입 및 팝업 동작 확인
        """
        print("[Test] 편의 기능 테스트 시작")
        print(type(self.page.CONVENIENCE_CAR_WASH_MODE))

        for toggle in self.toggles:
            print(f"[Test] {self.page.title_split(toggle)} 기능 테스트 시작")
            self.page.toggle_tap(toggle, x_offset=100, y_offset=150)
            time.sleep(1)

            if(toggle == self.page.CONVENIENCE_CAR_WASH_MODE):
                for i in range(2):
                    self.page.toggle_tap(self.page.CONVENIENCE_CAR_WASH_MODE_POPUP_NEURAL, x_offset=-60, y_offset=10)
                    time.sleep(1)
            elif(toggle == self.page.CONVENIENCE_VALET_MODE): # 현재 발레 모드 비활성화로 팝업이 뜨지 않음
                print("발렛 모드 비활성화로 팝업이 뜨지 않음")
                continue

            print("취소 버튼 클릭하여 팝업 닫기...")
            self.page.click(self.page.CONVENIENCE_CANCLE_BUTTON)
            time.sleep(1)
            print(f"[Test] {self.page.title_split(toggle)} 기능 테스트 종료")



        print("\n[Test] 스탠바이 모드 기능 테스트 시작")

        self.page.scroll_content_down()
        print("대기 모드 시작 버튼 클릭...")
        self.page.click(self.page.CONVENIENCE_START_BUTTON)
        time.sleep(1)

        print("대기 모드 취소 버튼 클릭...")
        self.page.click(self.page.CONVENIENCE_CANCLE_BUTTON)
        time.sleep(1)

        print("대기 모드 시작 버튼 재클릭...")
        self.page.click(self.page.CONVENIENCE_START_BUTTON)
        time.sleep(1)
        
        print("팝업 내 시작 버튼 클릭하여 모드 활성화 시도...")
        self.page.click(self.page.CONVENIENCE_START_BUTTON)
        time.sleep(2)
        
        print("편의 기능 시나리오 테스트 완료!") 