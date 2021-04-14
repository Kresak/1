klyuchi = set(input("Введите слова через запятую (без пробелов): ").split(',')) # set - множество
# Метод Split() в Python возвращает список слов в строке/строке, разделенных строкой разделителя

kolvo = len(klyuchi) # len( ) возвращает целое число (int), равное количеству элементов объекта
print("Количество слов в списке: ", kolvo)

znacheniya = set(input("Введите второй список слов с таким же количеством: ").split(','))
if len(klyuchi)==len(znacheniya):
    slovar = dict(zip(klyuchi, znacheniya)) # создаём словарь из двух массивов
    print(slovar)
else:
    print("Ошибка: Ошибка!")