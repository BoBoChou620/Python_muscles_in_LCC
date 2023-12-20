from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import os

try:
    driver=webdriver.Edge()
    url="https://hahow.in/"
    driver.implicitly_wait(2)
    driver.get(url)

# 先用bs4解析當下網頁的HTML靜態的值。
    soup= BeautifulSoup(driver.page_source, "lxml")
# 解析完存成本機檔案的HTML檔並重新命名
    with open("Haohao.xtml", "w",encoding="utf-8") as file:
        file.write(soup.prettify())
    print("存檔成HTML檔成功！")

except Exception as error:
    print("爬取網頁失敗",error)
    #接者請將"Haohao.xtml"中的<script>元素刪除後並定位至欲爬蟲的標題部位
    # 並另開一個python檔並用Beautifual來爬取刪除後的靜態"Haohao_edit.xtml"
finally:
    driver.quit()