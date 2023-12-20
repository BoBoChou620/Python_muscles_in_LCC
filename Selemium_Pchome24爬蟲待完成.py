from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import

#使用webdriver開始Edge瀏覽器
driver=webdriver.Edge()
url="https://24h.pchome.com.tw/"
driver.implicitly_wait(2)
driver.get(url)

# //*[@id="root"]/div/header/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/input
#尋找class="question"的標籤
try:    
     inputs = driver.find_elements(By.XPATH,'//*[@id="root"]/div/header/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/input')
     time.sleep(1) 
     inputs.click()
     inputs.send_keys('iphone 15 ')
   #輸入欲查詢的關鍵字
     element=driver.find_elements(By.XPATH,"//*[@id='root']/div/header/div[1]/div/div/div/div[2]/div/div[1]/button").click()
     
     driver.quit()
except Exception as er:
     print("輸入失敗！",er)


