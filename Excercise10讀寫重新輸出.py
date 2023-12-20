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
    for i in  list_file:
        if i[2] == outputstr:
         writerdata.writerow(i)