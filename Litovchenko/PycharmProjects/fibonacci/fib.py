print("Введите число: ")
number = int(input())
d = True
c = 1
a = 1
b = 1
for i in range(2, number):
    if (number % i == 0):
        print(number, 'не является простым числом')
        d = False
        break
while (c < number):
    b = c
    c += a
    a = b
if c == number:
    print(number, 'является числом Фибоначчи')
else:
    print(number, 'не является числом Фибоначчи')
if d and number != 1:
    print(number, 'является простым числом')