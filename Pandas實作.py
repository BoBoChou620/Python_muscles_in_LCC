import pandas as pd
import numpy as np
 
data= pd.Series(["Apple", "Manzana", "Alphe"])

#非常少更改索引值為自定義，因為要打正確index才能找到對應的value
s2=pd.Series(["蘋果","桃子","葡萄"], index=["第I個","第II個","第III個"])

#以下就是json檔案的形式：字串+value，但就是不能跑i迴圈啦
s3=pd.Series({"A":"皮卡丘", "B":"小火龍", "C":"傑尼龜", "D":"妙蛙種子"})

x=pd.Series([20,27,34], dtype=float)
y=pd.Series([20,27.5,34]) #會以float為主
z=pd.Series(["貓咪",20,27.5,24]) #會以String為主
print(data)
print(x)
print(y)
print(z)

data1 = pd.Series(np.random.randint(1,101,50))
print(data1)                
# =============================================================================
# DataFrames(可以調整index,values, colunms名稱)
# =============================================================================
score={"名稱":["皮卡丘", "妙蛙種子","鯉魚王"],
       "屬性":["電系","草系","水系"],
       "身長":[40,70,90]}
d1=pd.DataFrame(score)
print(d1)
#手動調整index索引值，因為0~2真的太醜所以改成神奇寶貝編號
d2=pd.DataFrame(score,index=["no.0001","no.0025","no.0129"])
print(d2)
# =============================================================================
#           名稱     屬性   身長
# no.0001   皮卡丘   電系   40
# no.0025  妙蛙種子  草系   70
# no.0129  鯉魚王    水系   90
# =============================================================================



#Pandas建立在Numpy上，所以等等在輸入CSV檔案時，都要換成數值才能做數學運算
data2=pd.DataFrame(np.arange(60).reshape(6,10)[:,:6])
print(data2)
