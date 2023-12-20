import matplotlib.pyplot as plt
x = ["2017-01" "2017-02" " 2017-03" " 2017-04"
"2017-05" "2017-06" "2017-07" "2017-08"" 2017-09" "2017-10"
" 2017-11" "2017-12"]

y = [86, 85, 84, 80, 75, 70, 70, 74,78, 70,74,80]

#設畫布大小為16x4
plt.figure(figsize=(16,4))
# 繪製長條圖
plt.plot(x, y, linewidth=3, color="#E0266F",marker="o",markersize=12)

#設置資料標,在位(x,y)上顯示字
#對齊方式重直方向底部、水平方向-置中,字體大小20
for a, b in zip(x, y):
   plt.text(a, b, b, ha="center" ,va="bottom" , fontsize=20)

plt.show()