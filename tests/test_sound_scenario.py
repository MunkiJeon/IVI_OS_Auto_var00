import pytest
import pytest
import time
import random
from pages.vehicle_control_page import VehicleControlPage

class TestSoundScenario:
    """
    사운드 (Sound) 탭 테스트 시나리오
    - 사운드 전반 레이아웃 및 요소 가시성 점검
    - 시스템 및 미디어 음량 제어 (스와이프/탭)
    - 자동 음량 조절, 사운드 포커스 및 밸런스 설정
    - 상세 이퀄라이저 주파수 대역 조절
    - 안드로이드 오토(폰 프로젝션) 전용 사운드 설정 확인
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 메서드 실행 전 초기화 및 사운드 메뉴 진입"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        if not self.page.is_loaded():
            pytest.fail("오류: 앱이 로드되지 않았습니다.")
        
        print("사운드 메뉴로 이동 중...")
        self.page.click_sidebar_menu("사운드")
        time.sleep(2)
        yield

    def test_volume_control_flow(self, driver):
        """
        [시나리오] 음량 조절 (조용한 모드 및 슬라이더 스와이프/탭) 동작 확인
        """
        print("\n[Test] 음량 조절 테스트 시작")
        
        # 1. 조용한 모드 토글 테스트
        print("조용한 모드 토글 테스트 (On/Off)...")
        for i in range(2):
            self.page.toggle_tap(self.page.SND_QUIET, x_offset=-60, y_offset=10)
            time.sleep(1)

        # 2. 개별 음량 조절 테스트 (시스템/벨소리 등)
        print("음량 슬라이더 조절 테스트 중...")
        target_locators = [
            (self.page.SND_SYSTEM, "시스템 음량"),
            #(self.page.SND_MEDIA, "미디어 음량"),
            #(self.page.SND_NAVIGATION, "내비게이션 음량"),
            (self.page.SND_RINGTONE, "벨소리 음량")
        ]
        for locator, label in target_locators:
            try:  
                rect_v = driver.find_element(*locator).rect  
                base_x = rect_v['x'] + 100
                base_y = rect_v['y'] + 80
                max_x = rect_v['x'] + 530
                
                print(f"{label} 스와이프 올리기...")
                self.page.swipe(base_x, base_y, max_x, base_y, 1000)
                time.sleep(1)
                
                print(f"{label} 스와이프 내리기...")
                self.page.swipe(max_x - 50, base_y, base_x - 50, base_y, 1000)  
                time.sleep(1)
                
                print(f"{label} 볼륨 높이기 (탭 12회)...")
                for _ in range(12):
                    self.page.tap_coordinates(max_x, base_y)
                    time.sleep(0.1)
                
                print(f"{label} 볼륨 낮추기 (탭 9회)...")
                for _ in range(9):
                    self.page.tap_coordinates(base_x - 50, base_y)
                    time.sleep(0.1)
                
                print(f"{label} 음소거 토글...")
                for _ in range(2):
                    self.page.tap_coordinates(max_x + 100, base_y)
                    time.sleep(1)
            except Exception as e:
                pytest.fail(f"{label} 동작 테스트 실패: {e}")

        """
        통화/안내 등 중단 음량 조절 동작 테스트 (스크롤 다운 후 진행)
        """
        # 아래로 스크롤
        print("아래로 스크롤 중...")
        self.page.scroll_content_down()
        time.sleep(2)

        bottomevolume = [
            (self.page.SND_CALL, "통화 음량"),
            #(self.page.SND_GUIDE, "음성 안내 음량"),
        ]
        for locator, label in bottomevolume:
            try:  
                rect_v = driver.find_element(*locator).rect     
                base_x = rect_v['x'] + 100
                base_y = rect_v['y'] + 80
                max_x = rect_v['x'] + 530
                
                print(f"{label} 스와이프 올리기...")
                self.page.swipe(base_x, base_y, max_x, base_y, 1000)
                time.sleep(1)
                
                print(f"{label} 스와이프 내리기...")
                self.page.swipe(max_x - 50, base_y, base_x - 50, base_y, 1000)  
                time.sleep(1)
                
                print(f"{label} 볼륨 높이기 (탭 12회)...")
                for _ in range(12):
                    self.page.tap_coordinates(max_x, base_y)
                    time.sleep(0.1)
                
                print(f"{label} 볼륨 낮추기 (탭 9회)...")
                for _ in range(9):
                    self.page.tap_coordinates(base_x - 50, base_y)
                    time.sleep(0.1)
            except Exception as e:
                pytest.fail(f"{label} 동작 테스트 실패: {e}")

    def test_automatic_and_focus_flow(self, driver):
        """
        [시나리오] 자동 음량 조절, 사운드 포커스 및 밸런스(랜덤 스와이프) 확인
        """
        print("\n[Test] 자동 음량 및 포커스 테스트 시작")
        
        # 1. 자동 음량 설정
        print("자동 음량 조절 단계별 클릭 테스트...")
        self.page.scroll_and_find(self.page.SND_AUTOMATIC)
        time.sleep(1)
        auto_options = [self.page.SND_OFF, self.page.SND_WEAKLY, self.page.SND_MIDDLE, self.page.SND_STRONG, self.page.SND_OFF]
        for opt in auto_options:
            self.page.click(opt)
            time.sleep(0.5)

        # 2. 사운드 포커스 설정
        print("사운드 포커스 프리셋 클릭 테스트...")
        self.page.scroll_and_find(self.page.SND_FOCUS)
        time.sleep(1)
        focus_options = [self.page.SND_FRONT, self.page.SND_CENTER, self.page.SND_REAR, self.page.SND_SETTINGS, self.page.SND_FRONT]
        for opt in focus_options:
            self.page.click(opt)
            time.sleep(0.5)

        # 3. 사운드 밸런스 조절 (랜덤 스와이프)
        print("사운드 밸런스 랜덤 조절 테스트...")
        self.page.scroll_content_down()
        time.sleep(1)
        ham_x, ham_y = self.page.SND_IconBtn["SND_HAM"]
        for i in range(1, 4):
            rx = random.uniform(0.703, 0.807) * 1920
            ry = random.uniform(0.352, 0.509) * 1080
            print(f"사운드 밸런스 램덤 스와이프 {i}회: ({rx}, {ry})")
            self.page.swipe(ham_x * 1920, ham_y * 1080, rx, ry, 500)
            time.sleep(1)
            # 위치 갱신 (탭 보다는 흉내내는 느낌으로 유지)
            ham_x, ham_y = rx / 1920, ry / 1080

        print("초기화 버튼 클릭하여 밸런스 복구...")
        self.page.click(self.page.SND_INITIAL)
        time.sleep(1)

    def test_equalizer_adjustment_flow(self, driver):
        """
        [시나리오] 이퀄라이저 상세 주파수 대역 조절 및 초기화 확인
        """
        print("\n[Test] 이퀄라이저 주파수 대역 테스트 시작")
        
        # 이퀄라이저 영역으로 이동
        self.page.scroll_and_find(self.page.SND_3D)
        time.sleep(1)
         # 3D 서라운드 탭
        print("3D 서라운드 클릭 테스트...")
        time.sleep(1)
        focus_options = [self.page.SND_OFF, self.page.SND_NORMAL, self.page.SND_MAXIMUM, self.page.SND_OFF]
        for opt in focus_options:
            self.page.click(opt)
            time.sleep(0.5)
        
        # 이퀄라이저 탭
        print("이퀄라이저 클릭 테스트...")
        self.page.scroll_and_find(self.page.SND_EQUALIZER)
        time.sleep(1)
        focus_options = [self.page.SND_ORIGINAL, self.page.SND_LOW, self.page.SND_GENTLY, self.page.SND_DYNAMIC, self.page.SND_VOICE, self.page.SND_SETTINGS, self.page.SND_ORIGINAL]
        for opt in focus_options:
            self.page.click(opt)
            time.sleep(0.5)
        # 주파수 대역 리스트
        equalizer_bands = [
            (self.page.SND_50HZ, "50Hz"),
            (self.page.SND_125HZ, "125Hz"),
            (self.page.SND_315HZ, "315Hz"),
            (self.page.SND_800HZ, "800Hz"),
            (self.page.SND_2KHZ, "2kHz"),
            (self.page.SND_5KHZ, "5kHz"),
            (self.page.SND_8KHZ, "8kHz")
        ]
        self.page.scroll_content_down()
        time.sleep(1)
        for locator, label in equalizer_bands:
            try:  
                rect = driver.find_element(*locator).rect     
                tx = rect['x'] + 35
                ty = rect['y'] - 360
                print(f"{label} 대역 조절 중...")
                self.page.swipe(tx, ty, tx, ty - 280, 500) # 올리기
                time.sleep(0.5)
                self.page.swipe(tx, ty - 280, tx, ty + 280, 500) # 내리기
                time.sleep(0.5)
            except Exception as e:
                pytest.fail(f"{label} 조절 실패: {e}")
        
        TODO("에러 많아 수정 필요....")
        print("이퀄라이저 초기화 테스트...")
        # 초기화 버튼 위치 확보를 위한 미세 스크롤
        self.page.swipe(0.536*1920, 0.509*1080, 0.536*1920, 0.240*1080, 1000)
        time.sleep(1)
        self.page.click(self.page.SND_INITIAL)
        time.sleep(1)

    def test_phone_projection_sound_flow(self, driver):
        """
        [시나리오] 안드로이드 오토(폰 프로젝션) 전용 사운드 설정 확인 및 복귀
        """
        print("\n[Test] 폰 프로젝션(Android Auto) 사운드 테스트 시작")
        
        # 하단 폰 프로젝션 영역 이동
        for _ in range(7):
            self.page.scroll_content_down()
        time.sleep(2)

        print("안드로이드 오토 메뉴 진입 중...")
        self.page.click(self.page.SND_ANDROID)
        time.sleep(2)
        # 뒤로가기 버튼 클릭 (안드로이드 오토 타이틀 옆 좌표 기반)
        print("안드로이드 오토 설정에서 사운드 메인으로 복귀...")
        self.page.scroll_up()
        time.sleep(1)
        self.page.toggle_tap(self.page.SND_ANDROID, x_offset=-40, y_offset=20)
        time.sleep(2)

        if self.page.is_displayed(self.page.SND_CONNECTING):
             print("성공: 사운드 메인 화면으로 복귀했습니다.")
        else:
             pytest.fail("오류: 사운드 메인 화면으로 복귀하지 못했습니다.")
        
        self.page.click(self.page.SND_ANDROID)
        time.sleep(2)

        # 1. 조용한 모드 토글 테스트
        print("조용한 모드 토글 테스트 (On/Off)...")
        for i in range(2):
            self.page.toggle_tap(self.page.SND_QUIET, x_offset=-60, y_offset=10)
            time.sleep(1)

        # 2. 개별 음량 조절 테스트 (시스템/벨소리 등)
        print("음량 슬라이더 조절 테스트 중...")
        target_locators = [
            (self.page.SND_SYSTEM, "시스템 음량"),
            #(self.page.SND_MEDIA, "미디어 음량"),
            #(self.page.SND_NAVIGATION, "내비게이션 음량"),
            (self.page.SND_RINGTONE, "벨소리 음량")
        ]
        for locator, label in target_locators:
            try:  
                rect_v = driver.find_element(*locator).rect     
                base_x = rect_v['x'] + 100
                base_y = rect_v['y'] + 80
                max_x = rect_v['x'] + 530
                
                print(f"{label} 스와이프 올리기...")
                self.page.swipe(base_x, base_y, max_x, base_y, 1000)
                time.sleep(1)
                
                print(f"{label} 스와이프 내리기...")
                self.page.swipe(max_x - 50, base_y, base_x - 50, base_y, 1000)  
                time.sleep(1)
                
                print(f"{label} 볼륨 높이기 (탭 12회)...")
                for _ in range(12):
                    self.page.tap_coordinates(max_x, base_y)
                    time.sleep(0.1)
                
                print(f"{label} 볼륨 낮추기 (탭 9회)...")
                for _ in range(9):
                    self.page.tap_coordinates(base_x - 50, base_y)
                    time.sleep(0.1)
                
                print(f"{label} 음소거 토글...")
                for _ in range(2):
                    self.page.tap_coordinates(max_x + 100, base_y)
                    time.sleep(1)
            except Exception as e:
                print(f"{label} 동작 테스트 실패: {e}")

        """
        통화/안내 등 중단 음량 조절 동작 테스트 (스크롤 다운 후 진행)
        """
        # 아래로 스크롤
        print("아래로 스크롤 중...")
        self.page.scroll_content_down()
        time.sleep(2)

        bottomevolume = [
            (self.page.SND_CALL, "통화 음량"),
            #(self.page.SND_GUIDE, "음성 안내 음량"),
        ]
        for locator, label in bottomevolume:
            try:  
                rect_v = driver.find_element(*locator).rect    
                base_x = rect_v['x'] + 100
                base_y = rect_v['y'] + 80
                max_x = rect_v['x'] + 530
                
                print(f"{label} 스와이프 올리기...")
                self.page.swipe(base_x, base_y, max_x, base_y, 1000)
                time.sleep(1)
                
                print(f"{label} 스와이프 내리기...")
                self.page.swipe(max_x - 50, base_y, base_x - 50, base_y, 1000)  
                time.sleep(1)
                
                print(f"{label} 볼륨 높이기 (탭 12회)...")
                for _ in range(12):
                    self.page.tap_coordinates(max_x, base_y)
                    time.sleep(0.1)
                
                print(f"{label} 볼륨 낮추기 (탭 9회)...")
                for _ in range(9):
                    self.page.tap_coordinates(base_x - 50, base_y)
                    time.sleep(0.1)
            except Exception as e:
                print(f"{label} 동작 테스트 실패: {e}")
        time.sleep(1)
        auto_options = [self.page.SND_OFF, self.page.SND_WEAKLY, self.page.SND_MIDDLE, self.page.SND_STRONG, self.page.SND_OFF]
        for opt in auto_options:
            self.page.click(opt)
            time.sleep(0.5)

        print("사운드 시나리오 테스트 완료!")
