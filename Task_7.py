import os.path
def fun_slova():
    return set(input("Введите слова через запятую (без пробелов): ").split(','))
def fun_kolvo(set):
    return len(set)
def fun_slovar(keys, values):
    return dict(zip(keys, values))
dic_keys = fun_slova()
print(fun_kolvo(dic_keys))
dic_values = fun_slova()
dictionary = fun_slovar(dic_keys, dic_values)


name = input("Введите название файла: ")
if os.path.exists(name): #os.path.exists(path) - возвращает True, если path указывает на существующий путь или дескриптор открытого файла
    file = open(name, "r")
    text = file.read()
    file.seek(0)
    file.truncate()
else:
    file = open(name, "w+") #w+:открывает файл для записи и создает если он не существует. Но если файл уже существует, то перезаписывает его
    text = ''
for key,val in dictionary.items():
    file.write('{}:{}\n'.format(key,val))
if text != '':
    file.write(text)
file.close()



