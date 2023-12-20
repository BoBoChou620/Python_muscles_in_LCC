from bs4 import BeautifulSoup
import requests

# yahoo新聞
url = "https://tw.news.yahoo.com/"
# 先用requests請求回應
web = requests.get(url)
# 使用lxml解析器去解析yahoo新聞網頁(需轉為text型式)
soup = BeautifulSoup(web.text, "lxml")

# 先找到置頂新聞最外層的框架
break_news = soup.find("ul", class_="H(100%) D(ib) Mstart(24px) W(32.7%)")
# 再逐步搜尋每條新聞的標籤與屬性
tag_news = break_news.find_all("li", class_="Pos(r) Lh(1.5) H(24px) Mb(8px)")

# 將新聞標題逐個輸出
for row in tag_news:
    print(row.text)
    
    