import pandas as pd
import numpy as np
import MySQLdb  # 安裝名稱為 mysqlclient(2.2.0)


file= r"C:\Users\wonde\OneDrive - 高雄師範大學\桌面\202308-11Java職訓課程\Python專題實作\進五年家庭暴力案件資料\地方檢察署家庭暴力案件-執行裁判確定人數(107~111).json"

data_json=pd.read_json(file)
print(data_json)

try:
    conn= MySQLdb.connect(host="localhost", #如果在公司就要用公司IP
                      user="root", #預設自定義
                      password="@Mmmm620816",#預設自定義
                      port=3306, #關於查詢方法在下方
                      database="global") #要查詢的資料庫

    data=pd.read_sql("SELECT * From countrydata", con=conn) #這裡要用到MySQL語法來找“countrydata”資料表
    conn.close() #資料庫記得要關閉，不然別人不能進去讀資料
except Exception as e: #若有例外錯誤則跳出以下訊息
    print("連接資料庫錯誤:",e)
    #例如，連接資料庫錯誤: (2002, "Can't connect to server on 'localhost' (10061)") → 修改port
    

# =============================================================================
# ※※ 關於通訊埠Port號的一些專用知識 ※※
# 通訊埠 Port=0~1023(不要亂改不然不能用!!!1024之後可以用~)
# HTTP=80
# HTTPS=443
# 可以用電腦 cmd模式去用findstr + port號碼，查詢PID，從工作管理員就可以找到正在使用這個port的應用程式)
# 查詢port使用狀況: nesttat -ano | findstr + 3306(port號)
#如何停用？本機>右鍵>服務與應用程式>內容>啟動類型>自動（開機時就已經喚醒了）
# =============================================================================

print(data_json.info()) #查詢資料資訊