m,d = input("輸入月及日為:").split() 
a = ["",31,28,31,30,31,30,31,31,30,31,30,31]
b = ["",21,19,21,21,22,22,23,24,24,24,23,22]
c = ["Capricornus","Aquarius","Pisces","Aries","Taurus","Gemini","Cancer","Leo","Virgo","Libra","Scorpio","Sagittarius","Capricornus"]
m = int(m) 
d = int(d)
if 0 <= m and m <= 12 :
    if 0 <= d and d <= a[m]:
        if d < b[m]:
            print("星座為:",c[m-1])
        else:
            print("星座為:",c[m])