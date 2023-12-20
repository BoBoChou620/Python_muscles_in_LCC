import matplotlib.pyplot as plt
x=["國文","英文","數學","自然","社會"] 
data = {"A":[65, 85, 73, 52, 61],   
        "B":[72, 79, 64, 80, 91]}

# 設定中文
plt.rcParams["font.family"] = "Microsoft JhengHei"

# 設定布局大小1x2
fig, ax = plt.subplots(1, 2, figsize=(9, 3))

# 圖一為柱寬0.6、紫色柱體
# y軸範圍0~100
bar1 = ax[0].bar(x, data["A"], width=0.6, color="#AF35F0")
ax[0].set(ylabel="數量", title="預設様式", ylim=(0, 100))
ax[0].bar_label(bar1)  # 設定柱狀資料標鐵

# 圖二為柱寬0.4、綠色柱體
# y軸範圍0~120、柱體底部從刻度10開始
bar2 = ax[1].bar(x, data["B"], width=0.7, color="#32E6A2", bottom=0, edgecolor='black', linewidth=1.5)  # 添加黑色外框和粗度
ax[1].set(title="自訂基準位置", ylim=(0, 120))
ax[1].bar_label(bar2)  # 設定柱狀資料標籤

plt.show()

