# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

size = int(input("Введите количество элементов в массиве: "))
start_list = [] * size
numbers = 0

while numbers < size:
    start_list.append(int(input(f"Введите {numbers + 1} элемент массива: ")))
    numbers += 1

x = int(input("Введите искомый элемент Х: "))
count = 0
for i in range(len(start_list)):
    if start_list[i] == x:
        count += 1

print(start_list)
print(f"{x} -> {count}")