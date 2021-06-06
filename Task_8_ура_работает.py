import math
import random
import sys


komandy1 = {'-', '+', '*', '/', '**'}
komandy2 = {"модуль", "!", "арккосинус"}
komandy3 = {"рандом"}

while True:
    class Calculator:
        def calculate(self, operator, a=0.0, b=0.0):
            if operator in komandy2:
                if operator == 'арккосинус':
                    if -1 <= a <= 1:
                        return math.acos(a)
                    else:
                        print("Ошибка: Ваше число не принадлежит промежутку от -1 до 1!")

                elif operator == 'модуль':
                    return abs(a)
                elif operator == '!':

                    return math.factorial(a)

            elif operator in komandy1:
                if operator == '-':
                    return print(a, '-', b, '=', a-b)
                elif operator == '+':
                    return print(a, '+', b, '=', a+b)
                elif operator == '*':
                    return print(a, '*', b, '=', a*b)
                elif operator == '/':
                    try:
                        a / b
                    except ZeroDivisionError:
                        print('Ошибка: Деление на ноль!')
                        return None
                    return print(a, '/', b, '=', a/b)
                elif operator == '**':
                    return print(a, '**', b, '=', a**b)

            elif operator in komandy3:
                return random.randint(0, 1000)
            return None


    mathMethod = input("Введите знак/команду (-, +, *, /, **, модуль, !, арккосинус, рандом): ")
    result = 0
    myCalculator = Calculator()

    if mathMethod in komandy2:
        number = input("Введите число: ")

        try:
            number = float(number)
        except ValueError:
            print("Ошибка: Это не число!")
            sys.exit(1)

        result = myCalculator.calculate(mathMethod, number)

    elif mathMethod in komandy1:
        x = input("Введите число x: ")
        y = input("Введите число y: ")

        try:
            x = float(x)
            y = float(y)
        except ValueError:
            print("Ошибка: Это не число!")
            sys.exit(1)

        result = myCalculator.calculate(mathMethod, x, y)

    elif mathMethod in komandy3:
        result = myCalculator.calculate(mathMethod)

    else:
        print("Ошибка: Нет такого математического оператора!")
        sys.exit(1)

    if result is not None:

        print("Ответ на команду", mathMethod, " - ", result)