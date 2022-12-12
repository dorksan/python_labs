import random

def randomMaze():
    length = random.randrange(15, 45+1, 2)
    maze = [[1 for i in range(length)] for j in range(length)]
    for i in range(length):
        for j in range(length):
            if (i % 2 > 0) & (j % 2 > 0):
                maze[i][j] = 0
    return maze

# def printMaze(maze):
#     maze = randomMaze()
#     for line in maze:
#         print(*line)
maze = randomMaze()
for line in maze:
    print(*line)