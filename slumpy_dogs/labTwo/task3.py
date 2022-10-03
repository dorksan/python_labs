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