import math

def inputFloat():
    while True:
        inputString = input()
        try:
            valueOne = float(inputString)
            return valueOne
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз:")

def inputInt():
    while True:
        inputString = input()
        try:
            valueOne = int(inputString)
            return valueOne
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз:")

def inputFloatDivider():
    while True:
        inputString = input()
        try:
            valueOne = float(inputString)
            if valueOne == 0:
                print("Некорректный ввод, попробуйте ещё раз:")
                continue
            return valueOne
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз:")

def inputFloatBaseOfLogarithm():
    while True:
        inputString = input()
        try:
            valueOne = float(inputString)
            if valueOne == 1 or valueOne <= 0:
                print("Некорректный ввод, попробуйте ещё раз:")
                continue
            return valueOne
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз:")

def inputFloatArgumentOfLogarithm():
    while True:
        inputString = input()
        try:
            valueOne = float(inputString)
            if valueOne <= 0:
                print("Некорректный ввод, попробуйте ещё раз:")
                continue
            return valueOne
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз:")

def inputIntNatural():
    while True:
        inputString = input()
        try:
            valueOne = int(inputString)
            if valueOne < 0:
                print("Некорректный ввод, попробуйте ещё раз:")
                continue
            return valueOne
        except ValueError:
            print("Некорректный ввод, попробуйте ещё раз:")

def printBeginning():
    print("Введите номер необходимой функции:")
    print("Сложение - 1")
    print("Вычитание - 2")
    print("Умножение - 3")
    print("Деление - 4")
    print("Возведение в степень - 5")
    print("Логарифм - 6")
    print("Округление в большую сторону до N знака после запятой - 7")
    print("Округление в меньшую сторону до N знака после запятой - 8")

printBeginning()
operations = (1, 2, 3, 4, 5, 6, 7, 8)
while True:
    operationNumber = inputInt()
    if operationNumber in operations:
        break
    print("Некорректный ввод, попробуйте ещё раз:")

match operationNumber:
    case 1:
        print("Введите первое слагаемое:")
        valueOne = inputFloat()
        print("Введите второе слагаемое:")
        valueTwo = inputFloat()
        result = valueOne + valueTwo
    case 2:
        print("Введите уменьшаемое:")
        valueOne = inputFloat()
        print("Введите вычитаемое:")
        valueTwo = inputFloat()
        result = valueOne - valueTwo
    case 3:
        print("Введите первый множитель:")
        valueOne = inputFloat()
        print("Введите второй множитель:")
        valueTwo = inputFloat()
        result = valueOne * valueTwo
    case 4:
        print("Введите делимое:")
        valueOne = inputFloat()
        print("Введите делитель:")
        valueTwo = inputFloatDivider()
        result = valueOne / valueTwo
    case 5:
        print("Введите основание:")
        valueOne = inputFloat()
        print("Введите степень:")
        valueTwo = inputFloat()
        result = valueOne ** valueTwo
    case 6:
        print("Введите основание:")
        valueOne = inputFloatBaseOfLogarithm()
        print("Введите аргумент:")
        valueTwo = inputFloatArgumentOfLogarithm()
        result = math.log(valueTwo, valueOne)
    case 7:
        print("Введите значение:")
        valueOne = inputFloat()
        print("Введите количество знаков после запятой:")
        valueTwo = inputIntNatural()
        if valueTwo == 0:
            valueOne += 0.5
        else:
            valueOne += 0.5*(0.1**valueTwo)
        result = round(valueOne, valueTwo)
    case 8:
        print("Введите значение:")
        valueOne = inputFloat()
        print("Введите количество знаков после запятой:")
        valueTwo = inputIntNatural()
        if valueTwo == 0:
            valueOne -= 0.5
        else:
            valueOne -= 0.5*(0.1**valueTwo)
        result = round(valueOne, valueTwo)
print(result)
input("Нажмите, чтобы продолжить...")