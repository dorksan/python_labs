import sort
import timeit
import random

print("Введите размер массива:")
n = int(input())
array = [0] * n
print("Заполните массив:")
for i in range(n):
    array[i] = int(input())

print("1 - быстрая сортировка")
print("2 - сортировка расчёской")

mod = int(input())
if mod == 1:
    startTimeQsort = timeit.default_timer()
    sort.qsort(array, 0, len(array) - 1)
    endTimeQsort = timeit.default_timer() - startTimeQsort
    print('Qsort')
    print('Отсортированный массив:\n', array)
    print('Время выполнения:', endTimeQsort)
if mod == 2:
    startTimeCombsort = timeit.default_timer()
    sort.combSort(array)
    endTimeCombsort = timeit.default_timer() - startTimeCombsort
    print('\nComb sort')
    print('Отсортированный массив:\n', array)
    print('Время выполнения:', endTimeCombsort)
