import matplotlib.pyplot as plt
import numpy as np
x = np.arange(0.0, 2.0, 0.01)
y1 = np.sin(2*np.pi*x)
y2 = [3,4,5,6,7]

#設定中文字型
plt.rcParams["font.family"] = "Microsoft JhengHei"
plt.rcParams["font.size"]=14

#建立一個2x2的畫布
fig, ax = plt.subplots(2,2)

#在左上角(0,0)的格子裡繪製圖表
ax[0][0].plot(y1,c="#5F38E0") #設定圖表資料、線條樣式
ax[0][0].set_title("picture 1") #設定圖表名稱

#在右下角(1,1)的格子裡繪製圖表
ax[1][1].plot(y2,"--",c="#F71670" ) #設定圖表資料、線條樣式
ax[1][1].set_title("picture 2") #設定圖表名稱
ax[1][1].set_ylim(0,10) #將y軸刻度範圍設定0~10

#設定子圖上下間距.4,左右間距0.5
plt.subplots_adjust(hspace=0.25, wspace=0.4)

#整體圖表標題
plt.suptitle("子圖範例")
plt.show()