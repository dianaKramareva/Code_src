x_min = float(input("Введите минимум"))
x_max = float(input("Введите максимум"))
step = int(input("Введите шаг"))
a = 0
while x_min<=x_max :
    y=1.3*x_min*3 - 8*x_min/5
    a+=1
    x_min+=step
    if a==7 :
        break
    print(x_min, "->", round(y,3))