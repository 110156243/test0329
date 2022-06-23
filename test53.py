a=int(input("輸入n值:"))
name=[]
mail=[]
for i in range(a):
    name1=input('請輸入姓名:')
    name.append(name1)
    mail1=input('請輸入電子郵件:')
    mail.append(mail1)
name2=input("請輸入要查詢電子郵件的姓名:")
if name2 in name:
    ans=name.index(name2)
    print(name2+'電子郵件帳號為'+mail[ans])
