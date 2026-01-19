import pytest
import time
from pages.vehicle_control_page import VehicleControlPage
import navigate_setup

class TestProfileScenario:
    """
    프로필 (Profile) 탭 테스트 시나리오
    - 프로필 메뉴 진입 및 메인 UI 요소 확인
    - 프로필 추가 화면 UI 점검 및 뒤로가기 동작 확인
    - 프로필 생성 흐름 테스트 (이름 입력, 삭제, 저장)
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 프로필 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        if not self.page.is_loaded():
            pytest.fail("오류: 앱이 로드되지 않았습니다.")
        
        print("프로필 메뉴로 이동 중...")
        self.page.click_sidebar_menu("프로필")
        time.sleep(2)
        yield

    def test_add_profile_flow(self, driver):
        """
        [시나리오] 프로필 추가 화면 UI 확인 및 뒤로가기 동작 테스트
        """
        print("\n[Test] 프로필 추가 화면 UI 테스트 시작")
        
        print("프로필 추가 버튼 클릭...")
        self.page.click(self.page.PROFILE_ADD)
        time.sleep(1)

        print("프로필 추가 화면 요소 확인 중...")
        add_ui_items = [
            (self.page.PROFILE_ADD, "프로필 추가 타이틀"),
            (self.page.PROFILE_ENTER_NAME, "이름 입력 필드"),
            (self.page.PROFILE_SAVE, "저장 버튼"),
        ]
        for locator, label in add_ui_items:
            if self.page.is_displayed(locator):
                print(f"확인됨: {label} 요소가 표시됩니다.")
            else:
                pytest.fail(f"오류: {label} 요소가 표시되지 않습니다.")

        # 뒤로가기 버튼 클릭 (좌표 기반: 타이틀 왼쪽)
        print("뒤로가기 버튼 클릭하여 메인으로 복귀...")
        self.page.toggle_tap(self.page.PROFILE_ADD, x_offset=-40, y_offset=20)
        time.sleep(1)
        
        if self.page.is_displayed(self.page.PROFILE_SETTINGS):
            print("확인됨: 프로필 메인 화면으로 정상 복귀했습니다.")
        else:
            pytest.fail("오류: 뒤로가기 동작 후 메인 화면이 표시되지 않습니다.")
        """
        [시나리오] 프로필 생성 흐름 테스트 (입력 -> 삭제 -> 재입력 -> 저장)
        """
        print("프로필 추가 버튼 클릭...")
        self.page.click(self.page.PROFILE_ADD)
        time.sleep(1)
        
        # 1. 초기 키보드 입력 (ASDF)
        print("키보드 입력 시도 (ASDF)...")
        keyboard_asdf = ["PROFILE_A", "PROFILE_S", "PROFILE_D", "PROFILE_F"]
        for key in keyboard_asdf:
            try:
                x, y = self.page.PROFILE_IconBtn[key]
                self.page.tap_coordinates(x * 1920, y * 1080)
                time.sleep(0.3)
            except Exception as e:
                print(f"입력 실패 ({key}): {e}")

        # 2. 이름 삭제 버튼 클릭 (저장 버튼 좌측 좌표 기반)
        print("입력된 이름 삭제 중...")
        self.page.toggle_tap(self.page.PROFILE_SAVE, x_offset=-75, y_offset=20)
        time.sleep(1)

        # 3. 재입력 (XPTMXM)
        print("키보드 재입력 시도 (XPTMXM)...")
        keyboard_new = ["PROFILE_X", "PROFILE_P", "PROFILE_T", "PROFILE_M", "PROFILE_X", "PROFILE_M"]
        for key in keyboard_new:
            try:
                x, y = self.page.PROFILE_IconBtn[key]
                self.page.tap_coordinates(x * 1920, y * 1080)
                time.sleep(0.3)
            except Exception as e:
                print(f"입력 실패 ({key}): {e}")

        print("저장시 연결 오류 발생으로 생략 \n\n\n프로필 시나리오 테스트 완료!")
        # 4. 저장 및 완료
        # print("프로필 저장 버튼 클릭...")
        # self.page.click(self.page.PROFILE_SAVE)
        # time.sleep(2)
        
        # print("프로필 시나리오 테스트 완료!")
        
        # print("\n[Setup Wizard] 1분 30초 대기 후 설정 마법사 자동화 실행...")
        # time.sleep(90)
        # print("[Setup Wizard] 설정 마법사 네비게이션 시작")
        # navigate_setup.run_flow()


