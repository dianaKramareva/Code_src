x1=float(input())
x2=float(input())
step=int(input())
a=0
while x1<=x2 :
    y=1.3*x1*3-8*x1/5
    print(x1,"->", round(y,3))
    x1 += step
    a +=1
    if a==7:
        break