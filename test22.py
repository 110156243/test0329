a=int(input("輸入查詢組數N為:"))
account={'123':'456','456':'789','789':'888','336':'558','775':'666','566':'221'}
password={'456':9000,'789':5000,'888':6000,'558':10000,'666':12000,'221':7000}
for i in range(a):
    act,pwd=input("").split()
    if pwd == account[act]:
        print(password[pwd])
    else:
        print("error")