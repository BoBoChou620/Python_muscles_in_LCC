#容器:dict字典一定是key(鑰匙):value(值)
x={"A":100,"B":20,"C":"abc", "A":5000}
print(x)
#創建Key的話不會有2個值，不然會以最後一個值來輸出
#不論順序只要對應到的值是相同的即可
y={"A":100,"B":20,"C":"abc"}

print("Key不能重複不然以最後一個value取代:",x)
y["D"]=50
print("使用y["+"D"+"]來插入一個新的key",y)
y1=set({(1,5,3,3,7,33)})
z=dict({"C":"abc","A":100,"B":20,})
print(x==z)
print(type(x))
print(x)
#雖然都是{}大括號但是不一定就是dict容器，還是要判斷
print(type(y))
print(y1)
print(type(y1))
#dict的語法有二種寫法
z=dict(B=20, C="abc", A=100, D=50) #第一種
w=dict([("B",20), ("A",100),("D", 50),("C","abc")])#第二種
print(z==y==w) #y為第一種寫法

#列印三種寫法且當中的Key-value都相同，搜尋以key索引為主
print(y)
print(z)
print(w)

print(len(y))



