# -*- coding: utf-8 -*-
"""
===========================================================================
                     IVI OS 전체 탭 순차 테스트 스위트
===========================================================================
이 파일은 모든 탭 시나리오를 순서대로 실행하는 마스터 테스트 스위트입니다.

실행 방법:
    pytest -s tests/test_all_tabs_scenario.py -v

테스트 순서 (21개):
    1.  Quick Settings (빠른 설정)
    2.  Lights (라이트)
    3.  AD (자율주행)
    4.  Driving (주행)
    5.  Lock (잠금) - 테스트 비활성화
    6.  Seat (좌석)
    7.  Climate (공조)
    8.  Charging (충전)
    9.  Navigation (네비게이션)
    10. Gleo AI
    11. Display (화면)
    12. Sound (사운드)
    13. Profile (프로필)
    14. Convenience (편의 기능)
    15. Connection (연결)
    16. Apps (앱)
    17. Security (보안)
    18. Privacy (개인정보 보호)
    19. Hi-Pass (하이패스) - 테스트 비활성화
    20. General Settings (일반 설정)
    21. Vehicle Info (차량 정보)

주의사항:
    - 각 테스트는 독립적이지만 순차적으로 실행됩니다.
    - 테스트 실패 시 다음 테스트가 계속 진행됩니다.
    - 전체 실행 시간: 약 30-45분 예상
===========================================================================
"""

import pytest
import time
from pages.vehicle_control_page import VehicleControlPage
from tests.test_quick_settings_scenario import TestQuickSettingsScenario
from tests.test_lights_scenario import TestLightsScenario
from tests.test_ad_scenario import TestADScenario
from tests.test_driving_scenario import TestDrivingScenario
# from tests.test_lock_scenario import TestLockScenario
from tests.test_seat_scenario import TestSeatScenario
from tests.test_climate_scenario import TestClimateScenario
from tests.test_charging_scenario import TestChargingScenario
from tests.test_navigation_scenario import TestNavigationScenario
from tests.test_gleo_ai_scenario import TestGleoAIScenario
from tests.test_display_scenario import TestDisplayScenario
from tests.test_sound_scenario import TestSoundScenario
# from tests.test_profile_scenario import TestProfileScenario
from tests.test_convenience_scenario import TestConvenienceScenario
from tests.test_connection_scenario import TestConnectionScenario
from tests.test_apps_scenario import TestAppsScenario
from tests.test_security_scenario import TestSecurityScenario
from tests.test_privacy_scenario import TestPrivacyScenario
# from tests.test_hi_pass_scenario import TestHiPassScenario # 왜 못 찾냐고!!!!
from tests.test_general_settings_scenario import TestGeneralSettingsScenario
from tests.test_vehicle_info_scenario import TestVehicleInfoScenario

class TestAllTabsScenario:
    """
    모든 탭을 순서대로 테스트하는 마스터 테스트 클래스
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """각 테스트 전 페이지 객체 초기화"""
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        print("\n" + "="*60)
        print("🏃‍➡️🏃‍➡️🏃‍➡️ 전체 21개 탭 테스트 시작!")
        print("="*60)
        yield

    # # =========================================================================
    # # 1. Quick Settings (빠른 설정)
    # # =========================================================================
    # def test_01_quick_settings(self, driver):
    #     """[1/21] 빠른 설정 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[1/21] Quick Settings (빠른 설정) 테스트 시작")
    #     print("="*60)
        
    #     # 빠른 설정은 기본 화면이므로 별도 메뉴 클릭 불필요
    #     assert self.page.is_displayed(self.page.QS_ALL_WINDOWS), "빠른 설정 화면이 로드되지 않았습니다."
    #     print("✓ 빠른 설정 화면 로드 확인")
    #     print("빠른 설정 테스트 시작")
    #     TestQuickSettingsScenario.test_quick_settings(driver)
    #     print("빠른 설정 테스트 종료")

    # # =========================================================================
    # # 2. Lights (라이트)
    # # =========================================================================
    # def test_02_lights(self, driver):
    #     """[2/21] 라이트 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[2/21] Lights (라이트) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("라이트")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.LIGHT_HEADLIGHT), "라이트 화면이 로드되지 않았습니다."
    #     print("✓ 라이트 화면 로드 확인")
    #     print("라이트 테스트 시작")
    #     TestLightsScenario.test_headlights()
    #     TestLightsScenario.test_frunk_trunk_lights()
    #     TestLightsScenario.test_interior_lights()
    #     TestLightsScenario.test_mood_lights()
    #     print("라이트 테스트 종료")


    # # =========================================================================
    # # 3. AD (자율주행)
    # # =========================================================================
    # def test_03_ad(self, driver):
    #     """[3/21] 자율주행 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[3/21] AD (자율주행) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("AD")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.AD_MODE_TITLE), "AD 화면이 로드되지 않았습니다."
    #     print("✓ AD 화면 로드 확인")

    #     print("AD 테스트 시작")
    #     TestADScenario.test_ad_speed_offset()
    #     print("AD 테스트 종료")

    # # =========================================================================
    # # 4. Driving (주행)
    # # =========================================================================
    # def test_04_driving(self, driver):
    #     """[4/21] 주행 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[4/21] Driving (주행) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("주행")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.DRIVING_MODE_STYLE), "주행 화면이 로드되지 않았습니다."
    #     print("✓ 주행 화면 로드 확인")
        
    #     print("주행 테스트 시작")
    #     TestDrivingScenario.setup()
    #     TestDrivingScenario.test_driving_convenience_toggles()
    #     TestDrivingScenario.test_driving_safety_settings()
    #     TestDrivingScenario.test_driving_parking_brake()
    #     print("주행 테스트 종료")

    # # =========================================================================
    # # 5. Lock (잠금)
    # # =========================================================================
    # # def test_05_lock(self, driver): #현재 활성화 되지 않음
    # #     """[5/21] Lock 탭 테스트"""
    # #     print("\n" + "="*60)
    # #     print("[5/21] Lock (잠금) 테스트 시작")
    # #     print("="*60)
        
    # #     self.page.click_sidebar_menu("잠금")
    # #     time.sleep(2)
    # #     assert self.page.is_displayed(self.page.LOCK_TITLE), "잠금 화면이 로드되지 않았습니다."
    # #     print("✓ 잠금 화면 로드 확인")

    # # =========================================================================
    # # 6. Seat (시트 포지션)
    # # =========================================================================
    # def test_06_seat(self, driver):
    #     """[6/21] 좌석 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[6/21] Seat (시트 포지션) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("시트 포지션")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.SEAT_TITLE), "시트 포지션 화면이 로드되지 않았습니다."
    #     print("✓ 시트 포지션 화면 로드 확인")
    #     print("시트 포지션 테스트 시작")
    #     TestSeatScenario.test_seat_part_selection()
    #     TestSeatScenario.test_seat_detail_adjustment()
    #     print("시트 포지션 테스트 종료")

    # # =========================================================================
    # # 7. Climate (공조)
    # # =========================================================================
    # def test_07_climate(self, driver):
    #     """[7/21] 공조 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[7/21] Climate (공조) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("공조")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.CLIMATE_AUTO_RECIRC), "공조 화면이 로드되지 않았습니다."
    #     print("✓ 공조 화면 로드 확인")

    #     print("공조 테스트 시작")
    #     TestClimateScenario.test_climate_feature_toggles()
    #     print("공조 테스트 종료")

    # # =========================================================================
    # # 8. Charging (충전)
    # # =========================================================================
    # def test_08_charging(self, driver):
    #     """[8/21] 충전 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[8/21] Charging (충전) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("충전")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.CHARGING_REMAINING), "충전 화면이 로드되지 않았습니다."
    #     print("✓ 충전 화면 로드 확인")

    #     print("충전 테스트 시작")
    #     TestChargingScenario.test_charging_layout()
    #     TestChargingScenario.test_connector_lock_flow()
    #     TestChargingScenario.test_charging_limits_flow()
    #     TestChargingScenario.test_charging_current_flow()
    #     print("충전 테스트 종료")

    # # =========================================================================
    # # 9. Navigation (내비게이션)
    # # =========================================================================
    # def test_09_navigation(self, driver):
    #     """[9/21] Navigation (내비게이션) 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[9/21] Navigation (내비게이션) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("내비게이션")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.NAV_CHARGING_STATION), "내비게이션 화면이 로드되지 않았습니다."
    #     print("✓ 내비게이션 화면 로드 확인")

    #     print("내비게이션 테스트 시작")
    #     TestNavigationScenario.test_navigation_layout()
    #     TestNavigationScenario.test_ev_route_switch_flow()
    #     TestNavigationScenario.test_initialize_popup_flow()
    #     print("내비게이션 테스트 종료")

    # # =========================================================================
    # # 10. Gleo AI
    # # =========================================================================
    # def test_10_gleo_ai(self, driver):
    #     """[10/21] Gleo AI 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[10/21] Gleo AI 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("Gleo AI")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.GLEO_TITLE), "Gleo AI 화면이 로드되지 않았습니다."
    #     print("✓ Gleo AI 화면 로드 확인")

    #     print("Gleo AI 테스트 시작")
    #     TestGleoAIScenario.test_gleo_layout()
    #     TestGleoAIScenario.test_voice_types_flow()
    #     TestGleoAIScenario.test_gleo_calling_popup_flow()
    #     TestGleoAIScenario.test_style_and_seats_flow()
    #     print("Gleo AI 테스트 종료")

    # # =========================================================================
    # # 11. Display (화면)
    # # =========================================================================
    # def test_11_display(self, driver):
    #     """[11/21] Display (화면) 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[11/21] Display (화면) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("화면")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.DIS_THEME), "화면 설정이 로드되지 않았습니다."
    #     print("✓ 화면 설정 로드 확인")

    #     print("화면 테스트 시작")
    #     TestDisplayScenario.test_display_layout()
    #     TestDisplayScenario.test_theme_interactions_flow()
    #     TestDisplayScenario.test_brightness_adjustments_flow()
    #     TestDisplayScenario.test_cleaning_mode_flow()
    #     print("화면 테스트 종료")

    # # =========================================================================
    # # 12. Sound (사운드)
    # # =========================================================================
    # def test_12_sound(self, driver):
    #     """[12/21] Sound (사운드) 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[12/21] Sound (사운드) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("사운드")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.SND_VOLUME), "사운드 화면이 로드되지 않았습니다."
    #     print("✓ 사운드 화면 로드 확인")

    #     print("사운드 테스트 시작")
    #     TestSoundScenario.test_sound_layout()
    #     TestSoundScenario.test_volume_control_flow()
    #     TestSoundScenario.test_automatic_and_focus_flow()
    #     TestSoundScenario.test_equalizer_adjustment_flow()
    #     TestSoundScenario.test_phone_projection_sound_flow()
    #     print("사운드 테스트 종료")

    # # =========================================================================
    # # 13. Profile (프로필)
    # # =========================================================================
    # # def test_13_profile(self, driver):
    # #     """[13/21] Profile (프로필) 탭 테스트"""
    # #     print("\n" + "="*60)
    # #     print("[13/21] Profile (프로필) 테스트 시작")
    # #     print("="*60)
        
    # #     self.page.click_sidebar_menu("프로필")
    # #     time.sleep(2)
    # #     assert self.page.is_displayed(self.page.PROFILE_SETTINGS), "프로필 화면이 로드되지 않았습니다."
    # #     print("✓ 프로필 화면 로드 확인")

    # #     print("프로필 테스트 시작")
    # #     TestProfileScenario.test_profile_entry_and_check()
    # #     TestProfileScenario.test_add_profile_flow()
    # #     print("프로필 테스트 종료")

    # # =========================================================================
    # # 14. Convenience (편의 기능)
    # # =========================================================================
    # def test_14_convenience(self, driver):
    #     """[14/21] Convenience (편의 기능) 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[14/21] Convenience (편의 기능) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("편의 기능")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.CONVENIENCE_TITLE), "편의 기능 화면이 로드되지 않았습니다."
    #     print("✓ 편의 기능 화면 로드 확인")

    #     print("편의 기능 테스트 시작")
    #     TestConvenienceScenario.test_convenience_layout()
    #     TestConvenienceScenario.test_car_wash_mode_flow()
    #     TestConvenienceScenario.test_camping_mode_flow()
    #     TestConvenienceScenario.test_double_parking_mode_flow()
    #     TestConvenienceScenario.test_towing_mode_flow()
    #     TestConvenienceScenario.test_standby_mode_flow()
    #     print("편의 기능 테스트 종료")

    # # =========================================================================
    # # 15. Connection (연결)
    # # =========================================================================
    # def test_15_connection(self, driver):
    #     """[15/21] Connection (연결) 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[15/21] Connection (연결) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("연결")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.CONNECTION_TITLE), "연결 화면이 로드되지 않았습니다."
    #     print("✓ 연결 화면 로드 확인")

    #     print("연결 테스트 시작")
    #     TestConnectionScenario.test_connection_layout()
    #     TestConnectionScenario.test_bluetooth_flow()
    #     TestConnectionScenario.test_wifi_flow()
    #     TestConnectionScenario.test_hotspot_flow()
    #     TestConnectionScenario.test_mobile_data_flow()
    #     print("연결 테스트 종료")

    # # =========================================================================
    # # 16. Apps (앱)
    # # =========================================================================
    # def test_16_apps(self, driver):
    #     """[16/21] Apps (앱) 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[16/21] Apps (앱) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("앱")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.APPS_TITLE), "앱 화면이 로드되지 않았습니다."
    #     print("✓ 앱 화면 로드 확인")

    #     print("앱 테스트 시작")
    #     TestAppsScenario.test_apps_collection_and_layout()
    #     TestAppsScenario.test_apps_detail_interaction_flow()
    #     TestAppsScenario.test_apps_termination_popup_flow()
    #     TestAppsScenario.test_downloaded_apps_interaction_flow()
    #     print("앱 테스트 종료")

    # # =========================================================================
    # # 17. Security (보안)
    # # =========================================================================
    # def test_17_security(self, driver):
    #     """[17/21] Security (보안) 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[17/21] Security (보안) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("보안")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.SECURITY_RECORDING_OPTIONS), "보안 화면이 로드되지 않았습니다."
    #     print("✓ 보안 화면 로드 확인")

    #     print("보안 테스트 시작")
    #     TestSecurityScenario.test_security_layout()
    #     TestSecurityScenario.test_recording_toggles_flow()
    #     print("보안 테스트 종료")

    # # =========================================================================
    # # 18. Privacy (개인정보 보호)
    # # =========================================================================
    # def test_18_privacy(self, driver):
    #     """[18/21] Privacy (개인정보 보호) 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[18/21] Privacy (개인정보 보호) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("개인정보 보호")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.PRIVACY_TITLE), "개인정보 보호 화면이 로드되지 않았습니다."
    #     print("✓ 개인정보 보호 화면 로드 확인")

    #     print("개인정보 보호 테스트 시작")
    #     TestPrivacyScenario.test_mic_usage()
    #     TestPrivacyScenario.test_location_usage()
    #     TestPrivacyScenario.test_camera_usage()
    #     TestPrivacyScenario.test_use_reset()
    #     print("개인정보 보호 테스트 종료")

    # # =========================================================================
    # # 19. Hi-Pass (하이패스)
    # # =========================================================================
    # # def test_19_hi_pass(self, driver): #현재 활성화 되지 않음
    # #     """[19/21] Hi-Pass (하이패스) 탭 테스트"""
    # #     print("\n" + "="*60)
    # #     print("[19/21] Hi-Pass (하이패스) 테스트 시작")
    # #     print("="*60)
        
    # #     self.page.click_sidebar_menu("하이패스")
    # #     time.sleep(2)
    # #     assert self.page.is_displayed(self.page.HIPASS_PAYMENT_INFO), "하이패스 화면이 로드되지 않았습니다."
    # #     print("✓ 하이패스 화면 로드 확인")


    # # =========================================================================
    # # 20. General Settings (일반 설정)
    # # =========================================================================
    # def test_20_general_settings(self, driver):
    #     """[20/21] General Settings (일반 설정) 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[20/21] General Settings (일반 설정) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("일반 설정")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.GENERAL_FONT_SETTING), "일반 설정 화면이 로드되지 않았습니다."
    #     print("✓ 일반 설정 화면 로드 확인")

    #     print("일반 설정 테스트 시작")
    #     TestGeneralSettingsScenario.test_font_settings()
    #     TestGeneralSettingsScenario.test_language_settings()
    #     TestGeneralSettingsScenario.test_date_time_settings()
    #     TestGeneralSettingsScenario.test_unit_settings()
    #     print("일반 설정 테스트 종료")

    # # =========================================================================
    # # 21. Vehicle Info (차량 정보)
    # # =========================================================================
    # def test_21_vehicle_info(self, driver):
    #     """[21/21] 차량 정보 탭 테스트"""
    #     print("\n" + "="*60)
    #     print("[21/21] Vehicle Info (차량 정보) 테스트 시작")
    #     print("="*60)
        
    #     self.page.click_sidebar_menu("차량 정보")
    #     time.sleep(2)
    #     assert self.page.is_displayed(self.page.VI_CONNECT), "차량 정보 화면이 로드되지 않았습니다."
    #     print("✓ 차량 정보 화면 로드 확인")

    #     print("차량 정보 테스트 시작")
    #     TestVehicleInfoScenario.test_vehicle_info_layout()
    #     TestVehicleInfoScenario.test_vehicle_info_flow()
    #     print("차량 정보 테스트 종료")

        
    #     print("\n" + "="*60)
    #     print("🎉 전체 21개 탭 테스트 완료!")
    #     print("="*60)

    # print("\n" + "="*60)
    # print("🎉 전체 21개 탭 테스트 완료!")
    # print("="*60)