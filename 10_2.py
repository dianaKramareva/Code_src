import random
n = int(input("Введите длину кортежа: "))
a = tuple(random.randint(1, 100) for _ in range(n))
min_a = min(a)
max_a = max(a)
print("Сгенерированный кортеж:")
for num in a:
    print(num)
print("Сумма минимального и максимального элементов:", min_a + max_a)


    