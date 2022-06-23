dict1={}
a=int(input("輸入筆數n:"))
for i in range(a):
    en,chi=map(str,input("").split()) 
    dict1[en]=chi
que=input("輸入欲查詢單字:")
answer=dict1.get(que)
if answer==None:
    print("字典未有此單字")
else:
    print(que+"中文意思為"+answer)    