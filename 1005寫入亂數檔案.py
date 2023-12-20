#write() 寫入檔案函數，以下random函數

import random
file =open(r"C:\Users\wonde\python\a1\20231005\rand_number.py","w")
for i in range(10):
    file.write(str(random.randint(1,100))+'\n')
file.close