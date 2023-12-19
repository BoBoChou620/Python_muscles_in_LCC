list1=[i for i in range(1,11)]
print(id(list1[9]))

list2=list1
list3=list1.copy()

list1[9]=100

print(id(list2[9]))
print(id(list3[9]))

x=[1,33,5,2,6,77,234,7,3.14,0,22,11]
print("原始資料經過排序後:",sorted(x))
print("我們再看一次原資料:",x)

y=(1,5,3,3,7,33)
y1=set({(1,5,3,3,7,33)})
print(y)
print(y1)

