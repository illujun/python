from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# 실행경로와 드라이버 객체 생성
driver = webdriver.Chrome()
wikidocs = []

for i in range(20):
    driver.get('http://wikidocs.net/'+str(i))
    title = driver.title
    url = driver.current_url
    wikidocs.append({"url" : url, "title" : title})

print(wikidocs)