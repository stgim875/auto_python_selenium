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
    "//div[@class ='email-input el-input el-input--suffix']/input[1]").send_keys('아이디 입력')

# 3초 대기
time.sleep(3)

# 패스워드 입력창 위치 찾기 및 패스워드 입력
userpw = driver.find_element(
    By.XPATH,
    "//div[@class = 'password-input el-input el-input--suffix']/input[1]").send_keys('패스워드 입력')

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
Remotemenu = driver.find_element(
    By.XPATH, "//a[@href ='https://stgremote.virnect.com']").click()

여기까지가 Product 홈페이지창(첫번째 탭), 즉, 첨부 파일 1번과 2번에 속함

###########################################################################################
71번 코드가 실행이 되면 새창이 열려서 Remote 라는 화면으로 이동됩니다.(첨부 파일 확인)
이 화면에 원격 협업 생성 및 오픈 룸 생성 버튼이 있는데요.
지금 이 코멘트 자리에는 Remote라는 새창이 열리니 새창으로 화면 전환을 해서 다음 코드들을 실행 시켜야 한다고 알려줘야 하지 않을까? 생각이듭니다.

아마도 71번 실행하는 즉시, 새창으로 화면이 이동이 되었는데 이에 대한 처리가 안되어 있다 보니 원격 협업 생성 및 오픈 룸 생성, 원격 협업 생성 버튼 클릭 > 원격 협업 생성하기 모달창에서 멤버 선택하여 추가하기 구현한 코드들은 계속 첫번째 화면탭이라고 생각해서 첫번째 화면에서 각 코드들을 실행 시키고 있는 것 같습니다.
이거 아니고서는 클릭 안될 이유가 없는거 같아요... 제가 이러한 정보들을 설명을 먼저 드렸어야 하는데 그냥 클릭하면 되는줄 알고....ㅠ.ㅠ

한번 제 의견 확인 좀 부탁 드려요.. 제 생각이 만약 맞다면 말씀 드린 코드는 어떻게 작성하면 되는지 좀 알려 주시면 될 것 같습니다.

###########################################################################################


###########################################################################################
지금부터는 Remote 새창(두번째 탭) 첨부 파일 3번에 속함


# 5초 대기
time.sleep(5)

# 쿠키 및 이용통계 수집 동의 모달
# cookiebtn = driver.find_element(
#     By.XPATH, "//*[@class = 'cookie-policy-wrapper__submit-button']").click()

# 5초 대기
time.sleep(5)

# 원격 협업 생성 버튼 클릭
driver.find_element_by_xpath(
    "/html/body/section/div/div/div[1]/section/div[1]/button[1]").click()

# 원격 협업 생성하기 모달창에서 멤버 선택하여 추가하기

# 오픈 룸 생성 버튼 클릭
driver.find_element_by_xpath(
    "/html/body/section/div/div/div[1]/section/div[1]/button[2]").click()
