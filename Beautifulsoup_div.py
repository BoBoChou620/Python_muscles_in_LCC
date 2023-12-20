from bs4 import BeautifulSoup

url="Example.html"

# 使用lxml解析器去解析Example.html網頁

with open(url,encoding="utf8") as file:
     soup= BeautifulSoup(file,"lxml")

# 取得標籤內容
# tag=soup.div
# print(tag)     

# P標籤的開始-結束的子標籤都會列印出來
tag_p=soup.find("p")
print(tag_p)
print("/"*20)
# =========HTML語法======================================================
# <p class="question">
# <a href="http://example.com/q1">請問你的性別?</a></p>     
# =======================================================================
tag_div2=soup.find(id="q2") #直接列印出q3標籤
print(tag_div2)
print("-"*20)
# =============================================================================
# <div class="survey" id="q2">
# <p class="question">
# <a href="http://example.com/q2">請問你是否喜歡偵探小說?</a></p>
# <ul class="answer">
# <li class="response">喜歡-<span>40</span></li>
# <li class="response selected">普通-<span>20</span></li>
# <li class="response">不喜歡-<span>0</span></li>
# </ul>
# </div>
# =============================================================================
tag_li_list=soup.find_all("li")
for row in tag_li_list: #for in迴圈去列印出來
    print(row.text)
print("~"*20) #我是分隔線
# 基本上都是用list的容器來接，
tag_li_list2=soup.find_all("div", class_="survey",limit=2)
for row in tag_li_list2: #for in迴圈去列印並限制只顯示前2
    print(row.text) 
print("★"*10) #我是分隔線