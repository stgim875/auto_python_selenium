from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# USB: usb_device_handle_win.cc:1048 Failed to read descriptor
# from node connection:시스템에 부착된 장치가 작동하지 않습니다.(0x1F)
# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--use-fake-ui-for-media-stream")

CHROME_DRIVER_PATH = (
    "C:\python_selenium_auto\chromedriver.exe")  # 크롬드라이버 경로경로
driver = webdriver.Chrome(
    executable_path=CHROME_DRIVER_PATH, chrome_options=options)

# 사용할 webdriver 지정: Chrome 사용
# driver = webdriver.Chrome(options=options)

# 진입할 경로 지정
driver.get("https://stgwww.virnect.com/")

# 웹페이지에서 특정 요소가 준비될 때까지 암묵적으로 대기한다.
# driver.implicitly_wait(5)
# 3초 대기
time.sleep(3)

# 웹페이지 해상도 조절
# driver.set_window_size(1690, 1060)
# windows을 최대 사이즈로 조절
driver.maximize_window()

# 3초 대기
time.sleep(3)

# Log in 페이지로 이동한다.
# driver.get(
#     'https://stgconsole.virnect.com/?continue=https%3A%2F%2Fstgwww.virnect.com%2F')

# Log in 버튼을 클릭하여 로그인센터로 이동한다.
logincenter = driver.find_element(By.XPATH, "//*[@class ='login-btn']").click()

# 3초 대기
time.sleep(3)

# 아이디 입력창 위치 찾기 및 아이디 입력
userid = driver.find_element(
    By.XPATH,
    "//div[@class ='email-input el-input el-input--suffix']/input[1]").send_keys('maxgim875@gmail.com')

# 3초 대기
time.sleep(3)

# 패스워드 입력창 위치 찾기 및 패스워드 입력
userpw = driver.find_element(
    By.XPATH,
    "//div[@class = 'password-input el-input el-input--suffix']/input[1]").send_keys('@rokmc875th')

# 3초 대기
time.sleep(3)

# 로그인 클릭
loginclick = driver.find_element(
    By.XPATH, "//*[@class = 'el-button next-btn block-btn el-button--info']").click()

# 3초 대기
time.sleep(3)

# 썸네일 버튼을 클릭
thumbnailbutn = driver.find_element(
    By.XPATH, "//*[@class = 'link-btn status-btn']").click()

# 3초 대기
time.sleep(3)

# Remote 메뉴 클릭
# Remotemenu = driver.find_element(
#     By.XPATH, "//*[@class='remote']").click()
Remotemenu = driver.find_element(
    By.XPATH, "//a[@href ='https://stgremote.virnect.com']").click()

# 5초 대기
time.sleep(5)

# 현재 활성화 된 탭
print(driver.window_handles)

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 5초 대기
time.sleep(5)

# 쿠키 및 이용통계 수집 동의 모달
cookiebtn = driver.find_element(
    By.XPATH, "//*[@class = 'cookie-policy-wrapper__submit-button']").click()

# 5초 대기
time.sleep(5)


# # 원격 협업 생성 버튼 클릭
# driver.find_element(By.XPATH,
#     "/html/body/section/div/div/div[1]/section/div[1]/button[1]").click()

remotecreatebtn = driver.find_element(
    By.XPATH, "//*[contains(text(), '원격 협업 생성')]").click()

# 5초 대기
time.sleep(5)

# 원격 협업 생성하기 모달창에서 멤버 선택하여 추가하기
# stgim875@gmail.com [1]
# stgim1516@gmail.com[1]
# stgim1314@gmail.com[2]
# stgim1112@gmail.com[3]
# stgim789@gmail.com[4]
# stgim456@gmail.com[5]
# stgim123@gmail.com[6]

createroommanager = driver.find_element(
    By.XPATH, "//*[@class = 'collapsible__content opend']/div[@class = 'widecard choice'][6]").click()

createroommanager = driver.find_element(
    By.XPATH, "//*[@class = 'collapsible__content opend']/div[@class = 'widecard choice'][6]").click()

# 5초 대기
time.sleep(5)

# 원격 협업 생성하기 시작하기 버튼 클릭
# createroommanager = driver.find_element(
#     By.XPATH, "//*[@class = 'btn large createroom-info__button']").click()

# 10초 대기
# time.sleep(10)

# permission 동의 팝업창 확인 선택하기
# 카메라 및 마이크 => options.add_argument("--use-fake-ui-for-media-stream")으로 fake 처리함

# 최근 열린 탭으로 전환
driver.switch_to.window(driver.window_handles[-1])

# 5초 대기
time.sleep(5)

# 현재 시점에 Remote 모바일 앱에서 알림 메뉴에서


# 추가 초대하기 버튼 클릭
# addbutton = driver.find_element(
#     By.XPATH, "//*[@class = 'participant-video append more']").click()
#
# # 5초 대기
# time.sleep(5)


# 녹화 버튼 클릭하기
# buttonmenu_1 = driver.find_element(
#     By.XPATH, "//*[@class='menus-box']/div[@class='tooltip tooltip-menu'][2]/button[@class='menu']").click()

# 3초 대기
# time.sleep(3)

# 녹화 버튼 다시 클릭하기
# buttonmenu_2 = driver.find_element(
#     By.XPATH, "//*[@class='menus-box']/div[@class='tooltip tooltip-menu'][2]/button[@class='menu active']").click()

# 5초 대기
# time.sleep(5)

# 나가기 버튼 클릭
# exit_ = driver.find_element(
#     By.XPATH, "//*[@class = 'header-tools__leave']").click()

# 5초 대기
# time.sleep(5)

# 최근 열린 탭으로 전환
# driver.switch_to.window(driver.window_handles[-1])

# 5초 대기
# time.sleep(5)

# 오픈 룸 생성 버튼 클릭
# openroomcreatebtn = driver.find_element(
#     By.XPATH, "//*[@class = 'btn workspace-welcome__open']").click()

# 로그아웃 시 매우 중요함
# status 메뉴 선택
# informatiobtn = driver.find_element(
#     By.XPATH, "//*[@class ='status-btn thumbnail-btn']").click()
