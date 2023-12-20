import requests
url=input("請輸入欲下載的網址：")
response=requests.get(url)

#利用例外處理爬蟲

try: 
    # raise_for_status()可處理爬蟲時網頁請求失敗時的異常
    response.raise_for_status()
    print("取得網頁內容成功")
    
    # 以bytes的方式回傳網頁原始碼
    data = response.content
    # 將網頁原始碼寫成檔案，寫入模式用wb(以二進制方式寫入)
    with open("getdata.html", "wb") as file:
        file.write(data)
except Exception as er:
    print("網頁下載失敗",er)