a=int(input("測試的資料量:"))
for i in range(a):
    f,m,k=input("").split()
    if (f=='O' and m=='O'):
        if k=='O':
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif (f=='O' and m=='A') or (f=='A' and m=='O'):
        if k =='A' or k=='O':
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif (f=='O' and m=='B') or (f=='B' and m=='O'):
        if k=='B' or k=='O':
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif (f=='O' and m=='AB') or (f=='AB' and m=='O'):
        if k=='A' or k=='B':
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif (f=='A' and m=='A'):
        if k=='A' or k=='O':
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif (f=='A' and m=='B') or (f=='B' and m=='A'):
        if k=='A' or k=='B' or k=='O' or k=='AB':
            print("YES")
    elif (f=='A' and m=='AB') or (f=='AB' and m=='A'):
        if k=='A' or k=='B' or k=='AB':
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif (f=='B' and m=='B'):
        if k=='B' or k=='O':
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif (f=='B' and m=='AB') or (f=='AB' and m=='B'):
        if k=='A' or k=='B' or k=='AB':
            print("YES")
        else:
            print("IMPOSSIBLE")
    elif (f=='AB' and m=='AB'):
        if k=='A' or k=='B' or k=='AB':
            print("YES")
        else:
            print("IMPOSSIBLE")
