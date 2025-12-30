import time
from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from config import AppConfig

class VehicleControlPage(BasePage):
    # Real Locators based on Compose Text attributes
    TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='빠른 설정']")

    # Left Menu Items
    MENU_QUICK_SETTINGS = (AppiumBy.XPATH, "//android.widget.TextView[@text='빠른 설정']")
    MENU_LIGHTS = (AppiumBy.XPATH, "//android.widget.TextView[@text='라이트']")
    MENU_AD = (AppiumBy.XPATH, "//android.widget.TextView[@text='AD']")
    MENU_DRIVING = (AppiumBy.XPATH, "//android.widget.TextView[@text='주행']")
    MENU_LOCK = (AppiumBy.XPATH, "//android.widget.TextView[@text='잠금']")
    MENU_SEAT = (AppiumBy.XPATH, "//android.widget.TextView[@text='시트 포지션']")
    MENU_CLIMATE = (AppiumBy.XPATH, "//android.widget.TextView[@text='공조']")
    MENU_CHARGING = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전']")
    MENU_NAVIGATION = (AppiumBy.XPATH, "//android.widget.TextView[@text='내비게이션']")
    MENU_GLEO_AI = (AppiumBy.XPATH, "//android.widget.TextView[@text='Gleo AI']")
    MENU_SCREEN = (AppiumBy.XPATH, "//android.widget.TextView[@text='화면']")
    MENU_SOUND = (AppiumBy.XPATH, "//android.widget.TextView[@text='사운드']")
    MENU_PROFILE = (AppiumBy.XPATH, "//android.widget.TextView[@text='프로필']")
    MENU_CONVENIENCE = (AppiumBy.XPATH, "//android.widget.TextView[@text='편의 기능']")
    MENU_CONNECTION = (AppiumBy.XPATH, "//android.widget.TextView[@text='연결']")
    MENU_APPS = (AppiumBy.XPATH, "//android.widget.TextView[@text='앱']")
    MENU_SECURITY = (AppiumBy.XPATH, "//android.widget.TextView[@text='보안']")
    MENU_PRIVACY = (AppiumBy.XPATH, "//android.widget.TextView[@text='개인정보 보호']")
    MENU_HIPASS = (AppiumBy.XPATH, "//android.widget.TextView[@text='하이패스']")
    MENU_GENERAL = (AppiumBy.XPATH, "//android.widget.TextView[@text='일반 설정']")
    MENU_VEHICLE_INFO = (AppiumBy.XPATH, "//android.widget.TextView[@text='차량 정보']")
    
    # Quick Settings (빠른 설정) - Right Panel Elements
    Quick_Settings_IconBtn ={
        "사이드 미러 개폐":(0.880, 0.232), # Text Center Y=690 -> 0.639
        "충전 포트":(0.948,0.232), 
        "프렁크":(0.784,0.327),    
        "라이트 끄기":(0.565, 0.441),  # Row Center Y=476 -> 0.441
        "라이트 자동":(0.616, 0.441),
        "라이트 미등":(0.667, 0.441),
        "라이트 전조등":(0.717, 0.441),
        "라이트 자동 전조등":(0.783,0.441), 
        "전방 와이퍼 1단":(0.578, 0.540), # Row Center Y=583 -> 0.540
        "전방 와이퍼 2단":(0.662, 0.540),
        "전방 와이퍼 자동":(0.725, 0.540),
        "전방 와이퍼 워셔액":(0.781,0.540), 
        "후방 와이퍼 1단":(0.578, 0.639), # Row Center Y=690 -> 0.639
        "후방 와이퍼 2단":(0.662, 0.639),
        "후방 와이퍼 자동":(0.725, 0.639),
        "후방 와이퍼 워셔액":(0.781,0.639), 
    }

    QS_ALL_WINDOWS = (AppiumBy.XPATH, "//android.widget.TextView[@text='모든 창문']")
    QS_WINDOW_LOCK = (AppiumBy.XPATH, "//android.widget.TextView[@text='창문 잠금']")
    
    QS_TRUNK = (AppiumBy.XPATH, "//android.widget.TextView[@text='트렁크']")
    QS_CHILD_LOCK = (AppiumBy.XPATH, "//android.widget.TextView[@text='차일드락']")
    
    QS_DOOR_LOCK = (AppiumBy.XPATH, "//android.widget.TextView[@text='도어 잠금']")
    #사이드 미러 개폐
    #충전 포트
    #밝기 조절?
    #프렁크
    QS_SUNBLIND_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='선블라인드']")
    #라이트 끄기
    #라이트 자동
    #라이트 미등
    #라이트 전조등
    #라이트 자동 전조등
    QS_GLOVE_BOX = (AppiumBy.XPATH, "//android.widget.TextView[@text='글로브박스']")
    #전방 와이퍼 1단
    #전방 와이퍼 2단
    #전방 와이퍼 자동
    #전방 와이퍼 워셔액
    QS_STEERING_WHEEL = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전대']")
    #후방 와이퍼 1단
    #후방 와이퍼 2단
    #후방 와이퍼 자동
    #후방 와이퍼 워셔액
    QS_SIDE_MIRROR = (AppiumBy.XPATH, "//android.widget.TextView[@text='사이드 미러']")    
    # Common 'Auto' buttons - we will fetch all and distinguish by order/position
    QS_AUTO_LABEL = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동']")

    # Lights (라이트) - Right Panel Elements
    Lights_IconBtn = {
        "전조등 끄기":(0.583, 0.259),
        "전조등 자동":(0.666, 0.259),
        "전조등 미등":(0.750, 0.259),
        "전조등 켜짐":(0.833, 0.259),
        "자동 상향 전조등":(0.619, 0.338),
        "에스코트 조명":(0.554, 0.425), 
    }
    # Headlights (전조등) - 
    LIGHT_HEADLIGHT_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='전조등']/parent::*/parent::*//android.widget.TextView[@text='끄기']")
    LIGHT_HEADLIGHT_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='전조등']/parent::*/parent::*//android.widget.TextView[@text='자동']")
    
    # Frunk Lights (프렁크등) - Off/On/Auto
    # LIGHT_FRUNK_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='프렁크등']/parent::*/parent::*//android.widget.TextView[@text='끄기']")
    # LIGHT_FRUNK_ON = (AppiumBy.XPATH, "//android.widget.TextView[@text='프렁크등']/parent::*/parent::*//android.widget.TextView[@text='켜기']")
    # LIGHT_FRUNK_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='프렁크등']/parent::*/parent::*//android.widget.TextView[@text='자동']")

    LIGHT_FRUNK_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='끄기'][1]")
    LIGHT_FRUNK_ON = (AppiumBy.XPATH, "//android.widget.TextView[@text='켜기'][1]")
    LIGHT_FRUNK_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동'][1]")

    # Trunk Lights (트렁크등)
    LIGHT_TRUNK_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='트렁크등']/parent::*/parent::*//android.widget.TextView[@text='끄기'][2]")
    LIGHT_TRUNK_ON = (AppiumBy.XPATH, "//android.widget.TextView[@text='트렁크등']/parent::*/parent::*//android.widget.TextView[@text='켜기'][2]")
    LIGHT_TRUNK_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='트렁크등']/parent::*/parent::*//android.widget.TextView[@text='자동'][2]")

    # Interior Lights (실내등)
    # Header: //android.widget.TextView[@text='실내등']
    LIGHT_INTERIOR_ALL_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='끄기']")
    LIGHT_INTERIOR_ALL_SEATS = (AppiumBy.XPATH, "//android.widget.TextView[@text='모든 좌석']")
    LIGHT_INTERIOR_DRIVER = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전석']")
    LIGHT_INTERIOR_PASSENGER = (AppiumBy.XPATH, "//android.widget.TextView[@text='동승석']")
    LIGHT_INTERIOR_REAR_LEFT = (AppiumBy.XPATH, "//android.widget.TextView[@text='뒷좌석 좌측']")
    LIGHT_INTERIOR_REAR_RIGHT = (AppiumBy.XPATH, "//android.widget.TextView[@text='뒷좌석 우측']")

    # Mood Lights (무드 조명)
    LIGHT_MOOD_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='무드 조명']/following-sibling::*//android.widget.TextView[@text='끄기']")
    LIGHT_MOOD_ON = (AppiumBy.XPATH, "//android.widget.TextView[@text='무드 조명']/following-sibling::*//android.widget.TextView[@text='켜기']")
    LIGHT_MOOD_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='무드 조명']/following-sibling::*//android.widget.TextView[@text='자동']")
    LIGHT_MOOD_COLOR = (AppiumBy.XPATH, "//android.widget.TextView[@text='무드 조명']/following-sibling::*//android.widget.TextView[@text='색상']")
    LIGHT_MOOD_BRIGHTNESS = (AppiumBy.CLASS_NAME, "android.widget.SeekBar")
    LIGHT_MOOD_SAVE_BTN = (AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")


    # AD (주행지원) - Right Panel
    AD_MODE_PRO = (AppiumBy.XPATH, "//android.widget.TextView[@text='프로']")
    AD_MODE_MAX = (AppiumBy.XPATH, "//android.widget.TextView[@text='맥스']")
    AD_SPEED_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동 (제한 속도)']")
    AD_SPEED_CURRENT = (AppiumBy.XPATH, "//android.widget.TextView[@text='현재 속도']")
    AD_LANE_CHANGE_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동']")
    AD_LANE_CHANGE_CONFIRM = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전자 확인']")

    # Coordinates/Bounds based on XML: Minus ~[1100, 600], Plus ~[1500, 600] for 10km/h row
    # Using generic XPaths for views if possible or text relative
    # AD_SPEED_VALUE = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, 'km/h')]")
    AD_IconBtn = {
        "AD_SPEED_MINUS":(0.573, 0.555),
        "AD_SPEED_PLUS":(0.781, 0.555),
    }

    # Driving (주행) - Right Panel 
    Driving_IconBtn = {
        "DRIVING_SNOW_RAIN_ASSIST":(0.541, 0.375),
        "DRIVING_ESC":(0.541, 0.587),
        "DRIVING_AUTO_HOLD":(0.549, 0.495),
        "DRIVING_BLIND_SPOT_CAMERA":(0.572, 0.555),
        "DRIVING_PARKING_BRAKE":(0.572, 0.555),
    }
    DRIVING_ACCEL_MODE_GENTLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='부드럽게']")
    DRIVING_ACCEL_MODE_STANDARD = (AppiumBy.XPATH, "//android.widget.TextView[@text='표준']")
    DRIVING_ACCEL_MODE_FAST = (AppiumBy.XPATH, "//android.widget.TextView[@text='빠르게']")
    DRIVING_SNOW_RAIN_ASSIST = (AppiumBy.XPATH, "//android.widget.TextView[@text='눈/빗길 보조']")
    DRIVING_STEERING_MODE_STANDARD = (AppiumBy.XPATH, "//android.widget.TextView[@text='표준']")
    DRIVING_STEERING_MODE_LIGHT = (AppiumBy.XPATH, "//android.widget.TextView[@text='가볍게']")
    DRIVING_CREEP = (AppiumBy.XPATH, "//android.widget.TextView[@text='크립 모드']")
    DRIVING_ONE_PADAL_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='원페달 모드']")
    DRIVING_FORWARD_COLLISION_WARNING = (AppiumBy.XPATH, "//android.widget.TextView[@text='전방 충돌 경고']")
    DRIVING_FORWARD_COLLISION_WARNING_DELAY = (AppiumBy.XPATH, "//android.widget.TextView[@text='늦게']")
    DRIVING_FORWARD_COLLISION_WARNING_NOMAL = (AppiumBy.XPATH, "//android.widget.TextView[@text='보통']")
    DRIVING_FORWARD_COLLISION_WARNING_EARLY = (AppiumBy.XPATH, "//android.widget.TextView[@text='일찍']")
    DRIVING_LANE_DEPARTURE_WARNING = (AppiumBy.XPATH, "//android.widget.TextView[@text='차선 이탈 경고']")
    DRIVING_LANE_DEPARTURE_WARNING_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='끄기']")
    DRIVING_LANE_DEPARTURE_WARNING_ON = (AppiumBy.XPATH, "//android.widget.TextView[@text='경고만']")
    DRIVING_LANE_DEPARTURE_WARNING_ALL = (AppiumBy.XPATH, "//android.widget.TextView[@text='경고와 제어']")
    DRIVING_BLIND_SPOT_COLLISION_WARNING = (AppiumBy.XPATH, "//android.widget.TextView[@text='사각지대 충돌 경고']")
    DRIVING_BLIND_SPOT_COLLISION_WARNING_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='끄기']")
    DRIVING_BLIND_SPOT_COLLISION_WARNING_ON = (AppiumBy.XPATH, "//android.widget.TextView[@text='경고만']")
    DRIVING_BLIND_SPOT_COLLISION_WARNING_ALL = (AppiumBy.XPATH, "//android.widget.TextView[@text='경고와 제어']")
    DRIVING_BLIND_SPOT_CAMERA_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='사각지대 카메라']")
    DRIVING_EPB_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='전자식 파킹 브레이크 수동 조작']")
    DRIVING_EPB_BTN = (AppiumBy.XPATH, "//android.widget.TextView[@text='파킹 브레이크']")

    # Lock (잠금) - Right Panel    
    LOCK_UNLOCK_ALL = (AppiumBy.XPATH, "//android.widget.TextView[@text='모두']")
    LOCK_DRIVER_ONLY = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전석만']")

    # Seat (시트 포지션) - Right Panel
    SEAT_IconBtn = {
        "COMFORTABLE_RIDE":(0.554, 0.222),
    }

    # Seat Selection Touch Points (Relative Coordinates x, y)
    SEAT_TOUCH_POINTS = {
        "운전석": (0.677, 0.685),       # Front Left (Driver) 1290 730
        "이동식 콘솔": (0.677, 0.592),  # Center Console 1290 630
        "동승석": (0.677, 0.555),       # Front Right (Passenger) 1290 580
        "뒷좌석 좌측": (0.799, 0.685),  # Rear Left 1570 730
        "뒷좌석 우측": (0.799, 0.555),  # Rear Right 1290 590
    }

    SEAT_MEMORY_1 = (AppiumBy.XPATH, "//android.widget.TextView[@text='1']")
    SEAT_MEMORY_2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='2']")
    # SEAT_DRIVER locator might change depending on selection, so we rely on finding text dynamically
    SEAT_POSITION_SAVE = (AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
    SEAT_POSITION_RESTORE = (AppiumBy.XPATH, "//android.widget.TextView[@text='복원']")
    SEAT_POSITION_CLOSE = (AppiumBy.XPATH, "//android.widget.TextView[@text='접기']")
    SEAT_POSITION_OPEN = (AppiumBy.XPATH, "//android.widget.TextView[@text='펼치기']")
    SEAT_SIDE_MIRROR_ANGLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='사이드미러 각도']")
    SEAT_HANDLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전대']")
    SEAT_HANDLE_SAVE = (AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
    SEAT_HANDLE_RESTORE = (AppiumBy.XPATH, "//android.widget.TextView[@text='복원']")
    
    # Climate (공조) - Right Panel
    CLIMATE_AUTO_RECIRC = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동 내기 전환']")
    CLIMATE_WASHER = (AppiumBy.XPATH, "//android.widget.TextView[@text='워셔액 분사']")
    CLIMATE_TUNNEL = (AppiumBy.XPATH, "//android.widget.TextView[@text='터널 진입']")
    CLIMATE_AIR_QUALITY = (AppiumBy.XPATH, "//android.widget.TextView[@text='공기 질 저하']")
    CLIMATE_OVERHEAT = (AppiumBy.XPATH, "//android.widget.TextView[@text='실내 과열 방지']")
    CLIMATE_AUTO_DRY = (AppiumBy.XPATH, "//android.widget.TextView[@text='에어컨 자동 건조']")




    # Sound Tab Elements
    SOUND_VOLUME = (AppiumBy.XPATH, "//android.widget.TextView[@text='음량']")
    SOUND_QUIET_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='조용한 모드']")
    
    # Apps Tab Elements
    APPS_VIVALDI = (AppiumBy.XPATH, "//android.widget.TextView[@text='Vivaldi Browser']")
    APPS_WIDGET_HOME = (AppiumBy.XPATH, "//android.widget.TextView[@text='WidgetHomeScreen']")
    APPS_SMART_KEY = (AppiumBy.XPATH, "//android.widget.TextView[@text='스마트키 콘솔']")
    APPS_PHONE = (AppiumBy.XPATH, "//android.widget.TextView[@text='전화']")
    APPS_VEHICLE_SETTINGS = (AppiumBy.XPATH, "//android.widget.TextView[@text='차량 설정']")
    APPS_CAMERA = (AppiumBy.XPATH, "//android.widget.TextView[@text='카메라']")
    APPS_CLOUD_CAM = (AppiumBy.XPATH, "//android.widget.TextView[@text='클라우드캠']")
    APPS_APPIUM_SETTINGS = (AppiumBy.XPATH, "//android.widget.TextView[@text='Appium Settings']")
    APPS_DEFAULT_APPS = (AppiumBy.XPATH, "//android.widget.TextView[@text='기본 앱']")

    # Profile Screen Locators
    PROFILE_SETTINGS_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='프로필 설정']")
    DRIVER_PROFILE = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전자 1']")
    PROFILE_IMAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='프로필 이미지']")
    LINK_ACCOUNT = (AppiumBy.XPATH, "//android.widget.TextView[@text='계정 연동']")
    KEY_MANAGEMENT = (AppiumBy.XPATH, "//android.widget.TextView[@text='디지털 키 관리']")
    DELETE_PROFILE = (AppiumBy.XPATH, "//android.widget.TextView[@text='프로필 삭제']")

    # Convenience Screen Locators
    CONVENIENCE_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='편의 기능']")
    CAR_WASH_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='세차 모드']")
    VALET_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='발레 모드']")
    CAMPING_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='캠핑 모드']")
    PET_CARE_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='펫 케어 모드']")
    DOUBLE_PARKING_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='이중 주차 모드']")
    TOWING_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='견인 모드']")
    STANDBY_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='대기 모드']")

    # Connection Screen Locators
    CONNECTION_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='연결']")
    BLUETOOTH = (AppiumBy.XPATH, "//android.widget.TextView[@text='블루투스']")
    WIFI = (AppiumBy.XPATH, "//android.widget.TextView[@text='Wi-Fi']")
    WIFI_HOTSPOT = (AppiumBy.XPATH, "//android.widget.TextView[@text='Wi-Fi 핫스팟']")
    MOBILE_DATA = (AppiumBy.XPATH, "//android.widget.TextView[@text='모바일 데이터']")

    # Apps Screen Locators
    APPS_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='앱']")
    ANDROID_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='Android Auto']")
    CARPLAY = (AppiumBy.XPATH, "//android.widget.TextView[@text='CarPlay']")
    GLEO_AI_APP = (AppiumBy.XPATH, "//android.widget.TextView[@text='Gleo AI']")
    # Locator for Gleo AI detail/info button (button sibling)
    GLEO_AI_DETAIL_BTN = (AppiumBy.XPATH, "//android.widget.TextView[@text='Gleo AI']/following-sibling::android.view.View//android.widget.Button")

    # Security Screen Locators
    SECURITY_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='보안']")
    RECORDING_OPTIONS = (AppiumBy.XPATH, "//android.widget.TextView[@text='녹화 옵션']")
    DRIVING_RECORDING = (AppiumBy.XPATH, "//android.widget.TextView[@text='주행 중']")
    PARKING_RECORDING = (AppiumBy.XPATH, "//android.widget.TextView[@text='주차 중']")
    EVENT_RECORDING = (AppiumBy.XPATH, "//android.widget.TextView[@text='이벤트 녹화']")
    CONST_RECORDING = (AppiumBy.XPATH, "//android.widget.TextView[@text='상시 녹화']")

    # Privacy Screen Locators
    PRIVACY_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='개인정보 보호']")
    PERMISSION_CONTROL = (AppiumBy.XPATH, "//android.widget.TextView[@text='권한 제어']")
    MIC_USAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='마이크 사용']")
    LOCATION_USAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='위치 정보 사용']")
    CAMERA_USAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='실내 카메라 사용']")

    # Hi-Pass Screen Locators
    HIPASS_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='하이패스']")
    PAYMENT_INFO = (AppiumBy.XPATH, "//android.widget.TextView[@text='결제 정보']")
    BALANCE = (AppiumBy.XPATH, "//android.widget.TextView[@text='잔액']")
    RECENT_HISTORY = (AppiumBy.XPATH, "//android.widget.TextView[@text='최근 결제 내역']")
    PAYMENT_DISPLAY = (AppiumBy.XPATH, "//android.widget.TextView[@text='결제 표시']")

    # General (일반 설정) - Font Setting
    FONT_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='글꼴']")
    FONT_DROPDOWN = (AppiumBy.XPATH, "//android.widget.TextView[@text='글꼴']/following-sibling::android.view.View")
    FONT_SETTING_BASIC = (AppiumBy.XPATH, "//android.widget.TextView[@text='기본']")
    FONT_SETTING_HYUNDAI = (AppiumBy.XPATH, "//android.widget.TextView[@text='현대']")
    FONT_SETTING_KIA = (AppiumBy.XPATH, "//android.widget.TextView[@text='기아']")
    FONT_SETTING_GENESIS = (AppiumBy.XPATH, "//android.widget.TextView[@text='제네시스']")
    FONT_SETTING_APPLY = (AppiumBy.XPATH, "//android.widget.TextView[@text='적용']")
    
    # General (일반 설정) - Language Setting
    LANGUAGE_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='언어']")
    LANGUAGE_DROPDOWN = (AppiumBy.XPATH, "//android.widget.TextView[@text='언어']/following-sibling::android.view.View")
    LANGUAGE_SETTING_KO = (AppiumBy.XPATH, "//android.widget.TextView[@text='한국어']")
    LANGUAGE_SETTING_EN = (AppiumBy.XPATH, "//android.widget.TextView[@text='English']")
    LANGUAGE_SETTING_ZH = (AppiumBy.XPATH, "//android.widget.TextView[@text='中文']")
    LANGUAGE_SETTING_JP = (AppiumBy.XPATH, "//android.widget.TextView[@text='日本語']")
    LANGUAGE_SETTING_DE = (AppiumBy.XPATH, "//android.widget.TextView[@text='Deutsch']")
    LANGUAGE_SETTING_FR = (AppiumBy.XPATH, "//android.widget.TextView[@text='Français']")
    LANGUAGE_SETTING_ES = (AppiumBy.XPATH, "//android.widget.TextView[@text='Español']")
    
    # General (일반 설정) - Time Setting
    AUTO_TIME_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동 시간 설정']")
    DATE_TIME_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='날짜 및 시간 설정']")
    MANUAL_TIME_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='설정']")
    MANUAL_TIME_TYPE_12 = (AppiumBy.XPATH, "//android.widget.TextView[@text='12시간']")
    MANUAL_TIME_TYPE_24 = (AppiumBy.XPATH, "//android.widget.TextView[@text='24시간']")

    # Date & Time
    AUTO_TIME_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동 시간 설정']")
    AUTO_TIME_TOGGLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동 시간 설정']/preceding-sibling::android.view.View")

    DATE_TIME_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='날짜 및 시간 설정']")    # "Settings" button to the right. 
    DATE_TIME_SET_BTN = (AppiumBy.XPATH, "//android.widget.TextView[@text='날짜 및 시간 설정']/following-sibling::android.widget.TextView[@text='설정']")
    
    TIME_FORMAT_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='시간 형식']")
    
    # Popups (Date/Time)
    POPUP_TITLE_DATE_TIME = (AppiumBy.XPATH, "//android.widget.TextView[@text='날짜 및 시간 설정']")
    POPUP_CONFIRM = (AppiumBy.XPATH, "//android.widget.TextView[@text='확인']")
    POPUP_CANCEL = (AppiumBy.XPATH, "//android.widget.TextView[@text='취소']")
    
    DATE_TIME = (AppiumBy.XPATH, "//android.widget.TextView[@text='날짜 및 시간']")
    
    # General (일반 설정) - Display Setting
    SUB_SPEED_DISPLAY = (AppiumBy.XPATH, "//android.widget.TextView[@text='보조속도 표시']")
    DISTANCE = (AppiumBy.XPATH, "//android.widget.TextView[@text='거리']")
    DISTANCE_KM = (AppiumBy.XPATH, "//android.widget.TextView[@text='km']")
    DISTANCE_MILE = (AppiumBy.XPATH, "//android.widget.TextView[@text='mile']")
    TEMPERATURE = (AppiumBy.XPATH, "//android.widget.TextView[@text='온도']")
    TEMPERATURE_C = (AppiumBy.XPATH, "//android.widget.TextView[@text='℃']")
    TEMPERATURE_F = (AppiumBy.XPATH, "//android.widget.TextView[@text='℉']")
    CONSUMPTION = (AppiumBy.XPATH, "//android.widget.TextView[@text='연비']")
    CONSUMPTION_L_100KM = (AppiumBy.XPATH, "//android.widget.TextView[@text='km/kWh']")
    CONSUMPTION_MILEAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='kWh/100km']")
    TIRE_PRESSURE = (AppiumBy.XPATH, "//android.widget.TextView[@text='타이어 공기압']")
    TIRE_PRESSURE_PSI = (AppiumBy.XPATH, "//android.widget.TextView[@text='psi']")
    TIRE_PRESSURE_KPA = (AppiumBy.XPATH, "//android.widget.TextView[@text='kpa']")
    TIRE_PRESSURE_BAR = (AppiumBy.XPATH, "//android.widget.TextView[@text='bar']")
    


    



    # Navigation Screen
    NAV_CHARGING_STATION = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전소']")
    NAV_EV_ROUTE = (AppiumBy.XPATH, "//android.widget.TextView[@text='EV 경로 계획']")
    NAV_PREF_STATION = (AppiumBy.XPATH, "//android.widget.TextView[@text='선호 충전소']")
    NAV_VERSION = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '2.3.0')]") # dynamic version check?

    # Gleo AI Screen
    GLEO_VOICE_1 = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 1']")
    GLEO_VOICE_2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 2']")
    GLEO_STYLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='대화 스타일']")
    GLEO_START = (AppiumBy.XPATH, "//android.widget.TextView[@text='바로 대화 시작']")


    # Vehicle Info (차량 정보) - Right side
    VEHICLE_INFO_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='차량 정보']")
    CONNECT = (AppiumBy.XPATH, "//android.widget.TextView[@text='Connect']")
    SOFTWARE_INFO = (AppiumBy.XPATH, "//android.widget.TextView[@text='소프트웨어 정보']")
    AUTO_UPDATE = (AppiumBy.XPATH, "//android.widget.TextView[@text='업데이트 자동 다운로드']")
    VIN = (AppiumBy.XPATH, "//android.widget.TextView[@text='차대 번호']")
    FACTORY_RESET = (AppiumBy.XPATH, "//android.widget.TextView[@text='공장 초기화']")
    INITIALIZE_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='초기화']")
    LEGAL_INFO = (AppiumBy.XPATH, "//android.widget.TextView[@text='법적 정보']")
    LEGAL_INFO_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='보기']")
    
    
    def start(self):
        """Starts the Vehicle Control Activity"""
        # Stop the app first to ensure a clean state
        try:
            self.driver.terminate_app(AppConfig.VEHICLE_CONTROL['package'])
        except:
            pass
            
        # Launch the Vehicle Control Activity
        self.driver.execute_script('mobile: startActivity', {
            'component': f"{AppConfig.VEHICLE_CONTROL['package']}/{AppConfig.VEHICLE_CONTROL['activity']}"
        })

    def is_loaded(self):
        # Check if the Title element is displayed
        return self.is_displayed(self.TITLE)

    
    
    # Lights Row (Approx Y=420-500)
    # Using specific hierarchy or bounds is brittle, but index 0 in that container is unique?
    # Let's verify presence of the RadioButton group for Lights.
    # We can assume the row below Sunblind / "AD" is Lights.
    
    


    

    GENERAL_INFO = (AppiumBy.XPATH, "//android.widget.TextView[@text='단말기 정보']")
    
    # Vehicle Info Tab Elements
    VEHICLE_INFO_SOFTWARE = (AppiumBy.XPATH, "//android.widget.TextView[@text='소프트웨어 정보']")
    
    # Gleo AI Tab Elements
    GLEO_WAKE_WORD = (AppiumBy.XPATH, "//android.widget.TextView[@text='바로 대화 시작']")
    GLEO_VOICE_STYLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='대화 스타일']")
    GLEO_VOICE_SEAT = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 인식 좌석']")
    
    # Screen (Hi-Pass/Display) content
    SCREEN_PAYMENT_INFO = (AppiumBy.XPATH, "//android.widget.TextView[@text='결제 정보']")
    SCREEN_SHOW_PAYMENT = (AppiumBy.XPATH, "//android.widget.TextView[@text='결제 표시']")
    SCREEN_SHOW_PAYMENT_TOGGLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='결제 표시']/preceding-sibling::android.view.View") # Toggle is sibling

    # Helper for sidebar navigation with Manual Swipe (User Request)
    def click_sidebar_menu(self, menu_text):
        target_menus = [
            "사운드", "프로필", "내비게이션", "Gleo AI",
            "편의 기능", "연결", "앱", "보안", "개인정보 보호", "하이패스", "일반 설정", "차량 정보"
        ]
        if menu_text in target_menus:
            print(f"Swiping sidebar up for '{menu_text}' (Manual)...")
            # Swipe from Bottom (800, 800) to Top (800, 300) to reveal bottom items
            self.driver.swipe(800, 800, 800, 300, 1000)
            time.sleep(1)
            
        print(f"Clicking '{menu_text}'...")
        try:
            self.driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[@text='{menu_text}']").click()
        except Exception:
            # Retry swipe if failed? or just fail.
            # Try one more swipe?
            print("Retry swipe...")
            self.driver.swipe(800, 800, 800, 300, 1000)
            time.sleep(1)
            try:
                self.driver.find_element(AppiumBy.XPATH, f"//android.widget.TextView[@text='{menu_text}']").click()
            except Exception as e:
                print(f"Final failure for '{menu_text}'. Dumping source...")
                safe_name = "debug_failure.xml"
                with open(safe_name, "w", encoding="utf-8") as f:
                    f.write(self.driver.page_source)
                raise e
    
    def scroll_to_bottom_sidebar(self):
        # Keeping this as legacy/manual helper
         self.driver.swipe(800, 900, 800, 200, 1000)
    
    
    def reset_sidebar(self):
        print("Resetting sidebar scroll to top (Manual Swipe)...")
        # Swipe Down (300 -> 900) to move content TOP-wards (i.e. scroll up)
        # Wait, Swipe Down (Start Top, End Bottom) moves content Down?
        # To see top items, we need to scroll UP the list?
        # Scroll View:
        # Items are [1, 2, 3... 10]
        # If we are at 10, we see [8, 9, 10].
        # We need to bring [1, 2, 3] into view.
        # This means dragging the content DOWN. 
        # So Finger moves from Top to Bottom?
        # Yes, Swipe (Start Y=300, End Y=900).
        for _ in range(3):
            self.driver.swipe(800, 300, 800, 900, 500)
            time.sleep(1)
            
    def scroll_down(self):
        """
        Performs a simple swipe up gesture to scroll down.
        Targeting the right panel (content area) which starts around x=1008.
        """
        size = self.driver.get_window_size()
        # Swipe in the right half of the screen
        start_x = size['width'] * 3 // 4 
        start_y = size['height'] * 3 // 4
        end_y = size['height'] // 4
        self.driver.swipe(start_x, start_y, start_x, end_y, 1000)

    def scroll_to_element(self, locator, max_scrolls=3):
        """
        Scrolls down until the element is visible.
        Returns True if found, False otherwise.
        """
        print(f"Scrolling to find element: {locator}")
        for i in range(max_scrolls + 1):
            if self.is_displayed(locator):
                print(f"Element found after {i} scrolls.")
                return True
            
            if i < max_scrolls:
                print(f"Scrolling down ({i+1}/{max_scrolls})...")
                self.scroll_down()
                time.sleep(1)
        
        print("Element not found after max scrolls.")
        return False

