from bs4 import BeautifulSoup
import requests
import urllib
import os
import datetime
from datetime import date
url="https://www.cwa.gov.tw/V8/C/"

#<img src="/Data/temperature/temp_forPreview.jpg" alt="" class="img-responsive">


# 先用requests請求
web =requests.get(url)
soup= BeautifulSoup(web.text,"lxml")
today = datetime.date.today()
# 先找到欲爬蟲的物件在HTML介面的所在絕對位置及共同性

picture_dir=(today+"中央氣象局天氣圖")
# 欲設置一資料夾專門存放圖片集，若不存在就產生一個資料夾
if not os.path.exists(picture_dir):
   os.mkdir(picture_dir)
#接者找尋所有img標籤

all_links= soup.find_all("img") 
for link in all_links:
    
    #所有的圖片的HTML路徑都在src下，取得src內容的字串轉成list
    attrs=[link.get("src")]
    for attr in attrs:
        if attr != None and(".jpg" in attr or ".png" in attr):
        # 設定圖片路徑
            full_path= attr
            file_name= full_path.split("/")[-1]
        # 由於路徑不完整所以要重新手動補齊
            img_path="https://www.cwa.gov.tw/"+full_path
            try:
              image= urllib.request.urlopen(img_path)
              fp=open(os.path.join(picture_dir, file_name),"wb")
              fp.write(image.read())
              print("圖片下載中...%s"%file_name)
              fp.close()
          
            except:
              print("下載失敗", file_name)
        


