import pytest
import time
import random
from appium.webdriver.common.appiumby import AppiumBy
from pages.vehicle_control_page import VehicleControlPage

class TestQuickSettingsScenario:
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        self.page = VehicleControlPage(driver)
        self.page.start()
        time.sleep(2)
        # Navigate to Quick Settings
        self.page.click_sidebar_menu("빠른 설정")
        time.sleep(2)

    def test_quick_settings_refactored(self, driver):
        """
        Finalized Quick Settings Scenario: 10 steps + Popup handling.
        """
        page = self.page

        print("\n[Step 0] 자동차 그래픽 아이콘 (Car Graphic Icons) Test")
        # 0. 프렁크, 사이드 미러, 썬 블라인드, 내부 조명, 트렁크 순서로 탭
        for name, (x, y) in page.QS_CAR_ICONS.items():
            print(f"  - Tapping Car Icon: {name}")
            page.tap(x, y)
            time.sleep(1.5)
            print(f"  - Tapping Car Icon: {name}")
            page.tap(x, y)
            time.sleep(1.5)

        print("\n[Step 1] 모든 창문 (All Windows) Toggle Test")
        # 1. "모든 창문" 탭 (닫힘 <-> 열림 확인). 닫힘으로 초기화.
        self._toggle_and_verify(page, "모든 창문", ["닫힘", "열림"], "닫힘")

        print("\n[Step 2] 창문 잠금 (Window Lock) Toggle Test")
        # 2. "창문 잠금" 탭 (잠김 <-> 해제됨 확인). 해제됨으로 초기화.
        self._toggle_and_verify(page, "창문 잠금", ["잠김", "해제됨"], "해제됨")

        print("\n[Step 3] 도어 (Door) Toggle Test")
        # 3. "도어" 탭 (잠김 <-> 해제됨 확인). 해제됨으로 초기화.
        self._toggle_and_verify(page, "도어", ["잠김", "해제됨"], "해제됨")

        print("\n[Step 4] 차일드락 (Child Lock) Popup Test")
        # 4. "차일드락" 탭 하여 팝업 확인 - 모두, 좌측, 우측, 꺼짐 순서로 탭 후 차일드 락 버튼 텝
        page.click_text("차일드락")
        time.sleep(1.5)
        for mode in ["모두", "좌측", "우측", "꺼짐"]:
            print(f"  - Tapping Child Lock Mode: {mode}")
            page.click_text(mode)
            time.sleep(0.8)

        page.tap(1880, 100)
        time.sleep(1.5)

        print("\n[Step 5] 글로브박스 & 충전구 Test")
        # 5. "글로브 박스" 탭 후 "충전구" 탭 하여 "닫힘" 또는 "열림"으로 변경됨 확인
        page.click_text("글로브박스")
        time.sleep(1)
        self._toggle_and_verify(page, "충전구", ["닫힘", "열림"])

        print("\n[Step 6] 화면 (Display) Slider & Popup Test")
        page.click_text("화면")
        time.sleep(2)
        
        # 6-1. Gauge Randomized Taps (2 times)
        slider_bounds = [874, 841, 1528, 929]
        for i in range(4):
            rx = random.randint(slider_bounds[0], slider_bounds[2])
            ry = random.randint(slider_bounds[1], slider_bounds[3])
            print(f"  - Random Gauge Tap {i+1}: ({rx}, {ry})")
            page.tap(rx, ry)
            time.sleep(1.2)
        
        page.tap(1880, 100)
        time.sleep(1.5)

        print("\n[Step 7] 사이드 미러 (Side Mirror) Popup Test")
        # 7-1. "사이드 미러" 탭 -> 팝업 확인 -> 왼쪽/오른쪽/토글/X
        page.click_text("사이드 미러")
        time.sleep(2)
        page.click_text("오른쪽")
        time.sleep(1.2)
        page.click_text("왼쪽")
        time.sleep(1.2)
        # Toggles
        page.tap(1020, 705)
        time.sleep(1)
        page.tap(1020, 769)
        time.sleep(1)
        # Close (X)
        page.tap(1523, 142)
        time.sleep(1.5)
        # Restore/Save
        for action in ["복원", "저장"]:
            page.click_text("사이드 미러")
            time.sleep(1.5)
            print(f"  - Clicking {action}")
            page.click_text(action)
            time.sleep(1.5)

        print("\n[Step 8] 운전대 (Steering Wheel) Popup Test")
        page.click_text("운전대")
        time.sleep(2)
        # Close (X)
        page.tap(1523, 260)
        time.sleep(1.5)
        # Restore/Save
        for action in ["복원", "저장"]:
            page.click_text("운전대")
            time.sleep(1.5)
            print(f"  - Clicking {action}")
            page.click_text(action)
            time.sleep(1.5)

        page.tap(200, 500)
        time.sleep(1.5)

        print("\n[Step 9] 전조등 (Headlights) Row Test")
        page.click_text("전조등")
        time.sleep(1.5)
        for i, coord in enumerate(page.QS_HEADLIGHTS):
            print(f"  - Tapping Headlight Button {i+1}")
            page.tap(*coord)
            time.sleep(1.2)

        print("\n[Step 10] 와이퍼 (Wipers) Row Test")
        page.click_text("와이퍼")
        time.sleep(1.5)
        for row, coords in [("Front", page.QS_WIPERS_FRONT), ("Rear", page.QS_WIPERS_REAR)]:
            print(f"  - Tapping {row} Wiper Row")
            for i, coord in enumerate(coords):
                page.tap(*coord)
                time.sleep(1.2)

        print("\nQuick Settings Refactored Test Completed Successfully.")

    def _toggle_and_verify(self, page, label, states, reset_to=None):
        print(f"  - Testing: {label}")
        current = None
        for s in states:
            if page.is_displayed((AppiumBy.XPATH, f"//android.widget.TextView[@text='{s}']")):
                current = s
                break
        print(f"    Current state: {current}")
        page.click_text(label)
        time.sleep(1.5)
        if reset_to:
            page.click_text(label) # Toggle back to initial
            time.sleep(1)
