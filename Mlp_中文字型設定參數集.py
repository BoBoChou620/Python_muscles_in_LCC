import numpy as ny
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

#設定中文形式字集
plt.rcParams["font.family"]="Microsoft JengHei"
#plt.rcParams["font.sans-serif"]="SimHei" #這是MacOS專用細黑體
plt.rcParams["font.size"]=14 #字體大小
plt.rcParams["exes,unicode_minus"=False #讓負數可以正常呈現 

             
x=np.range(1,10)
plt.plot(x,x**3,"--", marker="^")

#指定中文字型的位置設定



#輸出圖名稱
plt.savefig('chart.png')
plt.close()
