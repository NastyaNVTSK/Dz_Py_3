def arithmeticProgression():
    a1 = int(input("Введите первый элемент: "))
    d = int(input("Введите разность: "))
    n = int(input("Введите количество элементов: "))

    progression = []
    for i in range(n):
        an = a1 + (i * d)
        progression.append(an)

    return progression


result = arithmeticProgression()
print("Массив элементов арифметической прогрессии:", result)