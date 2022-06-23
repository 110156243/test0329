a=int(input("輸入筆數n:"))
list1=[]
list2=[]
for i in range(a):
    keys,values=map(str,input("").split())
    list1.append(keys)
    list2.append(values)
for i in range(a):
    print(list1[i]+"牌得到"+list2[i]+"面")
