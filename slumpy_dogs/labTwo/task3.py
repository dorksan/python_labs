import numpy as np
import timeit

def matrixOutput(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        print(matrix[i])

# принимает матрицу, возвращает матрицу(пустую, в случае ошибки)
def findInverseMatrix(matrix):
    numOfRows = len(matrix)
    numOfColumns = len(matrix[0])

    if numOfColumns != 3 and numOfRows != 3:
        return []

    matrixDeterminator = matrix[0][0] * matrix[1][1] * matrix[2][2] \
    + matrix[0][1] * matrix[1][2] * matrix[2][0] \
    + matrix[0][2] * matrix[2][1] * matrix[1][0] \
    - matrix[0][2] * matrix[1][1] * matrix[2][0] \
    - matrix[0][1] * matrix[2][2] * matrix[1][0] \
    - matrix[0][0] * matrix[1][2] * matrix[2][1]
    if matrixDeterminator == 0:
        return []

    returnMatrix = []
    for i in range(3):
        returnMatrix.append([0] * 3)

    returnMatrix[0][0] = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]
    returnMatrix[0][1] = -1 * (matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1])
    returnMatrix[0][2] =  matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
    returnMatrix[1][0] = -1 * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
    returnMatrix[1][1] = matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]
    returnMatrix[1][2] = -1 * (matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0])
    returnMatrix[2][0] =  matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]
    returnMatrix[2][1] = -1 * (matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0])
    returnMatrix[2][2] = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    intermediateValue = 1 / matrixDeterminator
    for i in range(3):
        for j in range(3):
            returnMatrix[i][j] *= intermediateValue

    return returnMatrix

def IsNotString(string):
    try:
        newString = int(string)
        return True
    except ValueError:
        return False


print("0 - выход из программы")
print("1 - нахождение обратной матрицы")
print("2 - тайм тест")
operations = (0, 1, 2)
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
            print("\nВы вышли из программы")
        case 1:
            a = [[4, 3, 2], [2, 1, -1], [3, 3, 2]]
            b = findInverseMatrix(a)
            matrixOutput(b)
        case 2:
            matrix = [[4, 3, 2], [2, 1, -1], [3, 3, 2]]

            startTime = timeit.default_timer()
            np.linalg.inv(matrix)
            endTimeNumpy = timeit.default_timer() - startTime

            startTime = timeit.default_timer()
            findInverseMatrix(matrix)
            endTime = timeit.default_timer() - startTime

            print("Время нахождения обратной матрицы с помощью собственной функции:")
            print(endTime)
            print("Время нахождения обратной матрицы с помощью функции библиотеки numpy:")
            print(endTimeNumpy)