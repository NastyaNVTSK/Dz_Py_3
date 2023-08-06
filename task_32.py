import random

def find_indexes(list, minVal, maxVal):
    indexes = []
    for i in range(len(list)):
        if minVal <= list[i] <= maxVal:
            indexes.append(i)
    return indexes

lst = [random.randint(0, 500) for _ in range(10)]

minVal = 33
maxVal = 200

indexes = find_indexes(lst, minVal, maxVal)

print("Список:", lst)
print("Минимум:", minVal)
print("Максимум:", maxVal)
print("Индексы элементов в диапазоне:", indexes)