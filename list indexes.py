# проверка элементов по индексу

numbers = [0, 1, 2, 3, 4, 5]

for x in numbers:
    if x == numbers[0]:
        print(f"{x} - Первый элемент.")
    if x == numbers[-1]:
        print(f"{x} - Последний элемент.")
    else:
        print(f"{x} - Промежуточный элемент.")
