import requests
from bs4 import BeautifulSoup

url ="https://www.ptt.cc/bbs/index.html"

try:
    res = requests.get(url)
    soup= BeautifulSoup(res.text,"lxml")
    
    Hot_tiles=soup.find_all("div","board-title")
   
    print("批踢踢實業坊PTT今日的熱門版標:")
    for row in Hot_tiles:
        print(row.text)
except Exception as er:
    print("批踢踢實業坊PTT熱門版標加載失敗",er)
