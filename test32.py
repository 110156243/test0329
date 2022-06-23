money=int(input("小明身上有幾元:"))
a=0
drink=[]
series=int(input("販賣機有幾種飲料:"))
for i in range(series):
    drink.append(int(input("")))
    if money>=int(drink[i]):
        a+=1
print(a)        