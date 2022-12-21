import random

def randomMaze():
    length = random.randrange(15, 45+1, 2)
    maze = [[[0 for i in range(length)] for j in range(length)] for k in range(length)]
    for i in range(length):
        for j in range(length):
            for k in range(length):
                maze[i][j][k] = random.randint(0,1)
    return maze

def printMaze(maze):
    for line in maze:
        print(*line)