import csv

indata =r"C:\Users\wonde\Downloads\家暴及性侵害被害人就業協助人數-按性別分資料.csv"
output ="DV_job.csv"

with open(indata, encoding="utf8") as readdata:
    #使用reader()函數建立readfile物件
    readfile= csv.reader(readdata)
    #傳換成list物件
    list_file=list(readfile)
    
with open(output, "w",newline="", encoding="utf8") as data:
     writerdata=csv.writer(data)
     for row in list_file:
         writerdata.writerow(row)