from bs4 import BeautifulSoup
import requests
url="https://water.taiwanstat.com/"

web =requests.get(url)
soup= BeautifulSoup(web.text,"lxml")

name=soup.find_all("div", class_="reservoir")
for row in name:
   print(row.text)


