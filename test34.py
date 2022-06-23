from ast import Return
from urllib3 import Retry


num=int(input("輸入一正整數(11<=n<=1000):"))
while num>=11 and num<=1000:
    if (num%2==0 and num%11==0):
        if(num%5!=0 and num%7!=0):
            print(str(num)+"為新公倍數?:"+"Yes")
    else:
        print("No")
    break


