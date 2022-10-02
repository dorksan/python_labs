# принимает матрицу, возвращает матрицу
def matrixTranspose(matrix):
    rows = len(matrix[0])
    columns = len(matrix)
    matrixNew = []
    for i in range(rows):
        matrixNew.append([0]*columns)
    for i in range(rows):
        for j in range(columns):
            matrixNew[i][j] = matrix[j][i]
    return matrixNew

m = [[1, 2, 3], [4, 5, 6]]
n = matrixTranspose(m)
print(n)

# принимает матрицу, возвращает матрицу
def matrixMultiplicate(matrixOne, matrixTwo):

# принимает матрицу, возвращает число
def determineRankOfMatrix(matrix):