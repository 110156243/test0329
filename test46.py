dict1={}
n=int(input("輸入比數n:"))
for i in range(n):
    a,b=map(str,input("").split()) 
    dict1[a]=b
for keys,values in dict1.items():
    print(keys+"牌得到",values+" "+"面")