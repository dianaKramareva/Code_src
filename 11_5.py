def calculate_deposit(amount, years, interest_rate=0.1):
 
  final_amount = amount * (1 + interest_rate) ** years
  return final_amount

# Пример использования:
initial_deposit = 10000 
term = 5  
result = calculate_deposit(initial_deposit, term)

print("Итоговая сумма на счету после",term," лет: ",result," грн.")
