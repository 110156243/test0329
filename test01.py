a = input("請輸入正整數 : ")
res = []
for i in range(0,len(a)):
    for j in range(i+1):
        say = int(a[j:len(a)-i+j])
        if say % 2 == 1 :
            sayl = []
            for k in range(1,say+1):
                if say % k == 0 :
                    sayl.append(k)
            if len(sayl) == 2 : res.append(say)

if len(res) == 0:
    print("子字串中最大的質數是 : No prime found")
elif len(res) == 1 and 1 in res:
    print("子字串中最大的質數是 : No prime found")
else:
    print("子字串中最大的質數是 : ",max(res))