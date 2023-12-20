from bs4 import BeautifulSoup
import requests
url="https://tw.news.yahoo.com"
web =requests.get(url)
soup= BeautifulSoup(web.text,"lxml")

#先找到新聞最外層的框架

break_news=soup.find("ul",class_="H(100%) D(ib) Mstart(24px) W(32.7%)")

tag_news= break_news.find_all("li", class_="Pos(r) Lh(1.5) H(24px) Mb(8px)")

for row in tag_news: #for in迴圈去列印出來
    print(row.text)
