from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

#使用webdriver開始Edge瀏覽器
driver=webdriver.Edge()
url=os.path.abspath(r"C:\Users\wonde\Downloads\Example.html")
driver.implicitly_wait(3)
driver.get(url)

try:
#尋找class="question"的標籤
   tags =driver.find_elements(By.ID,'emails')
   for tag in tags:
     print(tag.text) 
     print("爬取元素成功！")

except Exception as er:
    print("爬取元素失敗！",er)

finally:
 time.sleep(3)
 driver.quit()
