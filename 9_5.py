from random import randint
a=[randint(2500,3500) for i in range(10)]
print(a)
min1=min(a)
a.remove(min1)
min2=min(a)
print(min1, min2)
