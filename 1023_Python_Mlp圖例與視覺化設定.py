import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#一定要先設定中文才可以完成。
plt.rcParams["font.family"]="Microsoft JhengHei"
plt.rcParams["font.size"]=14

x= np.arange(1,11)
y1=pow(x,2)
y2=pow(x,3)

new_x= [str(i)+"月" for i in range(1,11)]

plt.plot(x, y1, lw=5, label="藍藍B")
plt.plot(x, y2, lw=3, label="橘橘O")

#設定圖例函數、圖例說明、圖例背景色
plt.legend(title="圖圖")
plt.grid(axis="y", ls="-.", color="m") #僅設置y軸輔助線,樣式,顏色

plt.xticks(x, new_x)
plt.show()            