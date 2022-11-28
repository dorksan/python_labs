import matplotlib.pyplot as plt
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


visa_list = []
with open('Visa.txt') as file:
    while (line := file.readline().rstrip()):
        line = line[12:17]
        line = line.replace(',', '.')
        visa_list.append(float(line))

mastercard_list = []
with open('MasterCard.txt') as file:
    while (line := file.readline().rstrip()):
        line = line[12:17]
        line = line.replace(',', '.')
        mastercard_list.append(float(line))

print('Visa', visa_list)
print('MasterCard', mastercard_list)
print('-' * len(visa_list) * 7)

visa_list_probability = create_list_of_data(visa_list)
mastercard_list_probability = create_list_of_data(mastercard_list)

print('Visa',visa_list_probability)
print('MasterCard',mastercard_list_probability)
print('-' * len(visa_list) * 16)
mathematical_expectation_mastercard = 0
mathematical_expectation_visa = 0
for i in range(len(visa_list_probability)):
    mathematical_expectation_visa += visa_list_probability[i][0] * visa_list_probability[i][1]
    mathematical_expectation_mastercard += mastercard_list_probability[i][0] * mastercard_list_probability[i][1]
print("Математическое ожидание visa =", mathematical_expectation_visa)
print("Математическое ожидание mastercard =", mathematical_expectation_mastercard)

a = 0
b = 0
c = 0
for i in range(len(visa_list)):
    a += (visa_list[i] - mathematical_expectation_visa) * (mastercard_list[i] - mathematical_expectation_mastercard)
    b += (visa_list[i] - mathematical_expectation_visa) * (visa_list[i] - mathematical_expectation_visa)
    c += (mastercard_list[i] - mathematical_expectation_mastercard) * (mastercard_list[i] - mathematical_expectation_mastercard)
r = a/((b*c)**0.5)
print('Коэффицент корреляции Пирсона =', r)
print('-' * len(visa_list) * 7)
visa_list_one = []
mastercard_list_one = []

for i in range(len(visa_list)):
    visa_list_one.append(visa_list[i])
    mastercard_list_one.append(mastercard_list[i])

for i in range(247):
    index = randint(0, len(visa_list_one) - 1)
    if visa_list_one[index] != []:
        visa_list_one[index] = []
    if mastercard_list_one[index] != []:
        mastercard_list_one[index] = []

visa_list_two = []
visa_list_three = []
mastercard_list_two = []
mastercard_list_three = []
for i in range(len(visa_list)):
    visa_list_two.append(visa_list_one[i])
    visa_list_three.append(visa_list_one[i])
    mastercard_list_two.append(mastercard_list_one[i])
    mastercard_list_three.append(mastercard_list_one[i])

print('Visa', visa_list_one)
print('MasterCard', mastercard_list_one)
print('-' * len(visa_list) * 7)

def vinzoring(list):
    for i in range(len(list)):
        if list[i] == []:
            index = -1
            index_next = i
            index_priveous = i
            while True:
                index_next += 1
                index_priveous -= 1
                if index_next < len(list) and list[index_next] != []:
                    index = index_next
                    break
                if index_priveous >= 0 and list[index_priveous] != []:
                    index = index_priveous
                    break
            list[i] = list[index]

vinzoring(visa_list_one)
vinzoring(mastercard_list_one)
print('Винзорирование')
print('Visa', visa_list_one)
print('MasterCard', mastercard_list_one)
print('-' * len(visa_list) * 7)

def linear_approximation(list):
    for i in range(len(list)):
        if list[i] == []:
            index_next = i
            index_priveous = i
            while True:
                index_next += 1
                if index_next >= len(list) or list[index_next] != []:
                    break
            while True:
                index_priveous -= 1
                if index_priveous < 0 or list[index_priveous] != []:
                    break
            if index_next >= len(list):
                index_next = index_priveous - 1
                while True:
                    if index_next >= 0 and list[index_next] != []:
                        break
                    index_next -= 1

            if index_priveous < 0:
                index_priveous = index_next + 1
                while True:
                    if index_priveous < len(list) and list[index_priveous] != []:
                        break
                    index_priveous += 1
            if list[index_priveous] == list[index_next]:
                list[i] = list[index_next]
            else:
                a = (index_priveous - index_next) / (list[index_priveous] - list[index_next])
                b = index_next - a * list[index_next]
                list[i] = (i - b)/a

linear_approximation(visa_list_two)
linear_approximation(mastercard_list_two)
print('Линейная аппроксимация')
print('Visa', visa_list_two)
print('MasterCard', mastercard_list_two)
print('-' * len(visa_list) * 7)

def correlation_recovery(list_one, list_two):
    for i in range(len(list_one)):
        if list_one[i] == []:
            index = -1
            index_next = i
            index_priveous = i
            while True:
                index_next += 1
                index_priveous -= 1
                if index_next < len(list_one) and list_one[index_next] != []:
                    index = index_next
                    break
                if index_priveous >= 0 and list_one[index_priveous] != []:
                    index = index_priveous
                    break
            list_one[i] = (list_two[i]/list_two[index])*list_one[index]




correlation_recovery(visa_list_three, mastercard_list)
correlation_recovery(mastercard_list_three, visa_list)
print('корреляционное восстановление')
print('Visa', visa_list_three)
print('MasterCard', mastercard_list_three)
print('-' * len(visa_list) * 7)


fig, ax = plt.subplots(4,2)
ax[0,0].set_title("Обычный набор данных Visa")
ax[0,0].plot(visa_list, color = 'green')
ax[1,0].set_title("Винзорирование")#Visa
ax[1,0].plot(visa_list_one)
ax[1,0].plot(visa_list, color = 'green')
ax[0,1].set_title("Обычный набор данных MasterCard")
ax[0,1].plot(mastercard_list, color = 'red')
ax[1,1].set_title("Винзорирование")#MasterCard
ax[1,1].plot(mastercard_list_one)
ax[1,1].plot(mastercard_list, color = 'red')
ax[2,0].set_title("Линейная аппроксимация")#Visa
ax[2,0].plot(visa_list_two)
ax[2,0].plot(visa_list, color = 'green')
ax[2,1].set_title("Линейная аппроксимация")#MasterCard
ax[2,1].plot(mastercard_list_two)
ax[2,1].plot(mastercard_list, color = 'red')
ax[3,0].set_title("Корреляционное восстановление")#Visa
ax[3,0].plot(visa_list_three)
ax[3,0].plot(visa_list, color = 'green')
ax[3,1].set_title("Корреляционное восстановление")#MasterCard
ax[3,1].plot(mastercard_list_three)
ax[3,1].plot(mastercard_list, color = 'red')
for ax in ax.flat:
    ax.label_outer()
plt.show()