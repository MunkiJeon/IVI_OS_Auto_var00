
import pytest
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from pages.vehicle_control_page import VehicleControlPage

class TestGeneralSettingsScenario:
    """
    일반 설정 (General Settings) 탭 테스트 시나리오
    - 글꼴 변경
    - 언어 변경
    - 날짜 및 시간 설정 (팝업 제어 포함)
    - 단위 및 표시 설정
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(3)
        self.page.click_sidebar_menu("일반 설정")
        time.sleep(1)
        yield
        # Teardown logic if needed

    def test_font_settings(self, driver):
        """
        [시나리오] 글꼴 설정 테스트
        1. 글꼴 드롭다운 클릭
        2. 각 글꼴(현대, 기아, 제네시스, 기본) 선택
        3. '적용' 버튼 활성화 여부 확인 및 클릭
        4. 팝업 확인 (앱 재시작 시나리오 대응)
        """
        print("\n[Test] 글꼴 설정 테스트 시작")
        
        # 테스트할 글꼴 목록
        FONT_SETTINGS = [
            self.page.GENERAL_FONT_SETTING_HYUNDAI,
            self.page.GENERAL_FONT_SETTING_KIA,
            self.page.GENERAL_FONT_SETTING_BASIC,
            self.page.GENERAL_FONT_SETTING_GENESIS
        ]

        for font in FONT_SETTINGS:
            self.page.click(self.page.GENERAL_FONT_DROPDOWN)
            time.sleep(1)
            self.page.click(font)
            time.sleep(1)
        
        self.page.click(self.page.GENERAL_FONT_SETTING_APPLY)
        time.sleep(1)
        print("적용 버튼 상태 확인...")

        if self.page.is_displayed(self.page.GENERAL_CONFIRM):
            self.page.click(self.page.GENERAL_CONFIRM)
            time.sleep(1)
        else:
            print("적용 버튼이 비활성화 상태입니다. (변경사항 없음)")

    def test_language_settings(self, driver):
        """
        [시나리오] 언어 설정 테스트
        1. 언어 드롭다운 클릭
        2. 'English' 선택 및 저장
        3. '한국어' 복귀 시도 (Fallback 로직 포함)
        """
        print("\n[Test] 언어 설정 테스트 시작")
        
        self.page.click(self.page.GENERAL_LANGUAGE_DROPDOWN)
        time.sleep(1)
        
        # 옵션 표시 확인
        assert self.page.is_displayed(self.page.GENERAL_LANGUAGE_SETTING_EN), "English 옵션 없음"
        assert self.page.is_displayed(self.page.GENERAL_LANGUAGE_SETTING_KO), "한국어 옵션 없음"
        
        # 영어로 변경
        print("[English]로 변경 시도...")
        self.page.click(self.page.GENERAL_LANGUAGE_SETTING_EN)
        time.sleep(1) 
        self.page.click(self.page.GENERAL_SAVE)
        time.sleep(1)
        print("[English]로 변경 완료")
        
        # 다시 드롭다운 열기 (영어 상태일 수 있음)
        self.page.click(self.page.GENERAL_LANGUAGE_DROPDOWN)
        time.sleep(1)
        
        # 한국어로 복귀
        print("[한국어]로 복귀 시도...")
        self.page.click(self.page.GENERAL_LANGUAGE_SETTING_KO)
        time.sleep(1)
        self.page.click(self.page.GENERAL_SAVE)
        time.sleep(1)
        print("[한국어]로 복귀 완료")

    def test_date_time_settings(self, driver):
        """
        [시나리오] 날짜 및 시간 설정 테스트
        1. '자동 시간 설정' 토글 해제
        2. '날짜 및 시간 설정' -> '설정' 버튼 클릭
        3. 팝업 내 Date/Time Picker 조작 (스와입)
        4. '저장' 버튼 클릭
        """
        print("\n[Test] 날짜 및 시간 설정 테스트 시작")
        
        # 자동 시간 설정이 켜져있어서 수동 설정이 안보이면 토글 끄기 (= 수동 모드 진입)
        if not self.page.is_displayed(self.page.GENERAL_DATE_TIME_SETTING):
            self.page.toggle_tap(self.page.GENERAL_AUTO_TIME_SETTING, x_offset=-60, y_offset=10)
            time.sleep(1)

            if self.page.is_displayed(self.page.GENERAL_DATE_TIME_SETTING):
                print("수동 설정 메뉴 표시됨")
            else:
                pytest.fail("수동 설정 메뉴가 활성화되지 않았습니다.")

        # 설정 버튼이 아래에 있을 수 있으므로 스크롤
        self.page.scroll_and_find(self.page.GENERAL_DATE_TIME_SETTING)
        time.sleep(1)
        self.page.scroll_content_down()
        time.sleep(1)
        
        self.page.click(self.page.GENERAL_MANUAL_TIME_SETTING)
        time.sleep(1)
        
        # --- 팝업 조작 ---
        print("날짜/시간 설정 팝업 진입. Picker 조작 시작...")
        
        headers_found = False
        pickers = []
        
        # 전략 1: EditText 찾기
        try:
            pickers = self.page.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.EditText")
            if len(pickers) != 5:
                 pickers = self.page.driver.find_elements(AppiumBy.CLASS_NAME, "android.widget.NumberPicker")
        except:
            pass
            
        if len(pickers) == 5:
            print(f"Picker 요소 발견 ({len(pickers)}개). 스와입 수행...")
            for i, picker in enumerate(pickers):
                try:
                    rect = picker.rect
                    cx = rect['x'] + rect['width'] // 2
                    cy = rect['y'] + rect['height'] // 2
                    # 위로 스와입 (값 변경)
                    self.page.swipe(cx, cy, cx, cy + 100, 300) 
                    time.sleep(0.5)
                except:
                    print(f"Picker {i+1} 스와입 실패")
        else:
            print("Picker 요소를 찾을 수 없음. 헤더 기준 상대 좌표 스와입 시도...")
            # 전략 2: 헤더 텍스트 기준 좌표 계산
            try:
                date_header = None
                time_header = None
                
                # 헤더 찾기 (한글/영어 대응)
                try:
                    date_header = self.page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='날짜']")
                    time_header = self.page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='시간']")
                except:
                    date_header = self.page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Date')]")
                    time_header = self.page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'Time')]")
                    
                # 하단 저장 버튼 찾기 (Y축 기준점)
                save_btn = self.page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='저장' or @text='Save' or @text='확인' or @text='OK']")
                
                if date_header and time_header and save_btn:
                    header_bottom = date_header.rect['y'] + date_header.rect['height']
                    save_top = save_btn.rect['y']
                    swipe_cy = (header_bottom + save_top) // 2
                    
                    # 날짜 컬럼 3개 (년, 월, 일) - Date 헤더 너비의 20%, 50%, 80% 지점
                    dr = date_header.rect
                    d_xs = [dr['x'] + dr['width'] * p for p in [0.20, 0.50, 0.80]]
                    
                    # 시간 컬럼 2개 (시, 분) - Time 헤더 너비의 30%, 70% 지점
                    tr = time_header.rect
                    t_xs = [tr['x'] + tr['width'] * p for p in [0.30, 0.70]]
                    
                    swipe_points = d_xs + t_xs
                    
                    for i, sx in enumerate(swipe_points):
                        self.page.swipe(sx, swipe_cy, sx, swipe_cy + 100, 300)
                        time.sleep(0.5)
                        print(f"컬럼 {i+1}/5 스와입 완료 (좌표 기반)")
                        
                else:
                    print("헤더 또는 저장 버튼을 찾을 수 없어 좌표 계산 불가")
                    
            except Exception as e:
                print(f"좌표 기반 스와입 실패: {e}")

        # 저장
        print("'저장' 버튼 클릭...")
        try:
            self.page.driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='저장' or @text='Save']").click()
            time.sleep(2)
            print("설정 저장 완료")
        except:
            print("저장 버튼 클릭 실패")

        # 시간 형식 설정
        self.page.click_after_text("시간 형식", "12 시간")
        time.sleep(1)
        self.page.click_after_text("시간 형식", "24 시간")
        time.sleep(1)
        # 원복: 다시 자동 시간 설정 켜기
        # (테스트 상태 복구를 위해)
        self.page.toggle_tap(self.page.GENERAL_AUTO_TIME_SETTING, x_offset=-60, y_offset=10)
        time.sleep(1)

        print("날짜 및 시간 설정 테스트 완료")

    # 단위 설정 테스트
    def test_unit_settings(self, driver):
        print("\n[Test] 단위 설정 테스트 시작")

        self.page.scroll_and_find(self.page.GENERAL_UNIT_SETTING)
        time.sleep(1)
        self.page.scroll_content_down()
        time.sleep(1)

        #보조 속도 표시
        print("보조 속도 표시 설정")
        self.page.toggle_tap(self.page.GENERAL_SUB_SPEED_DISPLAY, x_offset=-60, y_offset=10)
        time.sleep(1)
        self.page.toggle_tap(self.page.GENERAL_SUB_SPEED_DISPLAY, x_offset=-60, y_offset=10)
        time.sleep(1)

        # 거리 단위 설정    
        print("거리 단위 설정")
        self.page.click_after_text("거리", "km")
        time.sleep(1)
        self.page.click_after_text("거리", "mile")
        time.sleep(1)
        
        # 온도 단위 설정
        print("온도 단위 설정")
        # self.page.click_after_text("온도", "℃") # 특수문자가 인식이 안되는 듯 함
        # time.sleep(1)
        # self.page.click_after_text("온도", "℉")
        # time.sleep(1)
        self.page.click_grouped_button("온도", 0, 2, 652, 71, 14)
        time.sleep(1)
        self.page.click_grouped_button("온도", 1, 2, 652, 71, 14)
        time.sleep(1)

        # 연비 단위 설정
        print("연비 단위 설정")
        self.page.click_after_text("연비", "km/kWh")
        time.sleep(1)
        self.page.click_after_text("연비", "kWh/100km")
        time.sleep(1)

        # 타이어 공기압 단위 설정
        print("타이어 공기압 단위 설정")
        self.page.click_after_text("타이어 공기압", "kPa")
        time.sleep(1)
        self.page.click_after_text("타이어 공기압", "bar")
        time.sleep(1)
        self.page.click_after_text("타이어 공기압", "psi")
        time.sleep(1)

