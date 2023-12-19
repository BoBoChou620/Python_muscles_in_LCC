def generate_matrix(rows, columns):
    if rows < 1 or columns < 1:
        print("請輸入大於等於1的列數和欄數。")
    else:
        for i in range(rows):
            for j in range(columns + 1):
                print(f"{j - i:4}", end=" ")
            print()

rows = int(input("請輸入列數（整數）："))
columns = int(input("請輸入欄數（整數）："))

generate_matrix(rows, columns)

for _ in range(5):
    print("Hello")
    
    
import math
pi =math.pi

def circle(x):  #定義一個新函數
    ans = x*x*pi
    return ans  #一個參數，呼叫就是丟回一個

x=circle(6) #有人丟就要有人接print()才會輸出有東西
print(x)
