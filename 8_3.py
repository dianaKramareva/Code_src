x= int(input("Введите число"))
while x>=0 :
    x-=8
    if x%6==0 and x%10==3 :
        continue
    print (x, end=" ")