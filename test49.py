a=list(input("請輸入英文句子:").split())
str=[]
for i in range(len(a)-1,-1,-1):
    str.append(a[i])
print("輸出結果:",str)