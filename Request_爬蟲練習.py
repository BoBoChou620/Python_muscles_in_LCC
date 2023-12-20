import requests

#欲爬蟲的網站網址
url="https://tw.yahoo.com"


response=requests.get(url)
#若請求狀態為200（有回應）時則輸出以下response物件內容
if response.status_code == requests.codes.ok:
    print("網頁內容資料取得成功")
    print("網頁編碼：",response.encoding)
    print("網頁內容大小", len(response.text))
    print("表頭訊息：",response.headers)
    print("cookie訊息：",response.cookies)
    print("網頁原始碼")
    print(response.text)
else:
    print("網頁取得資料失敗")