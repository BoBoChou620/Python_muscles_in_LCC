x=[]

for i in range(10):
    x.append(i)
    print(x)    
    
y=[i for i in range(10) if i%2==0]
print(y)
list1 = ["紅色", "貓咪","羹",10, 3.134, 30, True]

print(type(list1))
print(list1[1])
print(list1[0])
print(list1[2:5])
print(list1[-1:-3:-1])
print(list1[::4])

for i in list1:
    print(i)
for i in range(len(list1)):
    print(list1[i])
    
#修改list內部的資料，直接對元素賦予新的
list1[6]=False
print(list1)

#修改2個以上的list內部資料，直接在:輸入指定索引值並更換
list1[2:5]="blue","orange"
print(list1)

#insert()插入排隊語法
list1.insert(3,"3.1415926")
print(list1)

#在list[]陣列中插入陣列
list1.insert(2,["宮崎駿", "EVA", "array", "3"])
print(list1)

