# --開始--批改評分使用，請勿變動
import matplotlib as mpl
mpl.use('Agg')
# --結束--批改評分使用，請勿變動

# 載入 matplotlib.pyplot 並縮寫為 plt
import matplotlib.pyplot as plt
# 載入 csv 模組
import csv

x = []
y = []

# 讀入 read.csv
with open('read_402 市場成交行情.csv', 'r', encoding='utf8') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(row[0]) #一次讀一行，索引0為6/14, 18.1迴圈跑完,就到[1]6/15
        y.append(float(row[1]))

x_ticks = range(1, len(x) + 1) #1~7
plt.plot(x_ticks, y,label="Banana") #開始畫折線圖，label="幫線取名字“
plt.xticks(x_ticks, x) #取代成x日期
plt.xlabel("Date") #x軸的名稱
plt.ylabel("NT$")
plt.ylim(15,25) #單獨調整y軸的上下線
# 添加圖表標題 title()
plt.title('Market Average Price') #圖表名稱
plt.legend()
# 使用 savefig() 函數
plt.savefig('chart402-折線圖.png')
plt.close()
