from bs4 import BeautifulSoup
import requests

url="https://www.ez2o.com/App/Net/IP"

try:
    #先用requests請求回應
    web=requests.get(url)
    soup= BeautifulSoup(web.text, "lxml")
    #先找出table欄位的位置
    table=soup.find("table", class_="table table-striped table-hover")
    data=table.find_all("tr",class_="active")
    #ip位置在tr標籤的索引1內
    ip=data[1].text
    print("目前您的所在"+ip)
except Exception as erros:
    print("IP位置下載失敗",erros)