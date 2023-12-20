import tkinter as tk

# 建立tk視窗
win=tk.Tk()
# 設定視窗標題，（）裡面記得是string“字串格式”
win.title("Tkinter Menu實作")

window_width = win.winfo_screenwidth()    # 取得螢幕寬度
window_height = win.winfo_screenheight()  # 取得螢幕高度

width = 800
height = 600
left = int((window_width - width)/2)       # 計算左上 x 座標
top = int((window_height - height)/2)      # 計算左上 y 座標
win.geometry(f'{500}x{500}+{1000}+{500}')
win.iconbitmap(r"C:\Users\wonde\Downloads\tkinter GUI介面設計\python_icon.ico")
# 設定視窗背景色
win.configure(bg_="#FFC1E0")

# 建立主選單
menu=tk.Menu(win)

# 建立上層第二子選單
submenu=tk.Menu(menu)
submenu.add_command(label="創建檔案") # 建立第二層子選單項目
submenu.add_command(label="另存新檔") # 建立第二層子選單項目
submenu.add_command(label="轉存為")   # 建立第二層子選單項目

# 建立底層第一子選單
menu.add_cascade(label="文件",menu=submenu)  # 建立第一層下拉選單
menu.add_command(label="編輯") # 建立第一層並列單項目
menu.add_command(label="工具") # 建立第一層並列單項目
menu.add_command(label="preference")# 建立第一層並列單項目
menu.add_command(label="說明(H)") # 建立第一層並列單項目
win.config(menu=menu)

win.mainloop()