import requests
import pandas as pd

url="https://data.ntpc.gov.tw/api/datasets/0f0c4a15-12ce-4c3c-a3e9-b76430a737a3/json"
response=requests.get(url)

if response.status_code == requests.codes.ok:
    # 將回應資訊以json()函數轉成DataFrame
    data=pd.DataFrame(response.json())
else:
    print("取得網頁內容失效")    