a=list(input("輸入五張牌:").split())
total=0
for i in range(5):
    if a[i]=='A':
        total += 1
    elif a[i]=='J':
        total +=11
    elif a[i]=='Q':
        total +=12
    elif a[i]=='K':
        total +=13
    else:
        total += int(a[i])
print(total)
    