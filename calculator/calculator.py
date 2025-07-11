import re

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль!"
    return a / b


print("Простой калькулятор")
print("Введите выражение (например, 2+3, 4 * 5, 10 / 2)")

while True:
    expr = input("Введите выражение: ")
    expr = expr.replace(" ", "")
    match = re.match(r"^(-?\d+(?:\.\d+)?)([+\-*/])(-?\d+(?:\.\d+)?)$", expr)
    if not match:
        print(
            "Ошибка: введите выражение в формате 'число операция число', например 2+3"
        )
        continue
    num1, operation, num2 = match.groups()
    num1 = float(num1)
    num2 = float(num2)

    if operation == "+":
        result = add(num1, num2)
    elif operation == "-":
        result = subtract(num1, num2)
    elif operation == "*":
        result = multiply(num1, num2)
    elif operation == "/":
        result = divide(num1, num2)
    else:
        print("Неверная операция! Пожалуйста, выберите из доступных: +, -, *, /")
        continue

    print(f"Результат: {result}")
    next_calculation = input("Хотите продолжить вычисления? (да/нет): ")
    if next_calculation.lower() != "да":
        break

