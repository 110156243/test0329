a=int(input("輸入第一行正整數為:"))
b=list(input("第二行中數列中的數字為:").split())
count=0
count1=0
for i in range(0,len(b)):
    if b.count(b[i])> count:
         count=b.count(b[i])
         count1=b[i]
print("最大出現次數的數字為:"+str(count1))
print("出現次數為:"+str(count))