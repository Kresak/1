import math
import random

while True:
    print("Команда 0 завершит работу программы")
    s = input("Введите знак/команду (-, +, *, /, ^, модуль, !, арккосинус, рандом): ")
    if s == '0':
        break
    if s in ('-', '+', '*', '/', '^'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '-':
            print("%.2f" % (x-y))
        elif s == '+':
            print("%.2f" % (x+y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Ошибка: Деление на ноль!")
        elif s == '^':
            print(math.pow(x, y))

    elif s in ("модуль", "!", "арккосинус"):
        x = float(input("x="))
        if s == "модуль":
            print(abs(x))
        elif s == "!":
            print(math.factorial(x))
        elif s == "арккосинус":
            if x > 1 or x < -1:
                print("Ваше число не принадлежит промежутку от -1 до 1")
                continue;
            else:
                print(math.acos(x))
    elif s == "рандом":
        print(random.uniform(0, 10000))
    else:
        print("Ошибка: Неверный знак операции!")