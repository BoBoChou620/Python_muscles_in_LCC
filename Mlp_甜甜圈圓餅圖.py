import matplotlib.pyplot as plt
import pandas as pd

x=[1,2,3,4,8] #請將All依照1:2:3:4:8分配比例
plt.pie(x,radius=1.4,
        autopct="%.1f%%",
        pctdistance=0.7,
        
        #百分比字樣設定
        textprops={"color":"w","weight":"bold", "size":14},
        # 甜甜圈的設定
        # 邊框寬度=3, 邊框=白色, 半徑長（大小）=o.8
        wedgeprops={"linewidth":3, "edgecolor":"w", "width":0.8})

plt.show()
