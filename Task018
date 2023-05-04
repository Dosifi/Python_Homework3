# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X

n = int(input("Введите количество элементов: "))
new_list = []
for i in range(n):
    new_list.append(i + 1)
x = int(input("Введите число которое необходимо найти: "))
i = new_list[0]
for index in range(len(new_list) - 1):
    if new_list[index] == x:
        i == new_list[index]
    elif new_list[index - 1] == x:
        i = new_list[index - 1]
    elif new_list[index + 1] <= x:
        i = new_list[index + 1]
print(f'Ближайшее число - {i}')