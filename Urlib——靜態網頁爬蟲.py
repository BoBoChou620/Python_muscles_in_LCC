import urllib
import requests

url="https://www.klchb.klcg.gov.tw/tw/klchb/"

try:
    # 向欲爬蟲的網頁發送請求後得到一個回應物件
    # 若超過5秒都未得到回應，則拋出異常
    response =urllib.request.urlopen(url, timeout=5)
    print(response.read()) #若有則會回傳200
    print("版本：", response.version)
    print("網址：", response.geturl())
    print("狀態為", response.status)
   
# ====列印結果如下：============================================================
#     版本： 11
#     網址： https://www.ithome.com.tw/
#     狀態為 200
# =============================================================================
    # 讀取表頭資訊
    print(response.getheaders())

except urllib.error.URLError as e:
    print(e.reason)
 
