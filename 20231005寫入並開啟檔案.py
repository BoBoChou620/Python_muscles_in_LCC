#將file的預設函數OPEN打開並’W‘覆寫在data.txt檔

text='將全部內容全部存起來'
print(text, file=open('data.txt', 'w'))

#方法二：複製檔案路徑（錯誤就換\\或是/）

data='''2020
陳伯偉〈讓性 empower 障礙者：性不只是權利，更應是社會福利〉。《性別平等教育季刊》，89: 111-116。
'''
print(data, file=open("C:\\Users\\wonde\\python\\a1\\20231005\\data1.txt", 'w'))

#方法三：使用raw string函數在檔案路徑前，就不用每個都調整）

data1='''
123
456
789
012
345
678
901'''

print(data1, file=open(r"C:\Users\wonde\python\a1\20231005\todaypython.py",'w'))