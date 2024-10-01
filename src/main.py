from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

pyautogui.FAILSAFE = False
from device_manager import *

chromedriver_autoinstaller.install()
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
driver = webdriver.Chrome(options=chrome_options)


def selectPeriod():
    element = driver.find_element(by=By.CSS_SELECTOR, value="#srhFromDt")
    element.send_keys("2024-09-01")
    element = driver.find_element(by=By.CSS_SELECTOR, value="#srhToDt")
    element.send_keys("2024-10-01")


def selectSeoul():
    element = driver.find_element(by=By.CSS_SELECTOR, value="#srhSidoCd")
    select = Select(element)
    select.select_by_index(1)  # 서울특별시


def selectGu(index: int):
    element = driver.find_element(by=By.CSS_SELECTOR, value="#srhSggCd")
    select = Select(element)
    select.select_by_index(index)


def getDongCount():
    element = driver.find_element(by=By.CSS_SELECTOR, value="#srhEmdCd")
    select = Select(element)
    item_count = len(select.options)
    return item_count


def selectDong(index: int):
    element = driver.find_element(by=By.CSS_SELECTOR, value="#srhEmdCd")
    select = Select(element)
    select.select_by_index(index)


def clickCsvDownload():
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    move_to_button()
    time.sleep(0.5)
    click_left_button()


def check_and_handle_alert(i, j):
    time.sleep(3)
    try:
        WebDriverWait(driver, 1).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        print(f"{i}-{j} ----- {alert_text}")
        if "다운로드에 실패하였습니다." in alert_text:
            alert.accept()
            return True

        elif "검색 조건에 해당하는 데이터가 존재하지 않습니다." in alert_text:
            alert.accept()
            return False
        alert.accept()
        return True
    except (TimeoutException, NoAlertPresentException):
        return False


start_gu_index = 1
start_dong_index = 1

selectPeriod()
selectSeoul()

for i in range(start_gu_index, 26):
    selectGu(i)
    dongs = getDongCount()
    for j in range(start_dong_index, dongs):
        selectDong(j)

        while True:
            clickCsvDownload()
            if not check_and_handle_alert(i, j):
                break

        print(f"{i}-{j} ----- done.")
