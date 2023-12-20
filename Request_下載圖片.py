import requests
url="https://s.yimg.com/ny/api/res/1.2/MqGTxjMi4T6eRguB3og4qg--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MDtoPTEyMzk7Y2Y9d2VicA--/https://media.zenfs.com/en/nownews.com/79680fe4ad80eb5c62522bb8d752bfa8"
response=requests.get(url)

#利用例外處理爬蟲

try: 
    # raise_for_status()可處理爬蟲時網頁請求失敗時的異常
    response.raise_for_status()
    print("取得網頁內容成功")
    
    # 以bytes的方式回傳網頁原始碼
    data = response.content
    # 將網頁原始碼寫成檔案，寫入模式用wb(以二進制方式寫入)
    with open("cat兔孫.jpg", "wb") as file:
        file.write(data)
        
except Exception as er:
    print("網頁圖片下載失敗",er)