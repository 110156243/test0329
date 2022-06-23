a=int(input("搭了幾次電梯:"))
now="1"
total=0

for i in range(a):
    next = int(input())
    if int(now) < next :
        total += (next - int(now))*20
        now = str(next) 
    elif int(now) > next : 
        total += (int(now) - next)*10
        now = str(next)
print(total,"元")