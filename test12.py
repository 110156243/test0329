a=list(input("輸入一整數序列為:").split())
b=[]
for i in range(len(a)):
    q = 0 
    for j in range(len(a)):
        if a[i] == a[j] :
            q += 1
    b.append(q)

if max(b) > len(a)/2 :
    print("過半元素為:",a[b.index(max(b))])
else:
    print("過半元素為: NO")