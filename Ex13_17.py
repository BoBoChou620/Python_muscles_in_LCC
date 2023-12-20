import pandas as pd

# 先列再欄
names = ["小林", "小黃", "小陳", "小美"]
columns = ["國語", "數學", "英文", "自然", "社會"]
point = [[75, 62, 85, 73, 60], [91, 53, 56, 63, 65],
         [71, 88, 51, 69, 87], [69, 53, 87, 74, 70]]
data = pd.DataFrame(point, columns=["國語", "數學", "英文", "自然", "社會"],  index=["小林", "小黃", "小陳", "小美"])

print('學生成績總表：')
print(data)
print("==============================")

# 輸出陳&美的成績
data1=data.iloc[2::]
print("小陳與小美的成績分別為：")
print(data1)
print("------------------------------")

# 輸出自然的成績並且遞減
#data_science = data.loc[0:4:4]
data2=data.sort_values(by="自然", ascending= False)
print('自然的成績排名（遞減）')
print(data2["自然"])
print("##############################")

# 列印小黃成績，並將英文改成=80
data3=data.loc[1,2]=80
print('小黃的英文成績：')
print(data3)
