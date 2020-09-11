from selenium import webdriver
import time

driver = webdriver.Chrome('./chromedriver.exe')
driver.get("https://papago.naver.com")
trans=input("")
time.sleep(10)
driver.fine_element_by_id('txtSourse').send_keys(trans)
time.sleep(10)
driver.fine_element_by_id('btnTranslate').click()
time.sleep(10)
