import math
import random

komandy1 = {'-', '+', '*', '/', '^'}
komandy2 = {"модуль", "!", "арккосинус"}


class Calc:
    def numbers(self, chislo1, chislo2=0): #self - ссылается на конкретный экземпляр класса, а не на класс в целом
        self.x = chislo1
        self.y = chislo2

    def operacii(self, znak):

        if znak in komandy1:
            if znak == '+':
                return print(int(self.x + self.y))
            elif znak == '-':
                return print(int(self.x - self.y))
            elif znak == '*':
                return print(int(self.x * self.y))
            elif znak == '/':
                if self.y == 0:
                    return print("Ошибка: Деление на ноль!")
                else:
                    return print(float(self.x / self.y))
            elif znak == '^':
                return print(int(self.x ** self.y))

        elif znak in komandy2:
            if znak == "модуль":
                return print(int(math.fabs(self.x)))
            elif znak == '!':
                return print(int(math.factorial(self.x)))
            elif znak == "арккосинус":
                if -1 <= self.x <= 1:
                    return print(int(math.acos(self.x)))
                else:
                    return print("Ваше число не принадлежит промежутку от -1 до 1")
            elif znak == "рандом":
                return print(random.uniform(0, 10000))
            else:
                return print("Ошибка: Неверный знак операции!\n")


while True:
    print("Команда 0 завершит работу программы\n")
    znak = input("Введите знак/команду (-, +, *, /, ^, модуль, !, арккосинус, рандом): ")
    if znak == '0':
        break
    calc = Calc()
    if znak in komandy1:
        calc.numbers(float(input("x=")), float(input("y=")))
    elif znak in komandy2:
        calc.numbers(float(input("x=")))


Calc.numbers(znak)