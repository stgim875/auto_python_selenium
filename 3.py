from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# USB: usb_device_handle_win.cc:1048 Failed to read descriptor
# from node connection:시스템에 부착된 장치가 작동하지 않습니다.(0x1F)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 사용할 webdriver 지정: Chrome 사용
driver = webdriver.Chrome(options=options)
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

# 3초 대기
time.sleep(10)

# 원격 협업 생성 버튼 클릭(우선 수동으로)

# 원격 협업 생성하기 모달창에서 멤버 선택하여 추가하기
for i in range(1, len(driver.find_elements_by_xpath("//button"))):
    print(str(i)+"번째")
print(driver.find_elements_by_xpath("//button")[i].accessible_name)

driver.find_elements_by_xpath("//button")[1].click()

print(driver.window_handles, "팝업 : "+str(len(driver.window_handles))+"개")
[i for i in BeautifulSoup(driver.page_source, 'html.parser').findAll("iframe")]
