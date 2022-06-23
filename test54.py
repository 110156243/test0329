a=float(input("請輸入路程公里數(km)："))
total=75
while(a>1.5):
    total+=5
    a-=0.25
print("所需車資為："+str(total))