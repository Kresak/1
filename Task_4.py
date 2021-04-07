imena_ovoshchei = []
kolvo_ovoshchei = []

for count in range(0, 3):
    word = input("Введите имена овощей: ")
    imena_ovoshchei.append(word)


for str in imena_ovoshchei:
    print(str.lower())
for str in imena_ovoshchei:
    print(str.upper())
for str in imena_ovoshchei:
    print(str.title())


for count in range(0, len(imena_ovoshchei)):
    amount = int(input("Введите количество овощей: "))
    kolvo_ovoshchei.append(amount)
for count in range(0, len(imena_ovoshchei)):
    print("В ящике лежит {amount} {title}.".format(title=imena_ovoshchei[count], amount = kolvo_ovoshchei[count]))