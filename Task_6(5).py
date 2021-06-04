def f_spisok():
    return set(input("Введите слова через запятую (без пробелов): ").split(',')) # set - множество


def f_kolvo(set):
    return len(set)


def f_slovar(keys, values):
    return dict(zip(keys, values)) # функция zip позволяет пройтись одновременно по нескольким итерируемым объектам (спискам и др.)


keys = f_spisok()
print(f_kolvo(keys))
values = f_spisok()


if len(keys) == len(values):
    slovar = f_slovar(keys, values)  # создаём словарь из двух массивов
    print(slovar)
else:
    print("Ошибка: Количество слов в списках не совпадает!")
