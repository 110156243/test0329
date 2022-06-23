while True:
    a=input("檢測的字串(end 結束):")
    list1=list(a)
    if a=='end':
        print("檢測結束")
        break
    check=input("檢測單一字元")
    if check in list1:
        answer=list1.count(check)
        print("字元"+check+"出現次數為:"+str(answer))