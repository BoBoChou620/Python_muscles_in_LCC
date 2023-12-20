import csv

inputdata= r"D:\1011_Python 基礎程式語言 II\drugstore.csv"
outputdata= "drugstore_NTPBanquiao.csv"
outputstr="板橋區"

with open(inputdata, encoding="utf-8-sig") as readdata:
    #使用reader()函數建立readfile物件
    readfile= csv.reader(readdata)
    #傳換成list物件
    list_file=list(readfile)
    
with open(outputdata, "w",newline="",encoding="utf-8-sig") as outdata:
    writerdata=csv.writer(outdata)
    #條件式索引2等於字串"板橋區"才一行行輸出
    for i in list_file:
        if i[2] == outputstr:#記得有冒號縮排
            writerdata.writerow(i)
            