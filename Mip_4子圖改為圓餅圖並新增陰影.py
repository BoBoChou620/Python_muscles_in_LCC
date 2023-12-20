import matplotlib.pyplot as plt
import numpy as np

# 設定中文字型
plt.rcParams["font.family"] = "Microsoft JhengHei"
plt.rcParams["font.size"] = 14

# 建立一個2x2的畫布
fig, ax = plt.subplots(2, 2)

# 在左上角(0,0)的格子裡繪製圖表
sizes1 = [60, 40]  # 百分比設定
colors1 = ['#5F38E0', 'white']
ax[0][0].pie(sizes1, colors=colors1, labels=["甜甜圈 1", ""], autopct='%1.1f%%', startangle=140, shadow=True)  # 增加陰影
ax[0][0].set_title("picture 1")

# 在右下角(1,1)的格子裡繪製圖表
sizes2 = [25, 75]  # 百分比設定
colors2 = ['#F71670', 'white']
ax[1][1].pie(sizes2, colors=colors2, labels=["甜甜圈 2", ""], autopct='%1.1f%%', startangle=90, shadow=True)  # 增加陰影
ax[1][1].set_title("picture 2", loc=8)  # 將標題設置在底部
# 設定子圖上下間距.4,左右間距0.5
plt.subplots_adjust(hspace=0.25, wspace=0.4)

# 整體圖表標題
plt.suptitle("子圖範例")
plt.show()
