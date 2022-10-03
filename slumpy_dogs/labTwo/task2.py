import numpy as np
def IsNotString(string):
      try:
            newString = int(string)
            return True
      except ValueError:
            return False

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
            matrixOne = [[1, 2, 3], [4, 5, 6]]
            transposedMatrix = np.transpose(matrixOne)
            print('Транспонированная матрица:\n', transposedMatrix)
        case 2:
            matrixTwo = [[6, 5], [1, 8], [7, 5]]
            multiplicatedMatrix = np.dot(matrixOne, matrixTwo)
            print('Результат умножения:\n', multiplicatedMatrix)
        case 3:
            rank = np.linalg.matrix_rank(matrixOne)
            print('Ранг матрицы:', rank)