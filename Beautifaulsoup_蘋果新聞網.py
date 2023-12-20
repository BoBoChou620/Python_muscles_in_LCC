from bs4 import BeautifulSoup
import requests
url="https://tw.nextapple.com/realtime/hit"
web =requests.get(url)
soup= BeautifulSoup(web.text,"lxml")

# 先找到新聞最外層的框架

Hot_news=soup.find("div",class_="post-hot stories-container")
# 每一則新聞都在熱門新聞裡面的"post-hot stories-container"
tag_news=Hot_news.find_all("article", class_="post-style3 infScroll")
# 可是我們的標題是又是在"post-style3 infScroll"
for row in tag_news:
    #for in迴圈列印出來最後再把a裏頭的"post-title"輸出就好。
    print(row.find("a",class_="post-title").text)
