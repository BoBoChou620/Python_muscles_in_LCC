import pandas as pd
import requests
url1 = "https://data.ntpc.gov.tw/openapi/swagger-ui/index.html?configUrl=%2Fapi%2Fv1%2Fopenapi%2Fswagger%2Fconfig&urls.primaryName=%E6%96%B0%E5%8C%97%E5%B8%82%E6%94%BF%E5%BA%9C%E4%B8%BB%E8%A8%88%E8%99%95(622)#/CSV/get_071cfeb3_05ab_4690_88ff_cbd036812c7d_csv"
url2 = "https://data.ntpc.gov.tw/api/datasets/0f0c4a15-12ce-4c3c-a3e9-b76430a737a3/csv?size=100"
data1 = requests.get(url1).text
data2 = requests.get(url2).text
print(data1+data2)

data=pd.read_csv("https://data.ntpc.gov.tw/openapi/swagger-ui/index.html?configUrl=%2Fapi%2Fv1%2Fopenapi%2Fswagger%2Fconfig&urls.primaryName=%E6%96%B0%E5%8C%97%E5%B8%82%E6%94%BF%E5%BA%9C%E4%B8%BB%E8%A8%88%E8%99%95(622)#/CSV/get_071cfeb3_05ab_4690_88ff_cbd036812c7d_csv")
