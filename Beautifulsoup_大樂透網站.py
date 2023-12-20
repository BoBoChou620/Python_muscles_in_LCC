from bs4 import BeautifulSoup
import requests
url="https://www.taiwanlottery.com.tw/index_new.aspx"

#先從requests請求大樂透網站回應開始
web =requests.get(url)
soup= BeautifulSoup(web.text,"lxml")


# 找尋號碼所在位置 class="contents_box02"的區塊
tag_number=soup.find_all("div",class_="contents_box02")
# 找出來的tag_number結果會有4個，但是我們要的是第3個的「大樂透」，所以索引值為2
data1=tag_number[2]

# 要找的號碼會在每個fiv的class="ball_tx ball_yellow"標籤底下
data2=data1.find_all("div",class_="ball_tx ball_yellow")

print("本期號碼為：",end="")
for i in range(0 ,6):
    print(data2[i].text, end="")
print("★"*16)
print("開出順序：  ",end="")
for i in range(6, len(data2)):
    print(data2[i].text, end="")
print("\n"+"="*28)
# 最後輸出特別號
data3=data1.find("div", class_="ball_red")
print("※今日特別號是：%s"%data3.text)
