import math
import random

def minus(x,y):
    return x-y
def plus(x,y):
    return x+y
def umn(x,y):
    return x*y
def delen(x,y):
    return x/y
def stepen(x,y):
    return math.pow(x,y)
def modul(x):
    return math.fabs(x)
def fact(x):
    return math.factorial(x)
def arccos(x):
    return math.acos(x)
def random():
    return random.random

while True:
    print("Команда 0 завершит работу программы")
    s = input("Введите знак/команду (-, +, *, /, ^, модуль, !, арккосинус, рандом): ")
    if s == '0':
        break
    if s in ('-', '+', '*', '/', '^'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '-':
            print(minus(x,y))
        elif s == '+':
            print(plus(x,y))
        elif s == '*':
            print(umn(x,y))
        elif s == '/':
            if y != 0:
                print(delen(x,y))
            else:
                print("Ошибка: Деление на ноль!")
        elif s == '^':
            print(stepen(x,y))

    elif s in ("модуль", "!", "арккосинус"):
        x = float(input("x="))
        if s == "модуль":
            print(modul(x))
        elif s == "!":
            print(fact(x))
        elif s == "арккосинус":
            if x > 1 or x < -1:
                print("Ваше число не принадлежит промежутку от -1 до 1")
                continue;
            else:
                print(add(x,y))
    elif s == "рандом":
        print(arccos(x))
    else:
        print("Ошибка: Неверный знак операции!")