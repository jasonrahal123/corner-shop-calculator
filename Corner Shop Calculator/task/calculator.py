# Write your code here
print("Earned amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")


Bubblegum = 202
Toffee = 118
Icecream = 2250
Milkchocolate = 1680
Doughnut = 1075
Pancake = 80

income = Bubblegum + Toffee + Icecream + Milkchocolate + Doughnut + Pancake
print("Income: $", income)

print("Staff expenses: ")
staff_expenses = float(input())

print("Other expenses: ")
other_expenses = float(input())

net_income = income - staff_expenses - other_expenses
print("Net income: $", net_income)

