import math
import random

komandy1 = {'-', '+', '*', '/', '**'}
komandy2 = {"модуль", "!", "арккосинус", "рандом"}



while True:
    print("Команда 0 завершит работу программы.\n")
    sign = input("Введите знак/команду (-, +, *, /, **, модуль, !, арккосинус, рандом): ")
    #print("Для комманд <модуль> и <рандом> берётся только число x.\n")

    x = int(input("Введите число x: "))
    y = int(input("Введите число y: "))


    class Calculator:

        def dfb(self, num1, num2):
            self.x == num1
            self.y == num2

        def __init__(self, n1=x, n2=y):
            self.chislo1 = n1 * n2
            self.chislo2 = n1 / n2
            self.chislo3 = n1 - n2
            self.chislo4 = n1 + n2
            self.chislo5 = n1 ** n2
            self.chislo6 = abs(n1)
            self.chislo7 = random.uniform(0, 10000)
            self.chislo8 = math.factorial(n1)
            #self.chislo9 = math.acos(n1)

        def get_list(self):
            if sign in komandy1:

                #x = int(input("Введите число x: "))
                #y = int(input("Введите число y: "))

                if sign == '*':
                    print(x, " *", y, '=', self.chislo1)

                if sign == '/':
                    if self.chislo1 == 0:
                        print("Ошибка: Деление на ноль!")
                    else:
                        print(x, '/', y, '=', self.chislo2)

                if sign == '-':
                    print(x, '-', y, '=', self.chislo3)
                if sign == '+':
                    print(x, '+', y, '=', self.chislo4)
                if sign == '**':
                    print(x, '^', y, '=', self.chislo5)

            elif sign in komandy2:

                x = int(input("Введите число x: "))

                if sign == 'модуль':
                    print('Модуль', x, '=', self.chislo6)
                if sign == 'рандом':
                    print('Рандомное число: ', self.chislo7)
                if sign == '!':
                    print('Факториал(', x, ')=', self.chislo8)
                #if sign == "арккосинус":
                    #if -1 <= x <= 1:
                        #print('Арккосинус(', x, ')=', self.chislo9)
                    #else:
                        #print("Ваше число не принадлежит промежутку от -1 до 1")

    # calc.get_list(float(input("x = ")))

    calc = Calculator(x, y)
    print(calc.get_list())

    if sign == '0':
        break
