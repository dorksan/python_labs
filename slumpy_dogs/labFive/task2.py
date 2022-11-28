import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
from random import randint

def search_in_list(list, value):
    for i in range(len(list)):
        if list[i][0] == value:
            return i
    return -1

def create_list_of_data(list):
    list_of_data = []
    for i in range(len(list)):
        index = search_in_list(list_of_data, list[i])
        if index > -1:
            list_of_data[index][1] += 1
        else:
            list_of_data.append([list[i], 1])
    for i in range(len(list_of_data)):
        list_of_data[i][1] /= len(list)
    return list_of_data

print("Введите n")
n = int(input())
print("Введите минимальное значение")
min_rand = int(input())
print("Введите максимальное значение")
max_rand = int(input())
array = [0] * n
for i in range(n):
    array[i] = randint(min_rand, max_rand)
array.sort()
list = create_list_of_data(array)
print(list)
mathematical_expectation = 0
for i in range(len(list)):
    mathematical_expectation += list[i][0] * list[i][1]
print("Математическое ожидание =", mathematical_expectation)
mathematical_expectation_2 = 0
for i in range(len(list)):
    mathematical_expectation_2 += (list[i][0]) * (list[i][0]) * list[i][1]
variance = mathematical_expectation_2 - mathematical_expectation * mathematical_expectation
print("Дисперсия =", variance)
mean_square_deviation = variance ** 0.5
print("Среднеквадратическое отклонение =", mean_square_deviation)

sum_x = 0
for i in range(len(list)):
    sum_x += list[i][0]

sum_y = 0
for i in range(len(list)):
    sum_y += list[i][1]

sum_x_x = 0
for i in range(len(list)):
    sum_x_x += list[i][0] * list[i][0]

a = (len(list) * mathematical_expectation - sum_x * sum_y) / (len(list) * sum_x_x - sum_x * sum_x)
b = (sum_y - a * sum_x) / len(list)

min_number_x = min(array)
max_number_x = max(array)
x_len_list = []
y_len_list = []
for i in range(min_number_x, max_number_x + 1):
    x_len_list.append(i)
    y_len_list.append(a*i + b)

x_list =[]
for i in range(len(list)):
    x_list.append(list[i][0])

y_list =[]
for i in range(len(list)):
    y_list.append(list[i][1])

min_number_y = min(y_list)
max_number_y = max(y_list)

fig, ax = plt.subplots()
ax.scatter(x_list, y_list, label='Вероятность значения', s = 15)
ax.plot(x_len_list, y_len_list, label='Линейная функция', color='red')
ax.scatter([min_number_x, max_number_x],[min_number_y - min_number_y * 0.5, max_number_y + max_number_y * 0.5], color ='white')
ax.set_xlabel('Значение')
ax.set_ylabel('Вероятность')
ax.set_title("Линейная функция методом наименьших квадратов")
ax.legend();
plt.show()