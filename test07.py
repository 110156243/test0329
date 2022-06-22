a=int(input("輸入月租費型式:"))
b=int(input("輸入通話時間:"))
if a==186:
    total=b*0.09
    if total<=186:
        print("通話費為:186")
    elif total >186:
        if total<=186*2:
            print("通話費為:",round(total*0.9))
        elif total>186*2:
            print("通話費為:",round(total*0.8))
elif a==386:
    total=b*0.08
    if total<=386:
        print("通話費為:386")
    elif total >386:
        if total<=386*2:
            print("通話費為:",round(total*0.8))
        elif total>386*2:
            print("通話費為:",round(total*0.7))
elif a==586:
    total=b*0.07
    if total<=586:
        print("通話費為:586")
    elif total >586:
        if total<=586*2:
            print("通話費為:",round(total*0.7))
        elif total>586*2:
            print("通話費為:",round(total*0.6))
elif a==986:
    total=b*0.06
    if total<=986:
        print("通話費為:986")
    elif total >986:
        if total<=986*2:
            print("通話費為:",round(total*0.6))
        elif total>986*2:
            print("通話費為:",round(total*0.5))
