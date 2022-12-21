import seaborn as sns
import matplotlib.pyplot as plt

import maze2D as m2D
import maze3D as m3D
import generateMaze2D as genMaze2D
import generateMaze3D as genMaze3D

def IsNotString(string):
    try:
        newString = int(string)
        return True
    except ValueError:
        return False

print("0 - выход из программы")
print("1 - тестовый 2D лабиринт")
print("2 - тестовый 3D лабиринт")
print("3 - случайный 2D лабиринт")
print("4 - случайный 3D лабиринт")
operations = (0, 1, 2, 3, 4)
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
            m2D.testMaze2D()
        case 2:
            m3D.testMaze3D()
        case 3:
            maze = genMaze2D.randomMaze()
            genMaze2D.printMaze(maze)
            m2D.maze2D(maze)
        case 4:
            maze = genMaze3D.randomMaze()
            genMaze3D.printMaze(maze)
            m3D.maze3D(maze)
