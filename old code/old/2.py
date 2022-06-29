from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# USB: usb_device_handle_win.cc:1048 Failed to read descriptor
# from node connection:시스템에 부착된 장치가 작동하지 않습니다. (0x1F)
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])

# 사용할 webdriver 지정: Chrome 사용
driver = webdriver.Chrome(options=options)
# 진입할 경로 지정
driver.get("https://stgwww.virnect.com/")

# 웹페이지에서 특정 요소가 준비될 때까지 암묵적으로 대기한다.
driver.implicitly_wait(10)
# 웹페이지 해상도 조절
driver.set_window_size(1690, 1060)
