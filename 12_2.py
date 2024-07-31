def sum_numbers(n):

  return n * (n + 1) // 2
n = int(input("Введите верхнюю границу (n): "))
result = sum_numbers(n)
print("Сумма натуральных чисел ", result)
