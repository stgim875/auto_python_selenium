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
driver.get(
    'https://stgconsole.virnect.com/?continue=https%3A%2F%2Fstgwww.virnect.com%2F')

# 아이디 입력창 선택
username = driver.find_element(By.NAME, "email")   /html/body/div/div/div/div/div[1]/input

# 아이디 입력
username.send_keys("maxgim875@gmail.com")

# 패스워드 입력창 선택
password = driver.find_element(By.NAME, "password")   /html/body/div/div/div/div/div[2]/input

# 패스워드 입력
password.send_keys("@rokmc875th")