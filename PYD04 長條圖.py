# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

#必要
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

# 讀取學生分數資料
# 讀取 read.csv
df = pd.read_csv("read.csv")
#呼叫出來的scores都是numpy objects
scores = df["scores"].values

# range_count[0]: range0~19
# range_count[1]: range20~39
# range_count[2]: range40~59
# range_count[3]: range60~79
# range_count[4]: range80~100
# 以0初始化計數串列

range_count = [0] * 5 #[0,0,0,0,0]

# 計數過程(索引就是[0,1,2,3,4]分別丟進去跑70次)
for score in scores:
    if score < 20:
        range_count[0] += 1
    elif score < 40:
        range_count[1] += 1
    elif score < 60:
        range_count[2] += 1
    elif score < 80:
        range_count[3] += 1
    else:
        range_count[4] += 1

# y軸標籤
index = np.arange(0, 25, 5)
# X軸刻度
labels = ["0~19","20~39", '40~59', "60~79", '80~100']
# 畫出長條圖(bar)，寬度2
plt.bar(index, range_count, 2)
# 設定X軸名稱
plt.xlabel('Range', fontsize=14)
# 設定Y軸名稱
plt.ylabel('Quantity', fontsize=14)
# 設定x軸標籤
plt.xticks(index, labels)
# 設定y軸標籤
plt.yticks(index)
# 設定圖名稱
plt.title('Score ranges count', fontsize=20)
# 輸出圖片檔案
plt.savefig('chart-長條圖.png')
plt.close()
