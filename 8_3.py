p = 0
while True:

        x = input()
        y = input()
        if x == "хватит" or y == "хватит":
            break
        x = int(x)
        y = int(y)
        a = x / y
        p += 1
        if p > 0:
            print(a, p)
