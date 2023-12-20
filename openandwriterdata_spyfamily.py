import csv

with open("Spy_family_data.csv","w",newline="", encoding="utf-8") as data:
    #使用writer()函數建立物件
    #方便使用writerow(寫一行)的方法
    
    writefile =csv.writer(data)
    writefile.writerow(["姓名","職業","年齡","代號"])
    writefile.writerow(["洛伊德","間諜","32","黃昏"])
    writefile.writerow(["約兒","職業殺手","28","荊棘公主"])
    writefile.writerow(["安妮亞","小孩","5","WakuWaku"])
                        
    #Excel: Alt+G 選擇[空格]或[值]自動標示後，可編輯刪除