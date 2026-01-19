import pytest
import time
from pages.vehicle_control_page import VehicleControlPage
from appium.webdriver.common.appiumby import AppiumBy

class TestAppsScenario:
    """
    앱 (Apps) 탭 테스트 시나리오
    - 앱 목록 수집 및 레이아웃 점검
    - 각 앱 상세 페이지 진입 및 인포테인먼트 설정(토글) 점검
    - 앱 강제 종료(Termination) 팝업 동작 확인
    - 다운로드된 앱 상세 확인
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 앱 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        if not self.page.is_loaded():
            pytest.fail("오류: 앱이 로드되지 않았습니다.")
        
        print("앱 메뉴로 이동 중...")
        self.page.click_sidebar_menu("앱")
        # 사이드바 스크롤 (앱 메뉴가 아래쪽에 있을 경우 대비)
        # self.page.scroll_down_sidebar()
        self.collected_apps = []
        time.sleep(2)
        yield

    def test_apps_collection_and_layout(self):
        """
        [시나리오] 앱 목록 확인 및 상/하단 앱 이름 수집
        """
        print("\n[Test] 앱 목록 수집 및 레이아웃 점검 시작")
        
        if self.page.is_displayed(self.page.APPS_DEFAULT_APPS):
            print("확인됨: 기본 앱 섹션이 표시됩니다.")
        else:
            pytest.fail("주의: 기본 앱 문구가 표시되지 않았습니다.")
        
        print("상단 앱 목록 수집 중...")
        top_apps = self.page.get_all_texts(min_y=120, min_x=1000, exclude_texts=['기본 앱', '강제 종료'])
        for app in top_apps:
            if app not in self.collected_apps:
                self.collected_apps.append(app)
        print(f"상단 앱 감지: {top_apps}")

        # 2. 하단 앱 목록 수집 (스크롤 다운)
        print("하단 앱 목록 확인을 위해 앱 컨텐츠 스크롤 다운...")
        self.page.scroll_content_down()
        time.sleep(2)

        bottom_apps = self.page.get_all_texts(min_y=120, min_x=1000, exclude_texts=['기본 앱', '강제 종료', '다운로드된 앱'])
        for app in bottom_apps:
            if app not in self.collected_apps:
                self.collected_apps.append(app)
        print(f"하단 앱 감지: {bottom_apps}")
        
        print(f"수집 완료: 총 {len(self.collected_apps)}개의 앱이 식별되었습니다.")

    def test_apps_detail_interaction_flow(self, driver,):
        """
        [시나리오] 수집된 앱별 상세 진입, 토글 테스트 및 뒤로가기 반복
        """
        print("\n[Test] 앱 상세 인터랙션 테스트 시작")
        
        if len(self.collected_apps) == 0:
            print("알림: 수집된 앱이 없어 테스트를 건너뜁니다. (test_apps_collection_and_layout 먼저 실행 필요)")
            return


        de = 0
        for index, app_name in enumerate(self.collected_apps):
            # 변수 초기화
            one = 0
            two = 0
            tg = 0
            # 동적 로케이터 생성
            locator = (AppiumBy.XPATH, f"//android.widget.TextView[@text='{app_name}']")
        
            try:  
                # 화면에 안 보이면 스크롤 다운 시도 (리스트의 후반부일 가능성)
                if de == 9:
                    print(f"'{app_name}' 찾기 위해 스크롤 다운...")
                    self.page.scroll_content_down()
                    time.sleep(1)

                print(f"[{index+1}/{len(self.collected_apps)}] '{app_name}' 클릭 중...")
                self.page.click(locator)
                time.sleep(1)
            
                # 상세 화면 진입 확인
                if self.page.is_displayed(locator):
                    print(f"확인됨: '{app_name}' 상세 화면 진입 성공.")
                else:
                    print(f"주의: '{app_name}' 상세 화면 타이틀 확인 불가.")
                strange = [
                    self.page.APPS_LOCATION,
                    self.page.APPS_ALARM,
                    self.page.APPS_MIC
                ]
                for locator2 in strange:
                    try:
                        if self.page.is_displayed(locator2, timeout=0.3):
                            tg += 1
                    except:
                        print(f"[locator] 토글 미노출 확인")
            
                # 토글 테스트 진행 여부 판단 (권한 허용 항목 등이 보이는지 확인)
                if tg >= 1:
                    print(f"'{app_name}' 토글 버튼 테스트 진행...")
                
                    togglebutton = [
                        self.page.APPS_IconBtn["APPS_TOGGLE"],
                        self.page.APPS_IconBtn["APPS_TOGGLE2"],
                        self.page.APPS_IconBtn["APPS_TOGGLE3"],
                    ]
                
                    for locator1 in togglebutton:
                        try:
                            # one, two 변수를 이용한 클릭 제어 복구
                            if one == 0 and two <= 1:
                                x, y = locator1
                                self.page.tap_coordinates(x*1920, y*1080)
                                time.sleep(0.5)
                                self.page.tap_coordinates(x*1920, y*1080)
                                time.sleep(0.5)
                        
                            # 앱 이름에 따라 변수 증가 (기존 de 인덱스 로직을 매핑)
                            if tg == 1:
                                one += 1
                            if tg == 2:
                                two += 1        
                        except Exception as e:
                            print(f"토글 클릭 건너뜀: {e}")  
                else:
                    print(f"'{app_name}' 토글 테스트 건너뜀 (설정 항목 없음).")

                # 뒤로가기 버튼 좌표 클릭
                # 상세 화면 진입 후 '앱 이름' 텍스트 위치 기준
                if self.page.is_displayed(locator):
                    print(f"'{app_name}' 뒤로가기 버튼 클릭...")
                    self.page.toggle_tap(locator, x_offset=-40, y_offset=20)
                else:
                    print(f"주의: '{app_name}' 요소를 찾지 못해 기본 좌표로 뒤로가기 시도.")
                    target_back_x, target_back_y = self.page.CONNECTION_IconBtn["CONNECTION_BACK_BUTTON"]
                    self.page.tap_coordinates(target_back_x*1920, target_back_y*1080)
                    time.sleep(1)
                time.sleep(1)
                de += 1 
            except Exception as e:
                print(f"'{app_name}' 테스트 중 오류 발생: {e}")
                # 복구 시도 (메인으로 이동)
                self.page.start()
                self.page.click_sidebar_menu("앱")
                time.sleep(1)
            

    def test_apps_termination_popup_flow(self, driver):
        """
        [시나리오] 강제 종료(Termination) 팝업 동작 확인 (취소/확인)
        """
        print("\n[Test] 강제 종료 팝업 테스트 시작")
        print("강제 종료 버튼 클릭...")
        self.page.click(self.page.APPS_TERMINATION)
        time.sleep(1)

        if self.page.is_displayed(self.page.APPS_TERMINATION_POPUP):
            print("확인됨: 강제 종료 확인 팝업이 표시됩니다.")
        
        print("팝업 내 취소 버튼 클릭...")
        self.page.click(self.page.APPS_TERMINATION_POPUP_CANCEL)
        time.sleep(1)

        print("강제 종료 버튼 재클릭 및 확인(Confirm) 시도...")
        self.page.click(self.page.APPS_TERMINATION)
        time.sleep(1)
        
        # 확인 버튼은 취소 버튼 좌측 좌표 기반
        self.page.toggle_tap(self.page.APPS_TERMINATION_POPUP_CANCEL, x_offset=-400, y_offset=0)
        time.sleep(2)
        
        print("앱 재진입 확인...")
        self.page.start()
        self.page.click_sidebar_menu("앱")
        time.sleep(1)

    def test_downloaded_apps_interaction_flow(self, driver):
        """
        [시나리오] 다운로드된 앱 섹션 확인 및 상세 동작 점검
        """
        print("\n[Test] 다운로드된 앱 점검 시작")
        
        print("목록 하단으로 스크롤...")
        for _ in range(3):
            self.page.scroll_content_down()
        time.sleep(1)

        if self.page.is_displayed(self.page.APPS_DOWNLOAD_APP):
            print(f"확인됨: {self.page.APPS_DOWNLOAD_APP} 표시됨.")
            print("다운로드 앱 클릭...")
            self.page.toggle_tap(self.page.APPS_DOWNLOAD_APP, x_offset=100, y_offset=100)
            time.sleep(1)
            one = 0
            two = 0
            tg = 0
            strange = [
                self.page.APPS_LOCATION,
                self.page.APPS_ALARM,
                self.page.APPS_MIC
                ]
            for locator2 in strange:
                try:
                    if self.page.is_displayed(locator2, timeout=0.3):
                        tg += 1
                except:
                    print("토글 미노출 확인")
                # 토글 테스트 진행 여부 판단 (권한 허용 항목 등이 보이는지 확인)
            if tg >= 1:
                print("토글 버튼 테스트 진행...")
            
                togglebutton = [
                    self.page.APPS_IconBtn["APPS_TOGGLE"],
                    self.page.APPS_IconBtn["APPS_TOGGLE2"],
                    self.page.APPS_IconBtn["APPS_TOGGLE3"],
                ]
            
                for locator1 in togglebutton:
                    try:
                        # one, two 변수를 이용한 클릭 제어 복구
                        if one == 0 and two <= 1:
                            x, y = locator1
                            self.page.tap_coordinates(x*1920, y*1080)
                            time.sleep(0.5)
                            self.page.tap_coordinates(x*1920, y*1080)
                            time.sleep(0.5)
                        
                            # 앱 이름에 따라 변수 증가 (기존 de 인덱스 로직을 매핑)
                            if tg == 1:
                                one += 1
                            if tg == 2:
                                two += 1        
                    except Exception as e:
                        print(f"토글 클릭 건너뜀: {e}")  
            else:
                print("토글 테스트 건너뜀 (설정 항목 없음).")
        
            print("뒤로가기 버튼 클릭...")
            # 다운로드 앱 기준으로 재계산하는 것이 안전함.
            target_back_x, target_back_y = self.page.CONNECTION_IconBtn["CONNECTION_BACK_BUTTON"]
            self.page.tap_coordinates(target_back_x*1920, target_back_y*1080)
            time.sleep(1)
            if self.page.is_displayed(self.page.APPS_DOWNLOAD_APP):
                print(f"확인됨: {self.page.APPS_DOWNLOAD_APP} 표시됨.")
            else:
                pytest.fail(f"오류: {self.page.APPS_DOWNLOAD_APP} 상세 화면이 표시되지 않습니다.")
        else:
            print(f"알림: {self.page.APPS_DOWNLOAD_APP} 가 보이지 않아 테스트를 건너뜁니다.")

        print("앱 시나리오 테스트 완료!")
