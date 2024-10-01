# real-estate-scraper

scraper for real estate information

## 라이브러리 설치

```
pip install selenium chromedriver-autoinstaller pyautogui
```

<br>

## 실행

### 크롬 디버거모드 실행

윈도우키 + R 을 눌러 실행기를 열어주고 아래의 명령어를 실행해주세요.

크롬이 열리면 로그인까지 해주셔야 합니다.

```
C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 --user-data-dir="C:/ChromeTEMP"
```

<br>

### 페이지 접속

디버거모드에서 아래의 링크를 열어주고, `연립/다세대`와 `전월세`를 선택해주세요.

https://rt.molit.go.kr/pt/xls/xls.do?mobileAt=

<br>

### 마우스 좌표 수정

`device_manager.py` 의 `get_current_position()` 함수를 실행하여 다운로드 버튼의 좌표를 구하세요.

그리고 `move_to_button()` 함수를 수정해줍니다.

```
def move_to_button():
    pyautogui.moveTo({x좌표}, {y좌표}, 0.5)
```

<br>

### main 함수 실행

터미널 경로를 `src` 로 이동해주세요.

```
cd src
```

`main.py` 파일을 실행해주세요.

```
python main.py
```
