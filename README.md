# 안드로이드 오토 IVI 자동화 테스트 프로젝트

이 프로젝트는 Appium과 Python을 사용하여 안드로이드 오토 기반의 IVI(In-Vehicle Infotainment) 시스템을 테스트하기 위한 자동화 솔루션입니다.
Page Object Model (POM) 패턴을 사용하여 유지보수성을 높였습니다.

## 사전 요구 사항 (Prerequisites)

- Python 3.8 이상
- Appium Server (GUI 또는 CLI)
- 테스트 대상 리눅스/안드로이드 장비 연결

## 설치 방법 (Installation)

의존성 라이브러리를 설치합니다.

```bash
pip install -r requirements.txt
```

## 설정 (Configuration)

`config.py` 파일에서 장비 연결 정보와 테스트 대상 앱 패키지 정보를 수정할 수 있습니다.

- **기본 연결 모드**: TCP/IP
- **대상 IP**: 192.168.0.111:5555
- **USB 모델명**: bb60ed15853

## 테스트 실행 (Running Tests)

### 1. Appium 서버 실행
로컬에서 Appium Server를 포트 `4723`으로 실행합니다. (변경 시 `config.py` 수정 필요)

### 2. 테스트 수행
프로젝트 루트 디렉토리에서 다음 명령어를 실행합니다.

```bash
pytest tests/test_navigation.py -v
```

또는 `-s` 옵션을 추가하여 콘솔 출력을 확인할 수 있습니다.

```bash
pytest -v -s
```

## 프로젝트 구조

- `pages/`: 화면별 요소 및 동작을 정의한 페이지 클래스들 (POM)
- `tests/`: 실제 테스트 시나리오 스크립트
- `utils/`: 드라이버 팩토리 등 유틸리티
- `config.py`: 설정 파일
