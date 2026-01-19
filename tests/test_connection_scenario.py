import pytest
import time
from pages.vehicle_control_page import VehicleControlPage

class TestConnectionScenario:
    """
    연결 (Connection) 탭 테스트 시나리오
    - 블루투스 (기기 추가, AA/CP 토글)
    - Wi-Fi (네트워크 추가, 보안 옵션, 비밀번호 입력)
    - Wi-Fi 핫스팟 (설정 및 비밀번호)
    - 모바일 데이터 (사용량 확인 및 토글)
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 연결 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        print("연결 메뉴로 이동 중...")
        self.page.click_sidebar_menu("연결")
        time.sleep(2)
        yield

    def test_connection_toggle(self, driver):
        """
        [시나리오] 연결 화면 메인 토글 확인
        """


        # 토글 버튼 동작 확인 (블루투스, 모바일 데이터)
        toggle_locs = [
            self.page.CONNECTION_BLUETOOTH,
            #self.page.CONNECTION_WIFI,
            #self.page.CONNECTION_WIFI_HOTSPOT,
            self.page.CONNECTION_MOBILE_DATA,
        ]
        for locator in toggle_locs:
            try:
                print(f"{locator} 토글 클릭 (OFF/ON 반복)...")
                self.page.toggle_tap(locator, x_offset=-60, y_offset=10)
                time.sleep(1)
                self.page.toggle_tap(locator, x_offset=-60, y_offset=10)
                time.sleep(1)
            except Exception as e:
                print(f"{locator} 토글 동작 실패: {e}")

    def test_bluetooth_flow(self, driver):
        """
        [시나리오] 블루투스 설정 및 기기 추가 흐름 테스트
        """
        print("\n[Test] 블루투스 설정 테스트 시작")
        
        print("블루투스 설정 클릭...")
        self.page.click(self.page.CONNECTION_BLUETOOTH)
        time.sleep(1)

        # 뒤로가기 후 재진입
        print("블루투스 화면 뒤로가기 클릭...")
        self.page.toggle_tap(self.page.CONNECTION_BLUETOOTH, x_offset=-40, y_offset=20)
        time.sleep(1)

        print("블루투스 설정 재클릭...")
        self.page.click(self.page.CONNECTION_BLUETOOTH)
        time.sleep(1)

        # 기기 추가 팝업 및 기기 찾기 화면
        print("기기 추가 버튼 클릭...")
        self.page.click(self.page.CONNECTION_BLUETOOTH_ADD)
        time.sleep(1)

        print("기기 검색 문구 클릭...")
        self.page.click(self.page.CONNECTION_BLUETOOTH_ADD_POPUP_TEXT)
        time.sleep(1)

        print("기기 찾기 닫기 클릭...")
        self.page.click(self.page.CONNECTION_BLUETOOTH_ADD_POPUP_CLOSE)
        time.sleep(1)

        print("기기 추가 팝업 취소 클릭...")
        self.page.click(self.page.CONNECTION_BLUETOOTH_ADD_POPUP_CANCEL)
        time.sleep(1)

        # AA/CP 토글 테스트
        for locator in [self.page.CONNECTION_BLUETOOTH_ANDROID_AUTO, self.page.CONNECTION_BLUETOOTH_APPLE_CARPLAY]:
            print(f"{locator} 토글 클릭...")
            self.page.toggle_tap(locator, x_offset=-60, y_offset=10)
            time.sleep(1)
            self.page.toggle_tap(locator, x_offset=-60, y_offset=10)
            time.sleep(1)
        print("블루투스 화면 뒤로가기 클릭...")
        self.page.toggle_tap(self.page.CONNECTION_BLUETOOTH, x_offset=-40, y_offset=20)
        time.sleep(1)

    def test_wifi_flow(self, driver):
        """
        [시나리오] Wi-Fi 설정 및 네트워크 추가 테스트
        """
        print("\n[Test] Wi-Fi 설정 테스트 시작")
        
        print("WI-FI 설정 클릭...")
        self.page.click(self.page.CONNECTION_WIFI)
        time.sleep(1)

        # 아이콘 좌표 기반 클릭 (설정 아이콘 등)
        # 기존 코드에서 x, y 값을 직접 가져오는 부분이 있어 주의
        print("WI-FI 설정 아이콘 클릭...")
        x, y = self.page.CONNECTION_IconBtn["CONNECTION_WIFI_SETTINGS"]
        self.page.tap_coordinates(x*1920, y*1080)
        time.sleep(0.5)

       
        print("WI-FI 설정 뒤로가기 버튼 클릭...")
        # 뒤로가기 버튼 좌표
        target_back_x, target_back_y = self.page.CONNECTION_IconBtn["CONNECTION_BACK_BUTTON"]
        self.page.tap_coordinates(target_back_x*1920, target_back_y*1080)
        time.sleep(1)
    
        # Wi-Fi 설정 아이콘 클릭 및 비밀번호 입력 필드 조작
        target_setting_x, target_setting_y = self.page.CONNECTION_IconBtn["CONNECTION_WIFI_SETTINGS"]
        self.page.tap_coordinates(target_setting_x*1920, target_setting_y*1080)
        time.sleep(1)

        print("눈 아이콘 클릭 (비밀번호 표시/숨김)...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=380, y_offset=75)
        time.sleep(1)
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=380, y_offset=75)
        time.sleep(1)
    
        print("[X] 아이콘 클릭 (초기화)...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=335, y_offset=75)
        time.sleep(1)
    
        print("비밀번호 입력 필드 클릭...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=255, y_offset=75)
        time.sleep(1)

        print("키보드 입력 (ASDF)...")
        keyboard = [
            self.page.PROFILE_IconBtn["PROFILE_A"],
            self.page.PROFILE_IconBtn["PROFILE_S"],
            self.page.PROFILE_IconBtn["PROFILE_D"],
            self.page.PROFILE_IconBtn["PROFILE_F"],
        ]
        for locator in keyboard:
            try:
                x2, y2 = locator
                self.page.tap_coordinates(x2*1920, y2*1080)
                time.sleep(0.5)
            except Exception as e:
                print(f"키보드 입력 실패 {locator}: {e}")
        time.sleep(0.5)
    
        print("취소 버튼 클릭...")
        self.page.click(self.page.CONNECTION_WIFI_NOW_CANCEL)
        time.sleep(1)
    
        print("WI-FI 설정 아이콘 클릭...")
        self.page.tap_coordinates(target_setting_x*1920, target_setting_y*1080)
        time.sleep(1)
    
        print("확인 버튼 클릭...")
        self.page.click(self.page.CONNECTION_WIFI_NOW_CHECK)
        time.sleep(1)

        # 네트워크 추가 테스트
        print("네트워크 추가 버튼 클릭...")
        self.page.click(self.page.CONNECTION_WIFI_ADD)
        time.sleep(1)


        # 네트워크 추가 뒤로가기 후 재진입
        print("네트워크 추가 뒤로가기 클릭...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_ADD, x_offset=-40, y_offset=20)
        time.sleep(1)
    
        self.page.click(self.page.CONNECTION_WIFI_ADD)
        time.sleep(1)

        print("보안 드롭다운 테스트...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_SUCURITY, x_offset=100, y_offset=80)
        time.sleep(1)
            
        # 드롭다운 선택 반복 체크
        drop = 0
        dropdown = [
            self.page.CONNECTION_WIFI_ADD_OPEN,
            self.page.CONNECTION_WIFI_ADD_WEP,
            self.page.CONNECTION_WIFI_ADD_WPA2,
            self.page.CONNECTION_WIFI_ADD_WPA3,
        ]
        for locator in dropdown:
            try:  
                print(f"{locator} 선택...")
                self.page.click(locator)
                time.sleep(1)
                # 여기 로직은 원본 그대로 유지 (오픈 시 비밀번호 숨김 확인 등)
                if self.page.is_displayed(locator):
                    print(f"검증: {locator} 선택됨.")
                    if drop == 0:
                        if not self.page.is_displayed(self.page.CONNECTION_WIFI_NOW_PASSWARD, timeout=2):
                            print(f"확인됨: Open 선택 시 비밀번호 필드 숨김.")
                        else:
                            pytest.fail(f"오류: Open 선택 시 비밀번호 필드가 보임.")
                
                # 마지막 항목이 아니면 다시 드롭다운 열기
                    if drop < 3:
                        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_SUCURITY, x_offset=100, y_offset=80)
                    drop += 1
                else:
                    pytest.fail(f"오류: {locator} 표시되지 않음.")
            except Exception as e:
                print(f"드롭다운 테스트 실패 {locator}: {e}")

        # 네트워크 이름 입력
        print("네트워크 이름 입력 필드 클릭...")
        self.page.click(self.page.CONNECTION_WIFI_ADD_NAME_TEXT)
        time.sleep(1)
    
        print("키보드 입력 (ASDF + ENTER)...")
        keyboard_name = [
            self.page.PROFILE_IconBtn["PROFILE_A"],
            self.page.PROFILE_IconBtn["PROFILE_S"],
            self.page.PROFILE_IconBtn["PROFILE_D"],
            self.page.PROFILE_IconBtn["PROFILE_F"],
            self.page.CONNECTION_IconBtn["CONNECTION_ENTER"],
        ]
        for locator in keyboard_name:
            try:
                x2, y2 = locator
                self.page.tap_coordinates(x2*1920, y2*1080)
                time.sleep(0.5)
            except Exception as e:
                print(f"키보드 입력 실패 {locator}: {e}")
        time.sleep(1)

        # 네트워크 이름 삭제 테스트
        print("[X] 아이콘 클릭 (이름 삭제)...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_ADD_NAME, x_offset=380, y_offset=75)
        time.sleep(1)

        # 비밀번호 입력
        print("네트워크 비밀번호 입력 필드 클릭...")
        self.page.click(self.page.CONNECTION_WIFI_ADD_PASSWARD)
        time.sleep(1)
    
        print("키보드 입력 (ASDF + ENTER)...")
        for locator in keyboard_name:
            try:
                x2, y2 = locator
                self.page.tap_coordinates(x2*1920, y2*1080)
                time.sleep(0.5)
            except Exception as e:
                print(f"키보드 입력 실패 {locator}: {e}")

        # 비밀번호 표시/숨김/삭제    
        print("눈 아이콘 클릭 (비밀번호 표시/숨김)...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=380, y_offset=75)
        time.sleep(1)
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=380, y_offset=75)
        time.sleep(1)
    
        print("[X] 아이콘 클릭 (초기화)...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=335, y_offset=75)
        time.sleep(1)

        print("취소 버튼 클릭...")
        self.page.click(self.page.CONNECTION_WIFI_NOW_CANCEL)
        time.sleep(1)
    
        print("WI-FI 화면 뒤로가기 클릭...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI, x_offset=-40, y_offset=20)
        time.sleep(1)

    def test_hotspot_flow(self, driver):
        """
        [시나리오] Wi-Fi 핫스팟 설정 테스트
        """
        print("\n[Test] Wi-Fi 핫스팟 테스트 시작")
        
        print("WI-FI 핫스팟 클릭...")
        self.page.click(self.page.CONNECTION_WIFI_HOTSPOT)
        time.sleep(1)
    
        print("눈 아이콘 클릭 (비밀번호 표시/숨김)...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=380, y_offset=75)
        time.sleep(1)
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=380, y_offset=75)
        time.sleep(1)
    
        print("[X] 아이콘 클릭 (초기화)...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=335, y_offset=75)
        time.sleep(1)
    
        print("비밀번호 입력 필드 클릭...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_NOW_PASSWARD, x_offset=255, y_offset=75)
        time.sleep(1)

        print("키보드 입력 (ASDF)...")
        keyboard = [
            self.page.PROFILE_IconBtn["PROFILE_A"],
            self.page.PROFILE_IconBtn["PROFILE_S"],
            self.page.PROFILE_IconBtn["PROFILE_D"],
            self.page.PROFILE_IconBtn["PROFILE_F"],
        ]
        for locator in keyboard:
            try:
                x2, y2 = locator
                self.page.tap_coordinates(x2*1920, y2*1080)
                time.sleep(0.5)
            except Exception as e:
                print(f"키보드 입력 실패 {locator}: {e}")
        time.sleep(0.5)

        print("WI-FI 핫스팟 뒤로가기 클릭...")
        self.page.toggle_tap(self.page.CONNECTION_WIFI_HOTSPOT, x_offset=-40, y_offset=20)
        time.sleep(1)

    def test_mobile_data_flow(self, driver):
        """
        [시나리오] 모바일 데이터 설정 테스트
        """
        print("\n[Test] 모바일 데이터 테스트 시작")
        
        print("모바일 데이터 클릭...")
        self.page.click(self.page.CONNECTION_MOBILE_DATA)
        time.sleep(1)

        print("모바일 데이터 토글 클릭...")
        self.page.toggle_tap(self.page.CONNECTION_MOBILE_DATA, x_offset=-20, y_offset=115)
        time.sleep(1)
        self.page.toggle_tap(self.page.CONNECTION_MOBILE_DATA, x_offset=-20, y_offset=115)
        time.sleep(1)
    
        print("모바일 데이터 뒤로가기 클릭...")
        self.page.toggle_tap(self.page.CONNECTION_MOBILE_DATA, x_offset=-40, y_offset=20)
        time.sleep(1)

        # 최종 연결 화면 확인
        print("연결 화면 복귀 확인...")
        conui = [
            self.page.CONNECTION_TITLE,
            self.page.CONNECTION_BLUETOOTH,
            self.page.CONNECTION_WIFI,
            self.page.CONNECTION_WIFI_HOTSPOT,
            self.page.CONNECTION_MOBILE_DATA,
        ]
        for locator in conui:
            try:  
                if self.page.is_displayed(locator):
                    print(f"확인됨: {locator} 요소가 표시됩니다.")
                else:
                    pytest.fail(f"오류: {locator} 요소가 표시되지 않습니다.")
            except Exception as e:
                print(f"{locator} 요소 가시성 확인 실패: {e}")

        print("연결 시나리오 테스트 완료!")