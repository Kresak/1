a = 0
string = input("Введите строку: ")
print("Длина строки: ", len(string))
for letter in string:
    a += 1
    # пропускаем третий символ/не выводим последний символ в строке
    if (a == 3 or letter == string[-1]):
        continue
    if letter == 'с':
        print("В строке есть буква С ")
    print(letter)