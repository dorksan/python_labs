import math

def IsInt(number):
    if number % 1 != 0:
        return number
    return int(number)

def IsNotString(string):
        try:
            newString = int(string)
            return True
        except ValueError:
            return False

def IsFloat():
    while True:
        string = input()
        try:
            newString = float(string)
            return newString
        except ValueError:
            print(string, "не является числом, попробуйте еще раз")

def Addition(summand, addend):
    result = summand + addend
    return IsInt(result)

def Subtraction(minuend, subtrahend):
    result = minuend - subtrahend
    return IsInt(result)

def Multiplication(multiplicand, multiplier):
    result = multiplicand * multiplier
    return IsInt(result)

def Division(dividend, divisor):
    result = dividend / divisor
    return IsInt(result)

def Increase(number, power):
    result = number ** power
    return IsInt(result)

def Logarithm(number, base):
    result = math.log(number, base)
    return IsInt(result)

def RoundingUp(number, n):
    if n == 0:
        number += 0.5
    else:
        number += 0.5 * (0.1 ** n)
    result = round(number, n)
    return IsInt(result)

def RoundingDown(number, n):
    if n == 0:
        number -= 0.5
    else:
        number -= 0.5 * (0.1 ** n)
    result = round(number, n)
    return IsInt(result)

print("0 - выход из программы")
print("1 - сложение")
print("2 - вычитание")
print("3 - умножение")
print("4 - деление")
print("5 - возведение в степень")
print("6 - логарифм")
print("7 - округление в большую сторону до N знака после запятой ")
print("8 - округление в меньшую сторону до N знака после запятой")
operations = (0, 1, 2, 3, 4, 5, 6, 7, 8)
IsNotExit = True
while IsNotExit:
    while True:
        print("\nВведите номер необходимой команды: ")
        operator = input()
        if IsNotString(operator):
            chooseYourCommand = int(operator)
            if chooseYourCommand in operations:
                break
        print("Неправильный ввод команды")
    match chooseYourCommand:
        case 0:
            IsNotExit = False
            print("\nВы вышли из калькулятора")
        case 1:
            print("\nВведите первое слагаемое: ")
            summand = IsFloat()
            print("Введите второе слагаемое: ")
            addend = IsFloat()
            print("Результат:", Addition(summand, addend))
        case 2:
            print("\nВведите уменьшаемое: ")
            minuend = IsFloat()
            print("Введите вычитаемое: ")
            subtrahend = IsFloat()
            print("Результат:", Subtraction(minuend, subtrahend))
        case 3:
            print("\nВведите умножаемое: ")
            multiplicand = IsFloat()
            print("Введите множитель: ")
            multiplier = IsFloat()
            print("Результат:", Multiplication(multiplicand, multiplier))
        case 4:
            print("\nВведите делимое: ")
            dividend = IsFloat()
            print("Введите делитель: ")
            divisor = 0
            while divisor == 0:
                divisor = IsFloat()
                if divisor == 0:
                    print("Пожалуйста, введите другое число")
                else:
                    print("Результат:", Division(dividend, divisor))
        case 5:
            print("\nВведите число: ")
            number = IsFloat()
            print("Введите степень: ")
            power = IsFloat()
            print("Результат:", Increase(number, power))
        case 6:
            IsWrongBase = True
            IsWrongNumber = True
            while IsWrongNumber:
                print("\nВведите число: ")
                number = IsFloat()
                if number <= 0:
                    print("\nВведите число больше нуля")
                else:
                    IsWrongNumber = False
            while IsWrongBase:
                print("Введите основание: ")
                base = IsFloat()
                if (base == 1) | (base <= 0):
                    print("Неверное основание, попробуйте еще раз")
                else:
                    print("Результат:", Logarithm(number, base))
                    IsWrongBase = False
        case 7:
            print("\nВведите число: ")
            number = IsFloat()
            print("Введите номер знака N после запятой: ")
            temp = True
            while temp:
                n = IsInt(IsFloat())
                if (type(n) != int) | (n < 0):
                    print("Введите целое положительное N ")
                else:
                    temp = False
            print("Результат:", RoundingUp(number, n))
        case 8:
            print("\nВведите число: ")
            number = IsFloat()
            print("Введите номер знака N после запятой: ")
            temp = True
            while temp:
                n = IsInt(IsFloat())
                if (type(n) != int) | (n < 0):
                    print("Введите целое положительное N ")
                else:
                    temp = False
            print("Результат:", RoundingDown(number, n))