import matplotlib.pyplot as plt
import numpy as np
#關於散點圖的應用多用於線性回歸、機器學習等應用
#設定x與y軸資料

x = color = np.arange(1,11) #有對應到預設色票
y = np.random.randint(1,10,10)

#將資料代入圖表,自訂顏色與點的大小

plt.scatter(x, y, c=color, s=200)
#顯示圖表
plt.show()