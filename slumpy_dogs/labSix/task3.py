import seaborn as sns
import matplotlib.pyplot as plt

import maze2D as m2D
import maze3D as m3D
import generateMaze2D as genMaze

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
            maze = m2D.testMaze()
        case 2:

        case 3:
            maze = genMaze.randomMaze()
        case 4:
