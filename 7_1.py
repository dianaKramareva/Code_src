a=int(input())
a1=0
a2=1
for i in str(a):
    if i==0 :
        break
    print(i)
    a1+=1
    a2+=int(i)
    print("сумма цифр равна", a2)
    print("количество цифр суммы", a1)