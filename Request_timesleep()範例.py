import time,requests

url="https://odportal.tw/dataset/kTCMDArg"
#對欲請求的網站發出請求次數

for i in range(10):
    response=requests.get(url)
    print(response.status_code)
    time.sleep(4)