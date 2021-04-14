def fun_slova():
    return set(input("Введите слова через запятую (без пробелов): ").split(',')) # set - множество
def fun_kolvo(set):
    return len(set)
def fun_slovar(keys, values):
    return slovar(zip(keys, values)) # функция zip позволяет пройтись одновременно по нескольким итерируемым объектам (спискам и др.)

klyuchi = fun_slova()
print(fun_kolvo(klyuchi))
znacheniya = fun_slova()

if len(klyuchi) == len(znacheniya):
    slovar = dict(zip(klyuchi, znacheniya)) # создаём словарь из двух массивов
    print(slovar)
else:
    print("Ошибка: Ошибка!")
