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

# принимает матрицу, возвращает число
def determineRankOfMatrix(matrix):