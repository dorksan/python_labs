def matrixOutput(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for i in range(rows):
        print(matrix[i])

# принимает матрицу, возвращает матрицу
def transposeMatrix(matrix):
    rows = len(matrix[0])
    columns = len(matrix)
    matrixNew = []
    for i in range(rows):
        matrixNew.append([0]*columns)
    for i in range(rows):
        for j in range(columns):
            matrixNew[i][j] = matrix[j][i]
    return matrixNew

# принимает матрицу, возвращает матрицу (возвращает пустую матрицу в случае ошибки, число при умножении строки на столбец)
def multiplicateMatrix(matrixOne, matrixTwo):
    numOfRowsTwo = len(matrixTwo)
    numOfColumnsOne = len(matrixOne[0])

    if numOfColumnsOne != numOfRowsTwo:
        return []

    numOfRowsOne = len(matrixOne)
    numOfColumnsTwo = len(matrixTwo[0])

    if numOfRowsOne < 1 or numOfColumnsOne < 1 or numOfRowsTwo < 1 or numOfColumnsTwo < 1:
        return []

    if numOfRowsOne == 1 and numOfColumnsTwo == 1:
        returnValue = 0
        for i in range(numOfColumnsOne):
            returnValue += matrixOne[0][i] * matrixTwo[i][0]
        return  returnValue

    returnMatrix = []
    for i in range(numOfRowsOne):
        returnMatrix.append([0] * numOfColumnsTwo)
    for i in range(numOfRowsOne):
        for j in range(numOfColumnsTwo):
            returnMatrix[i][j] = 0
            for k in range(numOfColumnsOne):
                returnMatrix[i][j] += matrixOne[i][k] * matrixTwo[k][j]
    return returnMatrix

# принимает матрицу, возвращает число( -1 в случае ошибки)
def determineRankOfMatrix(matrix):
    numOfRows = len(matrix)
    numOfColumns = len(matrix[0])

    if numOfColumns != numOfRows or numOfRows > 3 or numOfColumns < 2:
        return -1

    if numOfRows == 2:
        if matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] != 0:
            return 2
        for i in range(2):
            for j in range(2):
                if matrix[i][j] != 0:
                    return 1

        return 0

    if matrix[0][0] * matrix[1][1] * matrix[2][2] \
    + matrix[0][1] * matrix[1][2] * matrix[2][0] \
    + matrix[0][2] * matrix[2][1] * matrix[1][0] \
    - matrix[0][2] * matrix[1][1] * matrix[2][0] \
    - matrix[0][1] * matrix[2][2] * matrix[1][0] \
    - matrix[0][0] * matrix[1][2] * matrix[2][1] != 0:
        return 3

    if matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1] != 0 or \
    matrix[0][1] * matrix[2][2] - matrix[0][2] * matrix[2][1] != 0 or \
    matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1] != 0 or \
    matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0] != 0 or \
    matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0] != 0 or \
    matrix[0][0] * matrix[1][2] - matrix[0][2] * matrix[1][0] != 0 or \
    matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0] != 0 or \
    matrix[0][0] * matrix[2][1] - matrix[0][1] * matrix[2][0] != 0 or \
    matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0] != 0:
        return 2

    for i in range(numOfRows):
        for j in range(numOfColumns):
            if matrix[i][j] != 0:
                return 1
            
    return 0