a=list(input("輸入值為:").split(","))
max=""
min=""
for i in range(len(a)):
    a[i]=int(a[i])
a.sort()
for i in range(len(a)):
    min+=str(a[i])
a.reverse()
for i in range(len(a)):
    max+=str(a[i])
print("最大值數列與最小值數列的差值為 : ",int(max)-int(min))