import numpy as np

matrixOne = [[1, 2, 3], [4, 5, 6]]
transposedMatrix = np.transpose(matrixOne)
print('Транспонированная матрица:\n', transposedMatrix)

matrixTwo = [[6, 5], [1, 8], [7, 5]]
multiplicatedMatrix = np.dot(matrixOne, matrixTwo)
print('Результат умножения:\n', multiplicatedMatrix)

rank = np.linalg.matrix_rank(matrixOne)
print('Ранг матрицы:', rank)