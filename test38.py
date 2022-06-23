a=int(input(""))
b=0
d=[]
for i in range(a):
    d.append(int(input("")))
for j in range(len(d)):
    if d[j] %9==0 or d[j]%11==0:
        print("第"+str(j+1)+"個點"+str(d[j]))
    else:
        b+=1
if b == a:
    print("0")
      