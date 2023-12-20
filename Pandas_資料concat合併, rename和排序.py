import pandas as pd
 
d1=pd.DataFrame({"A":[1120,45,67],
                 "B":["marine", "pekora", "miko"]})
d2=pd.DataFrame({"C":[100.512]})

data=pd.concat([d1,d2], axis=1)
#合併資料後更換columns名稱，記得把data丟回給data
data1 = data.rename(columns={"B":"姓名", "C":"數值"})
# =============================================================================
# 資料排序~
# #排序，預設為升冪排序，若要降冪 ascending=False
# =============================================================================
data = data.sort_values("A")
print(data1.head())
print("==========================")

data1 = data.sort_values("A", ascending=False)
print(data.head())
print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
data2=data1.fillna(0)
data2["C"]=data2["C"].astype("int")
print(data2)

