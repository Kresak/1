imena = []
kolvo = []

for count in range(0, 3): #range() позволяет генерировать ряд чисел в рамках заданного диапазона
    a = input("Введите имена овощей: ")
    imena.append(a)
for str in imena: #нижний регистр
    print(str.lower())
for str in imena: #капс
    print(str.upper())
for str in imena: #слово с большой буквы
    print(str.title())
for count in range(0, len(imena)): #функция len( ) возвращает целое число (int), равное количеству элементов объекта
    b = int(input("Введите количество овощей: "))
    kolvo.append(b)
for count in range(0, len(imena)):
    print("В ящике лежит {b} {title}".format(title=imena[count], b = kolvo[count]))