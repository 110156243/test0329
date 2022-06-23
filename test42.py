a=int(input("a:"))
print()
b=int(input("b:"))
print()
c=int(input("c:"))
ans=b**2-4*a*c
if ans>0:
    x=(round(-b/2*a,0))+(round((ans**0.5)/2*a,0))
    y=(round(-b/2*a,0))-(round((ans**0.5)/2*a,0))
    print(x)
    print()
    print(y)
elif ans==0:
    x1=-b/(2*a)
    print(x1)
elif ans<0:
    print("0")   