import csv
fp1= r"C:\Users\wonde\Downloads\111年家暴通報案件統計_utf8.csv"
#SpyderIDE環境預設編碼方式為ANSCI，輸入讀取檔案格式的改為utf-82讀取

with open(fp1,encoding="utf-8") as data:
    #以csv屬性來讀data並且再以list盛裝，方便修改
    readfile =csv.reader(data)
    file=list(readfile)
    #print(readfile)，記得在python縮排有差別
    """若直接print(readfile)會變成<_csv.reader object at 0x00000186D9237760>
    跑出記憶體位置"""
    #可以方式呈現，因此可以用 list+ 迴圈方式帶出資料
    for i in range(len(file)):
        print(file[i]) 
    print(file)