from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class VehicleControlPage(BasePage):
    """
    차량 제어 페이지 (Vehicle Control Page) 객체입니다.
    좌측 사이드바 메뉴, 우측 콘텐츠 영역의 Locators와 동작을 정의합니다.
    """
    
    # === Locators (상수 정의) ===
    TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='빠른 설정']")

    # --- 좌측 사이드바 메뉴 ---
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
    
    # --- 빠른 설정 (Quick Settings) ------------------------------------------------------------------------
    QS_IconBtn = {
        "사이드 미러 개폐":(0.880, 0.232),
        "충전 포트":(0.948,0.232), 
        "프렁크":(0.784,0.327),    
        "라이트 끄기":(0.565, 0.441),
        "라이트 자동":(0.616, 0.441),
        "라이트 미등":(0.667, 0.441),
        "라이트 전조등":(0.717, 0.441),
        "라이트 자동 전조등":(0.783,0.441), 
        "전방 와이퍼 1단":(0.578, 0.540),
        "전방 와이퍼 2단":(0.662, 0.540),
        "전방 와이퍼 자동":(0.725, 0.540),
        "전방 와이퍼 워셔액":(0.781,0.540), 
        "후방 와이퍼 1단":(0.578, 0.639),
        "후방 와이퍼 2단":(0.662, 0.639),
        "후방 와이퍼 자동":(0.725, 0.639),
        "후방 와이퍼 워셔액":(0.781,0.639), 
    }

    QS_ALL_WINDOWS = (AppiumBy.XPATH, "//android.widget.TextView[@text='모든 창문']")
    QS_WINDOW_LOCK = (AppiumBy.XPATH, "//android.widget.TextView[@text='창문 잠금']")
    QS_TRUNK = (AppiumBy.XPATH, "//android.widget.TextView[@text='트렁크']")
    QS_CHILD_LOCK = (AppiumBy.XPATH, "//android.widget.TextView[@text='차일드락']")
    QS_DOOR_LOCK = (AppiumBy.XPATH, "//android.widget.TextView[@text='도어 잠금']")
    QS_SUNBLIND = (AppiumBy.XPATH, "//android.widget.TextView[@text='선블라인드']")
    QS_GLOVE_BOX = (AppiumBy.XPATH, "//android.widget.TextView[@text='글로브박스']")
    QS_STEERING_WHEEL = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전대']")
    QS_STEERING_WHEEL_SAVE = (AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
    QS_STEERING_WHEEL_RESTORE = (AppiumBy.XPATH, "//android.widget.TextView[@text='복원']")
    
    QS_SIDE_MIRROR = (AppiumBy.XPATH, "//android.widget.TextView[@text='사이드 미러']")    
    QS_AUTO_LABEL = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동']")

    # --- 라이트 (Lights) ------------------------------------------------------------------------
    LIGHTS_IconBtn = {
        "전조등 끄기":(0.583, 0.259),
        "전조등 자동":(0.666, 0.259),
        "전조등 미등":(0.750, 0.259),
        "전조등 켜짐":(0.833, 0.259),
        "자동 상향 전조등":(0.619, 0.338),
        "에스코트 조명":(0.554, 0.425), 
    }

    # 전조등
    LIGHT_HEADLIGHT = (AppiumBy.XPATH, "//android.widget.TextView[@text='전조등']")
    LIGHT_HEADLIGHT_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='전조등']/parent::*/parent::*//android.widget.TextView[@text='끄기']")
    LIGHT_HEADLIGHT_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='전조등']/parent::*/parent::*//android.widget.TextView[@text='자동']")

    #에스코트 조명
    LIGHT_ESCOOT_LIGHT = (AppiumBy.XPATH, "//android.widget.TextView[@text='전조등']/parent::*/parent::*//android.widget.TextView[@text='에스코트 조명']")
    # 프렁크등
    LIGHT_FRUNK_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='끄기'][1]")
    LIGHT_FRUNK_ON = (AppiumBy.XPATH, "//android.widget.TextView[@text='켜기'][1]")
    LIGHT_FRUNK_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동'][1]")
    # 트렁크등
    LIGHT_TRUNK_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='트렁크등']/parent::*/parent::*//android.widget.TextView[@text='끄기'][2]")
    LIGHT_TRUNK_ON = (AppiumBy.XPATH, "//android.widget.TextView[@text='트렁크등']/parent::*/parent::*//android.widget.TextView[@text='켜기'][2]")
    LIGHT_TRUNK_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='트렁크등']/parent::*/parent::*//android.widget.TextView[@text='자동'][2]")
    # 실내등 (Header)
    LIGHT_INTERIOR_ALL_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='끄기']")
    LIGHT_INTERIOR_ALL_SEATS = (AppiumBy.XPATH, "//android.widget.TextView[@text='모든 좌석']")
    LIGHT_INTERIOR_DRIVER = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전석']")
    LIGHT_INTERIOR_PASSENGER = (AppiumBy.XPATH, "//android.widget.TextView[@text='동승석']")
    LIGHT_INTERIOR_REAR_LEFT = (AppiumBy.XPATH, "//android.widget.TextView[@text='뒷좌석 좌측']")
    LIGHT_INTERIOR_REAR_RIGHT = (AppiumBy.XPATH, "//android.widget.TextView[@text='뒷좌석 우측']")
    # 무드 조명
    LIGHT_MOOD_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='무드 조명']/following-sibling::*//android.widget.TextView[@text='끄기']")
    LIGHT_MOOD_ON = (AppiumBy.XPATH, "//android.widget.TextView[@text='무드 조명']/following-sibling::*//android.widget.TextView[@text='켜기']")
    LIGHT_MOOD_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='무드 조명']/following-sibling::*//android.widget.TextView[@text='자동']")
    LIGHT_MOOD_COLOR = (AppiumBy.XPATH, "//android.widget.TextView[@text='무드 조명']/following-sibling::*//android.widget.TextView[@text='색상']")
    LIGHT_MOOD_BRIGHTNESS = (AppiumBy.CLASS_NAME, "android.widget.SeekBar")
    LIGHT_MOOD_SAVE_BTN = (AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")

    # --- AD (주행보조) ------------------------------------------------------------------------
    AD_IconBtn = {
        "AD_SPEED_MINUS":(0.573, 0.555),
        "AD_SPEED_PLUS":(0.781, 0.555),
    }
    
    AD_MODE_PRO = (AppiumBy.XPATH, "//android.widget.TextView[@text='프로']")
    AD_MODE_MAX = (AppiumBy.XPATH, "//android.widget.TextView[@text='맥스']")
    AD_SPEED_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동 (제한 속도)']")
    AD_SPEED_CURRENT = (AppiumBy.XPATH, "//android.widget.TextView[@text='현재 속도']")
    AD_SPEED_TARGET = (AppiumBy.XPATH, "//android.widget.TextView[@text='10km/h']")
    AD_LANE_CHANGE_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동']")
    AD_LANE_CHANGE_CONFIRM = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전자 확인']")

    # --- 주행 (Driving) ------------------------------------------------------------------------
    Driving_IconBtn = {
        "DRIVING_SNOW_RAIN_ASSIST":(0.541, 0.375),
        "DRIVING_ESC":(0.541, 0.587),
        "DRIVING_AUTO_HOLD":(0.549, 0.495),
        "DRIVING_BLIND_SPOT_CAMERA":(0.572, 0.555),
        "DRIVING_PARKING_BRAKE":(0.572, 0.555),
    }

    DRIVING_ACCEL_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='가속 모드']")
    DRIVING_ACCEL_MODE_GENTLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='부드럽게']")
    DRIVING_ACCEL_MODE_STANDARD = (AppiumBy.XPATH, "//android.widget.TextView[@text='표준']")
    DRIVING_ACCEL_MODE_FAST = (AppiumBy.XPATH, "//android.widget.TextView[@text='빠르게']")
    DRIVING_SNOW_RAIN_ASSIST = (AppiumBy.XPATH, "//android.widget.TextView[@text='눈/빗길 보조']")
    DRIVING_STEERING_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='조향 반응']")
    DRIVING_STEERING_MODE_STANDARD = (AppiumBy.XPATH, "//android.widget.TextView[@text='표준']")
    DRIVING_STEERING_MODE_LIGHT = (AppiumBy.XPATH, "//android.widget.TextView[@text='가볍게']")
    DRIVING_ESC = (AppiumBy.XPATH, "//android.widget.TextView[@text='ESC 활성화']")
    DRIVING_ESC_POPUP_OFF_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='끄기']")
    DRIVING_ESC_POPUP_ON_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='켜두기']")
    DRIVING_AUTOHOLD_BTN = (AppiumBy.XPATH, "//android.widget.TextView[@text='오토 홀드']")
    DRIVING_EPB_BTN = (AppiumBy.XPATH, "//android.widget.TextView[@text='파킹 브레이크']")
    DRIVING_BRAKE_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='브레이크 모드']")
    DRIVING_ACCEL_PEDAL_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='가속 페달 모드']")
    DRIVING_CREEP = (AppiumBy.XPATH, "//android.widget.TextView[@text='크립 모드']")
    DRIVING_ONE_PADAL_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='원페달 모드']")
    DRIVING_AUTO_HOLD = (AppiumBy.XPATH, "//android.widget.TextView[@text='정차 후 브레이크 자동 유지(Auto Hold)']")
    DRIVING_AUTO_HOLD_CONFIRM_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='확인']")
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
    DRIVING_BLIND_SPOT_CAMERA = (AppiumBy.XPATH, "//android.widget.TextView[@text='사각지대 카메라']")
    DRIVING_EPB_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='전자식 파킹 브레이크 수동 조작']")
    DRIVING_EPB_BTN = (AppiumBy.XPATH, "//android.widget.TextView[@text='파킹 브레이크']")

    # --- 잠금 (Lock) ---------------------------------------------------------------------------
    LOCK_UNLOCK_ALL = (AppiumBy.XPATH, "//android.widget.TextView[@text='모두']")
    LOCK_DRIVER_ONLY = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전석만']")

    # --- 시트 (Seat) ---------------------------------------------------------------------------
    SEAT_IconBtn = {
        "COMFORTABLE_RIDE":(0.554, 0.222),
    }

    SEAT_TOUCH_POINTS = {
        "운전석": (0.677, 0.685),
        "이동식 콘솔": (0.677, 0.592),
        "동승석": (0.677, 0.555),
        "뒷좌석 좌측": (0.799, 0.685),
        "뒷좌석 우측": (0.799, 0.555),
    }

    SEAT_MEMORY_1 = (AppiumBy.XPATH, "//android.widget.TextView[@text='1']")
    SEAT_MEMORY_2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='2']")
    SEAT_POSITION_SAVE = (AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
    SEAT_POSITION_RESTORE = (AppiumBy.XPATH, "//android.widget.TextView[@text='복원']")
    SEAT_POSITION_CLOSE = (AppiumBy.XPATH, "//android.widget.TextView[@text='접기']")
    SEAT_POSITION_OPEN = (AppiumBy.XPATH, "//android.widget.TextView[@text='펼치기']")
    SEAT_SIDE_MIRROR_ANGLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='사이드미러 각도']")
    SEAT_HANDLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전대']")
    SEAT_HANDLE_SAVE = (AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
    SEAT_HANDLE_RESTORE = (AppiumBy.XPATH, "//android.widget.TextView[@text='복원']")
    
    # --- 공조 (Climate) -----------------------------------------------------------------------
    CLIMATE_AUTO_RECIRC = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동 내기 전환']")
    CLIMATE_WASHER = (AppiumBy.XPATH, "//android.widget.TextView[@text='워셔액 분사']")
    CLIMATE_TUNNEL = (AppiumBy.XPATH, "//android.widget.TextView[@text='터널 진입']")
    CLIMATE_AIR_QUALITY = (AppiumBy.XPATH, "//android.widget.TextView[@text='공기 질 저하']")
    CLIMATE_OVERHEAT = (AppiumBy.XPATH, "//android.widget.TextView[@text='실내 과열 방지']")
    CLIMATE_AUTO_DRY = (AppiumBy.XPATH, "//android.widget.TextView[@text='에어컨 자동 건조']")

    # --- 충전 (Charging) -----------------------------------------------------------------------
    CHARGING_IconBtn = {
        "CHARGING_100%":(0.968, 0.324),
        "CHARGING_80%":(0.885, 0.324),
        "CHARGING_60%":(0.794, 0.324),
        "CHARGING_40%":(0.703, 0.324),
        "CHARGING_20%":(0.612, 0.324),
        "MINUS":(0.555, 0.602),
        "PLUS":(0.682, 0.602),
    }

    CHARGING_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전']")
    CHARGING_START = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전 시작']")
    CHARGING_UNLOCK_CONNECTOR = (AppiumBy.XPATH, "//android.widget.TextView[@text='커넥터 잠금 해제']")
    CHARGING_REMAINING = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전 잔량 표시']")
    CHARGING_KM = (AppiumBy.XPATH, "//android.widget.TextView[@text='km']")
    CHARGING_PERCENT = (AppiumBy.XPATH, "//android.widget.TextView[@text='%']")
    CHARGING_SLOW_CHARGING = (AppiumBy.XPATH, "//android.widget.TextView[@text='완속 충전']")
    CHARGING_CHARGING_CURRENT = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전 전류']")
    CHARGING_CHARGING_MINUS = (AppiumBy.XPATH, "//android.widget.TextView[@text='-']")
    CHARGING_CHARGING_MINUS2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='-']")
    CHARGING_CHARGING_PLUS = (AppiumBy.XPATH, "//android.widget.TextView[@text='+']")
    CHARGING_CONNECTOR = (AppiumBy.XPATH, "//android.widget.TextView[@text='커넥터 잠금 설정']")
    CHARGING_ALWAYS_LOCK = (AppiumBy.XPATH, "//android.widget.TextView[@text='상시 잠금']")
    CHARGING_LOCKING_CHARGING = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전 중 잠금']")
    CHARGING_DISABLED = (AppiumBy.XPATH, "//android.widget.TextView[@text='사용 안함']")
    CHARGING_ALWAYS_LOCK_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='완속 충전 시 커넥터가 항상 잠기며, 도어 잠금 해제 또는 커넥터 잠금 해제를 눌러야 잠금 해제됩니다.']")
    CHARGING_LOCKING_CHARGING_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전이 시작되면 커넥터가 잠기고, 충전이 끝나면 자동으로 해제됩니다.']")
    CHARGING_DISABLED_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전 중에도 커넥터가 잠기지 않으며 급속 충전에는 적용되지 않습니다.']")
    CHARGING_100 = (AppiumBy.XPATH, "//android.widget.TextView[@text='100%']")
    CHARGING_80 = (AppiumBy.XPATH, "//android.widget.TextView[@text='80%']")
    CHARGING_60 = (AppiumBy.XPATH, "//android.widget.TextView[@text='60%']")
    CHARGING_40 = (AppiumBy.XPATH, "//android.widget.TextView[@text='40%']")
    CHARGING_20 = (AppiumBy.XPATH, "//android.widget.TextView[@text='20%']")
    CHARGING_100_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='배터리 보호를 위해 80%까지 충전을 권장합니다.']")
    CHARGING_TOAST_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='현재 충전량이 목표 충전량보다 높습니다.']")

    # --- 네비게이션 (Navigation) -----------------------------------------------------------------------
    Nav_IconBtn = {
        "EV_SWICH":(0.547, 0.212),
        "Initialize":(0.938, 0.787),
        "Initialize2":(0.573, 0.648),
    }

    NAV_CHARGING_STATION = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전소']")
    NAV_EV_ROUTE = (AppiumBy.XPATH, "//android.widget.TextView[@text='EV 경로 계획']")
    NAV_EV_ROUTE_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='목적지까지 이동하기에 배터리가 부족할 것으로 예상되면 경로에 선호 충전소가 추가됩니다.']")
    NAV_PREF_STATION = (AppiumBy.XPATH, "//android.widget.TextView[@text='선호 충전소']")
    NAV_PREF_STATION_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='충전소 검색 및 경로 안내 시, 선택한 사업자의 충전소를 우선 표시합니다.']")
    NAV_VERSION = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '버전 정보')]")
    NAV_VERSION_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '2.3.0')]") # dynamic version check?
    NAV_DATA = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '데이터 관리')]")
    NAV_INITIALIZE = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '사용 이력 초기화')]")
    NAV_INITIALIZE_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '최근 목적지, 즐겨찾기, 주행 기록 등 내비게이션 사용 이력을 모두 삭제합니다.')]")
    NAV_INITIALIZE_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '초기화')]")
    NAV_POPUP_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '현재 프로필에 연결된 모든 모바일 및 차량 서비스에서 아래의 사용 이력이 삭제됩니다.')]")
    NAV_POPUP_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '취소')]")
    NAV_POPUP_LIST = (AppiumBy.XPATH, "//android.widget.TextView[contains(@text, '최근 목적지 \n• 즐겨찾기 \n• 검색 기록 \n• 주행 기록')]")

    # Gleo AI Screen ---------------------------------------------------------------------------
    GLEO_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='Gleo AI']")
    GLEO_VOICE = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 유형']")
    GLEO_VOICE_1 = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 1']")
    GLEO_VOICE_2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 2']")
    GLEO_VOICE_3 = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 3']")
    GLEO_VOICE_4 = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 4']")
    GLEO_VOICE_5 = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 5']")
    GLEO_VOICE_6 = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 6']")
    GLEO_WAY = (AppiumBy.XPATH, "//android.widget.TextView[@text='대화 방법']")
    GLEO_CALLING = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"'글레오'라고 불러 대화 시작\"]")
    GLEO_CALLING_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"음성인식 버튼을 누를 필요 없이 '글레오'라고 불러 대화를 시작할 수 있습니다.\"]")
    GLEO_START = (AppiumBy.XPATH, "//android.widget.TextView[@text='바로 대화 시작']")
    GLEO_START_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='글레오라고 부를 필요 없이, 질문이나 명령을 하여 자연스럽게 대화를 시작할 수 있습니다.']")
    GLEO_CONTINUOUS = (AppiumBy.XPATH, "//android.widget.TextView[@text='연속 대화']")
    GLEO_CONTINUOUS_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='응답 후에도 글레오가 켜진 상태로 유지되어 대화를 이어갈 수 있습니다.']")
    GLEO_STYLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='대화 스타일']")
    GLEO_POLITE = (AppiumBy.XPATH, "//android.widget.TextView[@text='정중한']")
    GLEO_FRIENDLY = (AppiumBy.XPATH, "//android.widget.TextView[@text='친근한']")
    GLEO_SEAT = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 인식 좌석']")
    GLEO_DRIVER = (AppiumBy.XPATH, "//android.widget.TextView[@text='운전석']")
    GLEO_DRIVER_RECOGNITION = (AppiumBy.XPATH, "//android.widget.TextView[@text='항상 인식됨']")
    GLEO_PASSENGER = (AppiumBy.XPATH, "//android.widget.TextView[@text='동승석']")
    GLEO_REAR_LEFT = (AppiumBy.XPATH, "//android.widget.TextView[@text='뒷좌석 좌측']")
    GLEO_REAR_RIGHT = (AppiumBy.XPATH, "//android.widget.TextView[@text='뒷좌석 우측']")
    GLEO_CALLING_POPUP_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text=\"'글레오'라고 부르면 글레오 AI가 응답합니다. 기능을 활성화하면 호출어 인식을 위해 음성 정보가 수집될 수 있습니다.\"]")
    GLEO_CALLING_POPUP_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='활성화']")
    GLEO_CALLING_POPUP_BUTTON2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='취소']")

    # Display (화면) ---------------------------------------------------------------------------
    DIS_IconBtn = {
        "DIS_DOWN":(0.557, 0.463),
        "DIS_UP":(0.807, 0.463),
        "DIS_CLEENING_MODE_END":(0.173, 0.589),
    }

    DIS_THEME = (AppiumBy.XPATH, "//android.widget.TextView[@text='테마']")
    DIS_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동']")
    DIS_AUTO_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='테마를 주변 밝기에 맞춰 자동으로 변경합니다.']")
    DIS_LIGHT = (AppiumBy.XPATH, "//android.widget.TextView[@text='라이트']")
    DIS_DARK = (AppiumBy.XPATH, "//android.widget.TextView[@text='다크']")
    DIS_BRIGHTNESS = (AppiumBy.XPATH, "//android.widget.TextView[@text='밝기']")
    DIS_ADJUSTMENT = (AppiumBy.XPATH, "//android.widget.TextView[@text='밝기 조정']")
    DIS_DOWN = (AppiumBy.XPATH, "//android.widget.TextView[@text='<']")
    DIS_UP = (AppiumBy.XPATH, "//android.widget.TextView[@text='>']")
    DIS_BRIGHTNESS_AUTO_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='화면 밝기를 주변 밝기에 맞춰 자동으로 변경합니다.']")
    DIS_MNAGEMENT = (AppiumBy.XPATH, "//android.widget.TextView[@text='화면 관리']")
    DIS_CLEENING_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='화면 클리닝 모드']")
    DIS_CLEENING_MODE_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='화면 클리닝 모드가 실행 중입니다.']")
    DIS_CLEENING_MODE_TEXT2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='화면을 닦는 동안 오입력을 방지하기 위해 터치 기능이 꺼집니다. 모드를 종료하려면 아래 버튼을 3초 이상 눌러주세요.']")
    DIS_CLEENING_MODE_END = (AppiumBy.XPATH, "//android.widget.TextView[@text='길게 눌러 종료']")

    # Sound (사운드) ---------------------------------------------------------------------------
    SND_IconBtn = {
        "SND_HAM":(0.75, 0.352),
    }

    SND_VOLUME = (AppiumBy.XPATH, "//android.widget.TextView[@text='음량']")
    SND_QUIET = (AppiumBy.XPATH, "//android.widget.TextView[@text='조용한 모드']")
    SND_QUIET_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='차량 내 사운드를 최소화해 조용하고 편안한 주행 환경을 제공합니다.']")
    SND_SYSTEM = (AppiumBy.XPATH, "//android.widget.TextView[@text='시스템']")
    SND_MEDIA = (AppiumBy.XPATH, "//android.widget.TextView[@text='미디어']")
    SND_NAVIGATION = (AppiumBy.XPATH, "//android.widget.TextView[@text='내비게이션']")
    SND_RINGTONE = (AppiumBy.XPATH, "//android.widget.TextView[@text='벨소리']")
    SND_CALL = (AppiumBy.XPATH, "//android.widget.TextView[@text='통화']")
    SND_GUIDE = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성 안내']")
    SND_AUTOMATIC = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동 음량 조절']")
    SND_AUTOMATIC_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='주행 속도와 주변 소음에 따라 미디어, 라디오, 내비게이션 음량을 자동으로 조절해 편안한 청취 환경을 유지합니다.']")
    SND_OFF = (AppiumBy.XPATH, "//android.widget.TextView[@text='끄기']")
    SND_WEAKLY = (AppiumBy.XPATH, "//android.widget.TextView[@text='약하게']")
    SND_MIDDLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='중간']")
    SND_STRONG = (AppiumBy.XPATH, "//android.widget.TextView[@text='강하게']")
    SND_AUDIO = (AppiumBy.XPATH, "//android.widget.TextView[@text='오디오']")
    SND_FOCUS = (AppiumBy.XPATH, "//android.widget.TextView[@text='사운드 포커스']")
    SND_FRONT = (AppiumBy.XPATH, "//android.widget.TextView[@text='전방']")
    SND_CENTER = (AppiumBy.XPATH, "//android.widget.TextView[@text='중앙']")
    SND_REAR = (AppiumBy.XPATH, "//android.widget.TextView[@text='후방']")
    SND_SETTINGS = (AppiumBy.XPATH, "//android.widget.TextView[@text='사용자 설정']")
    SND_INITIAL = (AppiumBy.XPATH, "//android.widget.TextView[@text='초기화']")
    SND_3D = (AppiumBy.XPATH, "//android.widget.TextView[@text='3D 서라운드']")
    SND_NORMAL = (AppiumBy.XPATH, "//android.widget.TextView[@text='보통']")
    SND_MAXIMUM = (AppiumBy.XPATH, "//android.widget.TextView[@text='최대']")
    SND_EQUALIZER = (AppiumBy.XPATH, "//android.widget.TextView[@text='이퀄라이저']")
    SND_ORIGINAL = (AppiumBy.XPATH, "//android.widget.TextView[@text='원음']")
    SND_LOW = (AppiumBy.XPATH, "//android.widget.TextView[@text='저음 강조']")
    SND_GENTLY = (AppiumBy.XPATH, "//android.widget.TextView[@text='부드럽게']")
    SND_DYNAMIC = (AppiumBy.XPATH, "//android.widget.TextView[@text='다이내믹']")
    SND_VOICE = (AppiumBy.XPATH, "//android.widget.TextView[@text='음성']")
    SND_50HZ = (AppiumBy.XPATH, "//android.widget.TextView[@text='50 Hz']")
    SND_125HZ = (AppiumBy.XPATH, "//android.widget.TextView[@text='125 Hz']")
    SND_315HZ = (AppiumBy.XPATH, "//android.widget.TextView[@text='315 Hz']")
    SND_800HZ = (AppiumBy.XPATH, "//android.widget.TextView[@text='800 Hz']")
    SND_2KHZ = (AppiumBy.XPATH, "//android.widget.TextView[@text='2 kHz']")
    SND_5KHZ = (AppiumBy.XPATH, "//android.widget.TextView[@text='5 kHz']")
    SND_8KHZ = (AppiumBy.XPATH, "//android.widget.TextView[@text='8 kHz']")
    SND_LOW_E = (AppiumBy.XPATH, "//android.widget.TextView[@text='Low']")
    SND_MID = (AppiumBy.XPATH, "//android.widget.TextView[@text='Mid']")
    SND_HIGH = (AppiumBy.XPATH, "//android.widget.TextView[@text='Hi']")
    SND_CONNECTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='연결 기기 음량']")
    SND_ANDROID = (AppiumBy.XPATH, "//android.widget.TextView[@text='Android Auto']")
    SND_APPLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='Apple CarPlay']")
    
    # Profile (프로필) ---------------------------------------------------------------------------
    PROFILE_IconBtn = {
        "PROFILE_A":(0.286, 0.704),
        "PROFILE_S":(0.344, 0.704),
        "PROFILE_D":(0.402, 0.704),
        "PROFILE_F":(0.460, 0.704),
        "PROFILE_X":(0.385, 0.769),
        "PROFILE_P":(0.737, 0.625),
        "PROFILE_T":(0.474, 0.625),
        "PROFILE_M":(0.656, 0.769),
        "PROFILE_CRN":(0.563, 0.444),
    }

    PROFILE_SETTINGS = (AppiumBy.XPATH, "//android.widget.TextView[@text='프로필 설정']")
    PROFILE_ADD = (AppiumBy.XPATH, "//android.widget.TextView[@text='프로필 추가']")
    PROFILE_KEY = (AppiumBy.XPATH, "//android.widget.TextView[@text='키 관리']")
    PROFILE_CARDKEY = (AppiumBy.XPATH, "//android.widget.TextView[@text='NFC 카드키']")
    PROFILE_ENTER_NAME = (AppiumBy.XPATH, "//android.widget.TextView[@text='이름 입력']")
    PROFILE_SAVE = (AppiumBy.XPATH, "//android.widget.TextView[@text='저장']")
    PROFILE_CRN = (AppiumBy.XPATH, "//android.widget.TextView[@text='CRN이 등록되지 않은 타겟 보드입니다. \n보안 정책에 따라 CRN이 등록되지 않은 타겟 보드는 사용할 수 없습니다. \nCRN 등록 방법은 Pleos Playground 웹사이트를 참고하세요.']")

    # --- 편의 기능(Convenience) ---------------------------------------------------------------------------
    CONVENIENCE_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='편의 기능']")
    CONVENIENCE_CAR_WASH_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='세차 모드']")
    CONVENIENCE_VALET_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='발레 모드']")
    CONVENIENCE_CAMPING_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='캠핑 모드']")
    CONVENIENCE_PET_CARE_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='펫 케어 모드']")
    CONVENIENCE_DOUBLE_PARKING_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='이중 주차 모드']")
    CONVENIENCE_TOWING_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='견인 모드']")
    CONVENIENCE_ON_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='켜기']")
    CONVENIENCE_STANDBY_MODE = (AppiumBy.XPATH, "//android.widget.TextView[@text='대기 모드']")

    CONVENIENCE_STANDBY_MODE_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='차량 전원, 조명, 화면을 모두 꺼 대기 상태로 전환합니다.']")
    CONVENIENCE_START_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='시작']")
    CONVENIENCE_CAR_WASH_MODE_POPUP = (AppiumBy.XPATH, "//android.widget.TextView[@text='안전한 세차를 위해 아래 기능이 자동으로 설정됩니다.']")
    CONVENIENCE_CAR_WASH_MODE_POPUP_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='창문, 도어, 트렁크, 충전 포트, 사이드 미러 닫힘']")
    CONVENIENCE_CAR_WASH_MODE_POPUP_TEXT2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='와이퍼, 주차 센서, 외부 녹화 기능 중지']")
    CONVENIENCE_CAR_WASH_MODE_POPUP_TEXT3 = (AppiumBy.XPATH, "//android.widget.TextView[@text='내기 순환으로 변경']")
    CONVENIENCE_CAR_WASH_MODE_POPUP_NEURAL = (AppiumBy.XPATH, "//android.widget.TextView[@text='중립 유지 모드']")
    CONVENIENCE_CAR_WASH_MODE_POPUP_NEURAL_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='기어를 N단으로 전환한 뒤 운전자가 하차하더라도 N단 상태를 유지합니다.']")
    CONVENIENCE_CANCLE_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='취소']")
    CONVENIENCE_CAMPING_MODE_POPUP = (AppiumBy.XPATH, "//android.widget.TextView[@text='실내 온도, 조명, 전원을 유지해 휴식이나 캠핑 시 쾌적한 환경을 제공합니다.']")
    CONVENIENCE_CAMPING_MODE_POPUP_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='주차 녹화와 디지털 키 자동 잠금 기능이 꺼집니다.']")
    CONVENIENCE_CAMPING_MODE_POPUP_TEXT2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='배터리 잔량이 20% 이하로 떨어지면 모드가 자동으로 종료됩니다.']")
    CONVENIENCE_PET_CARE_MODE_POPUP = (AppiumBy.XPATH, "//android.widget.TextView[@text='반려동물이 쾌적하게 머물 수 있도록 차량이 잠긴 상태에서도 실내 온도를 적절하게 유지합니다.']")
    CONVENIENCE_PET_CARE_MODE_POPUP_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='이 모드가 켜진 동안에는 주행할 수 없습니다.']")
    CONVENIENCE_PET_CARE_MODE_POPUP_TEXT2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='배터리 잔량이 20% 이하로 떨어지면 모드가 자동으로 종료됩니다.']")
    CONVENIENCE_DOUBLE_PARKING_MODE_POPUP = (AppiumBy.XPATH, "//android.widget.TextView[@text='차량을 중립 상태로 유지해, 다른 사람이 안전하게 차를 이동시킬 수 있습니다.']")
    CONVENIENCE_DOUBLE_PARKING_MODE_POPUP_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='경사가 있는 곳에서는 차량이 움직일 수 있으니 주의하세요.']")
    CONVENIENCE_DOUBLE_PARKING_MODE_POPUP_TEXT2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='속도가 5km/h를 초과하거나, 차량이 10m 이상 이동 또는 배터리 잔량이 20% 이하로 떨어지면 모드가 자동으로 해제됩니다.']")
    CONVENIENCE_DOUBLE_PARKING_MODE_POPUP_TEXT3 = (AppiumBy.XPATH, "//android.widget.TextView[@text='모드를 켜려면 브레이크를 밟은 상태에서 버튼을 누르세요.']")
    CONVENIENCE_TOWING_MODE_POPUP = (AppiumBy.XPATH, "//android.widget.TextView[@text='안전한 견인을 위해 차량을 준비합니다. 모든 바퀴가 들어올려진 상태에서만 사용하세요.']")
    CONVENIENCE_TOWING_MODE_POPUP_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='경사가 있는 곳에서는 차량이 움직일 수 있으니 주의하세요.']")
    CONVENIENCE_TOWING_MODE_POPUP_TEXT2 = (AppiumBy.XPATH, "//android.widget.TextView[@text='속도가 5km/h를 초과하거나, 차량이 10m 이상 이동 또는 배터리 잔량이 5% 이하로 떨어지면 모드가 자동으로 해제됩니다.']")
    CONVENIENCE_TOWING_MODE_POPUP_TEXT3 = (AppiumBy.XPATH, "//android.widget.TextView[@text='모드를 켜려면 브레이크를 밟은 상태에서 3초 동안 시작 버튼을 누르세요.']")
    CONVENIENCE_STANDBY_MODE_POPUP = (AppiumBy.XPATH, "//android.widget.TextView[@text='화면이 꺼진 후에도 설정된 온도를 일정 시간 유지합니다.']")
    CONVENIENCE_STANDBY_MODE_POPUP_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='화면을 터치하거나 브레이크 페달을 밟으면 대기 모드가 해제됩니다.']")

    # --- 연결(Connection) ---------------------------------------------------------------------------
    CONNECTION_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='연결']")
    CONNECTION_BLUETOOTH = (AppiumBy.XPATH, "//android.widget.TextView[@text='블루투스']")
    CONNECTION_WIFI = (AppiumBy.XPATH, "//android.widget.TextView[@text='Wi-Fi']")
    CONNECTION_WIFI_HOTSPOT = (AppiumBy.XPATH, "//android.widget.TextView[@text='Wi-Fi 핫스팟']")
    CONNECTION_MOBILE_DATA = (AppiumBy.XPATH, "//android.widget.TextView[@text='모바일 데이터']")

    # --- 앱(Apps) ---------------------------------------------------------------------------
    APPS_VIVALDI = (AppiumBy.XPATH, "//android.widget.TextView[@text='Vivaldi Browser']")
    APPS_WIDGET_HOME = (AppiumBy.XPATH, "//android.widget.TextView[@text='WidgetHomeScreen']")
    APPS_SMART_KEY = (AppiumBy.XPATH, "//android.widget.TextView[@text='스마트키 콘솔']")
    APPS_PHONE = (AppiumBy.XPATH, "//android.widget.TextView[@text='전화']")
    APPS_VEHICLE_SETTINGS = (AppiumBy.XPATH, "//android.widget.TextView[@text='차량 설정']")
    APPS_CAMERA = (AppiumBy.XPATH, "//android.widget.TextView[@text='카메라']")
    APPS_CLOUD_CAM = (AppiumBy.XPATH, "//android.widget.TextView[@text='클라우드캠']")
    APPS_APPIUM_SETTINGS = (AppiumBy.XPATH, "//android.widget.TextView[@text='Appium Settings']")
    APPS_DEFAULT_APPS = (AppiumBy.XPATH, "//android.widget.TextView[@text='기본 앱']")
    APPS_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='앱']")

    APPS_ANDROID_AUTO = (AppiumBy.XPATH, "//android.widget.TextView[@text='Android Auto']")
    APPS_CARPLAY = (AppiumBy.XPATH, "//android.widget.TextView[@text='CarPlay']")
    APPS_GLEO_AI_APP = (AppiumBy.XPATH, "//android.widget.TextView[@text='Gleo AI']")
    APPS_GLEO_AI_DETAIL_BTN = (AppiumBy.XPATH, "//android.widget.TextView[@text='Gleo AI']/following-sibling::android.view.View//android.widget.Button")

    # --- 보안(Security) -----------------------------------------------------------------------
    SECURITY_RECORDING_OPTIONS = (AppiumBy.XPATH, "//android.widget.TextView[@text='녹화 옵션']")
    SECURITY_DRIVING_RECORDING = (AppiumBy.XPATH, "//android.widget.TextView[@text='주행 중']")
    SECURITY_PARKING_RECORDING = (AppiumBy.XPATH, "//android.widget.TextView[@text='주차 중']")
    SECURITY_EVENT_RECORDING = (AppiumBy.XPATH, "//android.widget.TextView[@text='이벤트 녹화']")
    SECURITY_CONST_RECORDING = (AppiumBy.XPATH, "//android.widget.TextView[@text='상시 녹화']")

    # --- 개인정보 보호(Privacy) -------------------------------------------------------------------
    PRIVACY_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='개인정보 보호']")
    PRIVACY_PERMISSION_CONTROL = (AppiumBy.XPATH, "//android.widget.TextView[@text='권한 제어']")
    PRIVACY_MIC_USAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='마이크 사용']")
    PRIVACY_LOCATION_USAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='위치 정보 사용']")
    PRIVACY_CAMERA_USAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='실내 카메라 사용']")
    PRIVACY_BLOCK_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='차단']")
    PRIVACY_CANCEL_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='취소']")


    # --- 하이패스 (HyundaiPass) -------------------------------------------------------------------
    HIPASS_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='하이패스']")
    HIPASS_PAYMENT_INFO = (AppiumBy.XPATH, "//android.widget.TextView[@text='결제 정보']")
    HIPASS_BALANCE = (AppiumBy.XPATH, "//android.widget.TextView[@text='잔액']")
    HIPASS_RECENT_HISTORY = (AppiumBy.XPATH, "//android.widget.TextView[@text='최근 결제 내역']")
    HIPASS_PAYMENT_DISPLAY = (AppiumBy.XPATH, "//android.widget.TextView[@text='결제 표시']")

    # --- 일반 설정 (General) -------------------------------------------------------------------
    GENERAL_SAVE = (AppiumBy.XPATH, "//android.widget.TextView[@text='저장' or @text='Save']")
    GENERAL_CONFIRM = (AppiumBy.XPATH, "//android.widget.TextView[@text='확인' or @text='Confirm']")
    GENERAL_CANCEL = (AppiumBy.XPATH, "//android.widget.TextView[@text='취소' or @text='Cancel']")

    GENERAL_FONT_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='글꼴']")
    GENERAL_FONT_DROPDOWN = (AppiumBy.XPATH, "//android.widget.TextView[@text='기본' or @text='현대' or @text='기아' or @text='제네시스']")
    GENERAL_FONT_SETTING_BASIC = (AppiumBy.XPATH, "//android.widget.TextView[@text='기본']")
    GENERAL_FONT_SETTING_HYUNDAI = (AppiumBy.XPATH, "//android.widget.TextView[@text='현대']")
    GENERAL_FONT_SETTING_KIA = (AppiumBy.XPATH, "//android.widget.TextView[@text='기아']")
    GENERAL_FONT_SETTING_GENESIS = (AppiumBy.XPATH, "//android.widget.TextView[@text='제네시스']")
    GENERAL_FONT_SETTING_APPLY = (AppiumBy.XPATH, "//android.widget.TextView[@text='적용']")
    
    GENERAL_LANGUAGE_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='언어']")
    GENERAL_LANGUAGE_DROPDOWN = (AppiumBy.XPATH, "//android.widget.TextView[@text='한국어' or @text='English']")
    GENERAL_LANGUAGE_SETTING_KO = (AppiumBy.XPATH, "//android.widget.TextView[@text='한국어']")
    GENERAL_LANGUAGE_SETTING_EN = (AppiumBy.XPATH, "//android.widget.TextView[@text='English']")
    GENERAL_LANGUAGE_SETTING_ZH = (AppiumBy.XPATH, "//android.widget.TextView[@text='中文']")
    GENERAL_LANGUAGE_SETTING_JP = (AppiumBy.XPATH, "//android.widget.TextView[@text='日本語']")
    GENERAL_LANGUAGE_SETTING_DE = (AppiumBy.XPATH, "//android.widget.TextView[@text='Deutsch']")
    GENERAL_LANGUAGE_SETTING_FR = (AppiumBy.XPATH, "//android.widget.TextView[@text='Français']")
    GENERAL_LANGUAGE_SETTING_ES = (AppiumBy.XPATH, "//android.widget.TextView[@text='Español']")
    
    GENERAL_AUTO_TIME_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='자동 시간 설정']")
    GENERAL_DATE_TIME_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='날짜 및 시간 설정']")
    GENERAL_MANUAL_TIME_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='설정']")

    GENERAL_TIME_FORMAT_TEXT = (AppiumBy.XPATH, "//android.widget.TextView[@text='시간 형식']")
    GENERAL_MANUAL_TIME_TYPE_12 = (AppiumBy.XPATH, "//android.widget.TextView[@text='12시간' or @text='12 hours']")
    GENERAL_MANUAL_TIME_TYPE_24 = (AppiumBy.XPATH, "//android.widget.TextView[@text='24시간' or @text='24 hours']")
    
    GENERAL_POPUP_TITLE_DATE_TIME = (AppiumBy.XPATH, "//android.widget.TextView[@text='날짜 및 시간 설정']")
    GENERAL_POPUP_CONFIRM = (AppiumBy.XPATH, "//android.widget.TextView[@text='확인']")
    GENERAL_POPUP_CANCEL = (AppiumBy.XPATH, "//android.widget.TextView[@text='취소']")
    GENERAL_DATE_TIME = (AppiumBy.XPATH, "//android.widget.TextView[@text='날짜 및 시간']")
    
    GENERAL_UNIT_SETTING = (AppiumBy.XPATH, "//android.widget.TextView[@text='단위']")
    GENERAL_SUB_SPEED_DISPLAY = (AppiumBy.XPATH, "//android.widget.TextView[@text='보조 속도 표시']")
    GENERAL_DISTANCE = (AppiumBy.XPATH, "//android.widget.TextView[@text='거리']")
    GENERAL_DISTANCE_KM = (AppiumBy.XPATH, "//android.widget.TextView[@text='km']")
    GENERAL_DISTANCE_MILE = (AppiumBy.XPATH, "//android.widget.TextView[@text='mile']")
    GENERAL_TEMPERATURE = (AppiumBy.XPATH, "//android.widget.TextView[@text='온도']")
    GENERAL_TEMPERATURE_C = (AppiumBy.XPATH, "//android.widget.TextView[@text='℃']")
    GENERAL_TEMPERATURE_F = (AppiumBy.XPATH, "//android.widget.TextView[@text='℉']")
    GENERAL_CONSUMPTION = (AppiumBy.XPATH, "//android.widget.TextView[@text='연비']")
    GENERAL_CONSUMPTION_L_100KM = (AppiumBy.XPATH, "//android.widget.TextView[@text='km/kWh']")
    GENERAL_CONSUMPTION_MILEAGE = (AppiumBy.XPATH, "//android.widget.TextView[@text='kWh/100km']")
    GENERAL_TIRE_PRESSURE = (AppiumBy.XPATH, "//android.widget.TextView[@text='타이어 공기압']")
    GENERAL_TIRE_PRESSURE_PSI = (AppiumBy.XPATH, "//android.widget.TextView[@text='psi']")
    GENERAL_TIRE_PRESSURE_KPA = (AppiumBy.XPATH, "//android.widget.TextView[@text='kpa']")
    GENERAL_TIRE_PRESSURE_BAR = (AppiumBy.XPATH, "//android.widget.TextView[@text='bar']")

    # --- 차량 정보(Vehicle Info) ---
    VI_TITLE = (AppiumBy.XPATH, "//android.widget.TextView[@text='차량 정보']")
    VI_CONNECT = (AppiumBy.XPATH, "//android.widget.TextView[@text='Connect']")
    VI_SOFTWARE_INFO = (AppiumBy.XPATH, "//android.widget.TextView[@text='소프트웨어 정보']")
    VI_AUTO_UPDATE = (AppiumBy.XPATH, "//android.widget.TextView[@text='업데이트 자동 다운로드']")
    VI_VIN = (AppiumBy.XPATH, "//android.widget.TextView[@text='차대 번호']")
    VI_FACTORY_RESET = (AppiumBy.XPATH, "//android.widget.TextView[@text='공장 초기화']")
    VI_INITIALIZE_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='초기화']")

    VI_LEGAL_INFO = (AppiumBy.XPATH, "//android.widget.TextView[@text='법적 정보']")
    VI_LEGAL_INFO_BUTTON = (AppiumBy.XPATH, "//android.widget.TextView[@text='보기']")
    VI_INFO_DEVICE = (AppiumBy.XPATH, "//android.widget.TextView[@text='단말기 정보']")
    VI_INFO_SOFTWARE = (AppiumBy.XPATH, "//android.widget.TextView[@text='소프트웨어 정보']")
    VI_POPUP_OK = (AppiumBy.XPATH, "//android.widget.TextView[@text='확인']")