import numpy as np
def isInt(string):
      try:
            newString = int(string)
            return True
      except ValueError:
            return False

def matrixInput():
    print('\n-------------ВВОД РАЗМЕРА МАТРИЦЫ-------------\n')
    print('Введите число строк:')
    while True:
        rows = input()
        if not (isInt(rows)):
            print("Ошибка ввода, попробуйте еще раз")
        else:
            rows = int(rows)
            if rows < 1:
                print("Ошибка ввода, попробуйте еще раз")
            else:
                break
    print('Введите число столбцов:')
    while True:
        columns = input()
        if not (isInt(columns)):
            print("Ошибка ввода, попробуйте еще раз")
        else:
            columns = int(columns)
            if columns < 1:
                print("Ошибка ввода, попробуйте еще раз")
            else:
                break
    matrix = []
    for i in range(rows):
        matrix.append([0] * columns)
    print('Введите все числа матрицы через ENTER:')
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = int(input())
    return matrix

print("0 - выход из программы")
print("1 - транспонирование")
print("2 - умножение")
print("3 - нахождение ранга")
operations = (0, 1, 2, 3)
IsNotExit = True
while IsNotExit:
    while True:
        print("\nВведите номер необходимой команды: ")
        operator = input()
        if isInt(operator):
            chooseYourCommand = int(operator)
            if chooseYourCommand in operations:
                break
        print("Неправильный ввод команды")
    match chooseYourCommand:
        case 0:
            IsNotExit = False
            print("\nВы вышли из программы")
        case 1:
            matrixOne = matrixInput()
            transposedMatrix = np.transpose(matrixOne)
            print('\nТранспонированная матрица:\n', transposedMatrix)
        case 2:
            print('Введите первую матрицу:\n')
            matrixOne = matrixInput()
            print('Введите вторую матрицу:\n')
            matrixTwo = matrixInput()
            multiplicatedMatrix = np.dot(matrixOne, matrixTwo)
            print('\nРезультат умножения:\n', multiplicatedMatrix)
        case 3:
            matrixOne = matrixInput()
            rank = np.linalg.matrix_rank(matrixOne)
            print('\nРанг матрицы:', rank)