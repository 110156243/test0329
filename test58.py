a=[]
b=[]
for i in range(1,11):
    num=int(input("請輸入第"+str(i)+"個數字："))
    a.append(num)
    a.sort()
    a.reverse()
    b.append(num)
    b.sort()
print("最大的3個數字為：%d,%d,%d" %(a[0],a[1],a[2]))    
print("最小的3個數字為：%d,%d,%d" %(b[2],b[1],b[0]))