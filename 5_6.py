import math
a = int(input("Введите "))
x = math.sin(a)+math.cos(a)/math.sin(a)-math.tan(a)
if x==0 :
    print("равно первому условию")
elif x<=0.8 :
    print("равно второму условию")
elif x>0.8 :
    print("равно третьему условию")
print(x)