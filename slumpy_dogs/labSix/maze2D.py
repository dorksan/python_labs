import seaborn as sns
import matplotlib.pyplot as plt

def testMaze2D():
    def testMaze():
        maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
        return maze
    maze = testMaze()
    start = 7, 0
    end = 7, 14
    length = len(maze)
    steps = [[0 for i in range(length)] for j in range(length)]
    i, j = start
    steps[i][j] = 1

    def makeStep(k):
      for i in range(length):
        for j in range(length):
          if steps[i][j] == k:
            if i > 0 and steps[i-1][j] == 0 and maze[i-1][j] == 0:
              steps[i-1][j] = k + 1
            if j > 0 and steps[i][j-1] == 0 and maze[i][j-1] == 0:
              steps[i][j-1] = k + 1
            if i < len(steps)-1 and steps[i+1][j] == 0 and maze[i+1][j] == 0:
                steps[i+1][j] = k + 1
            if j < len(steps[i])-1 and steps[i][j+1] == 0 and maze[i][j+1] == 0:
               steps[i][j+1] = k + 1

    def outputWayToExit(path):
        wayToExit = [[1]*length for i in range(length)]
        for i in range(len(path)):
            a, b = path[i]
            wayToExit[a][b] = 0
        return wayToExit

    k = 0
    while steps[end[0]][end[1]] == 0:
        k += 1
        makeStep(k)

    i, j = end
    k = steps[i][j]
    path = [(i, j)]
    while k > 1:
      if i > 0 and steps[i - 1][j] == k-1:
        i, j = i-1, j
        path.append((i, j))
        k -= 1
      elif j > 0 and steps[i][j - 1] == k-1:
        i, j = i, j-1
        path.append((i, j))
        k -= 1
      elif i < len(steps) - 1 and steps[i + 1][j] == k-1:
        i, j = i+1, j
        path.append((i, j))
        k -= 1
      elif j < len(steps[i]) - 1 and steps[i][j + 1] == k-1:
        i, j = i, j+1
        path.append((i, j))
        k -= 1

    data = outputWayToExit(path)
    ax = sns.heatmap(maze, annot=True, fmt="d", cbar=None, xticklabels=False, yticklabels=False, cmap="Greens_r", vmin=-0.3, vmax=1.3)
    plt.title("Лабиринт", fontsize=18)
    plt.savefig("visualize_maze.png", bbox_inches='tight', dpi=100)
    plt.show()
    ax = sns.heatmap(data, annot=True, fmt="d", cbar=None, xticklabels=False, yticklabels=False, cmap="Greens_r", vmin=0, vmax=1.3)
    plt.title("Выход", fontsize=18)
    plt.savefig("visualize_way_to_exit.png", bbox_inches='tight', dpi=100)
    plt.show()

    def testMaze2D():
        def testMaze():
            maze = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 1, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                    [1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1],
                    [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
                    [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
                    [1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1],
                    [1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1],
                    [1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                    [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                    [1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                    [1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
            return maze

        maze = testMaze()
        start = 7, 0
        end = 7, 14
        length = len(maze)
        steps = [[0 for i in range(length)] for j in range(length)]
        i, j = start
        steps[i][j] = 1

        def makeStep(k):
            for i in range(length):
                for j in range(length):
                    if steps[i][j] == k:
                        if i > 0 and steps[i - 1][j] == 0 and maze[i - 1][j] == 0:
                            steps[i - 1][j] = k + 1
                        if j > 0 and steps[i][j - 1] == 0 and maze[i][j - 1] == 0:
                            steps[i][j - 1] = k + 1
                        if i < len(steps) - 1 and steps[i + 1][j] == 0 and maze[i + 1][j] == 0:
                            steps[i + 1][j] = k + 1
                        if j < len(steps[i]) - 1 and steps[i][j + 1] == 0 and maze[i][j + 1] == 0:
                            steps[i][j + 1] = k + 1

        def outputWayToExit(path):
            wayToExit = [[1] * length for i in range(length)]
            for i in range(len(path)):
                a, b = path[i]
                wayToExit[a][b] = 0
            return wayToExit

        k = 0
        while steps[end[0]][end[1]] == 0:
            k += 1
            makeStep(k)

        i, j = end
        k = steps[i][j]
        path = [(i, j)]
        while k > 1:
            if i > 0 and steps[i - 1][j] == k - 1:
                i, j = i - 1, j
                path.append((i, j))
                k -= 1
            elif j > 0 and steps[i][j - 1] == k - 1:
                i, j = i, j - 1
                path.append((i, j))
                k -= 1
            elif i < len(steps) - 1 and steps[i + 1][j] == k - 1:
                i, j = i + 1, j
                path.append((i, j))
                k -= 1
            elif j < len(steps[i]) - 1 and steps[i][j + 1] == k - 1:
                i, j = i, j + 1
                path.append((i, j))
                k -= 1

        data = outputWayToExit(path)
        ax = sns.heatmap(maze, annot=True, fmt="d", cbar=None, xticklabels=False, yticklabels=False, cmap="Greens_r",
                         vmin=-0.3, vmax=1.3)
        plt.title("Лабиринт", fontsize=18)
        plt.savefig("visualize_maze.png", bbox_inches='tight', dpi=100)
        plt.show()
        ax = sns.heatmap(data, annot=True, fmt="d", cbar=None, xticklabels=False, yticklabels=False, cmap="Greens_r",
                         vmin=0, vmax=1.3)
        plt.title("Выход", fontsize=18)
        plt.savefig("visualize_way_to_exit.png", bbox_inches='tight', dpi=100)
        plt.show()
def maze2D(maze):
    start = -1, -1
    end = -1, -1
    for i in range(len(maze[0])):
        if maze[i][0] == 0:
            start = i, 0
            break
    i, j = start
    if i == -1:
        print("Нет входа")
        return

    for i in range(len(maze[0])):
        if maze[i][len(maze[0]) - 1] == 0:
            end = i, len(maze[0]) - 1
            break

    i, j = end
    if i == -1:
        print("Нет выхода")
        return


    length = len(maze)
    steps = [[0 for i in range(length)] for j in range(length)]
    i, j = start
    steps[i][j] = 1

    def makeStep(k):
      check = 0
      for i in range(length):
        for j in range(length):
          if steps[i][j] == k:
            check = 1
            if i > 0 and steps[i-1][j] == 0 and maze[i-1][j] == 0:
              steps[i-1][j] = k + 1
            if j > 0 and steps[i][j-1] == 0 and maze[i][j-1] == 0:
              steps[i][j-1] = k + 1
            if i < len(steps)-1 and steps[i+1][j] == 0 and maze[i+1][j] == 0:
                steps[i+1][j] = k + 1
            if j < len(steps[i])-1 and steps[i][j+1] == 0 and maze[i][j+1] == 0:
               steps[i][j+1] = k + 1
      if check == 0:
          return True
      else:
          return False

    def outputWayToExit(path):
        wayToExit = [[1]*length for i in range(length)]
        for i in range(len(path)):
            a, b = path[i]
            wayToExit[a][b] = 0
        return wayToExit

    k = 0
    while steps[end[0]][end[1]] == 0:
        k += 1
        if makeStep(k):
            print("Пути не существет")
            return
    i, j = end
    k = steps[i][j]
    path = [(i, j)]
    while k > 1:
      if i > 0 and steps[i - 1][j] == k-1:
        i, j = i-1, j
        path.append((i, j))
        k -= 1
      elif j > 0 and steps[i][j - 1] == k-1:
        i, j = i, j-1
        path.append((i, j))
        k -= 1
      elif i < len(steps) - 1 and steps[i + 1][j] == k-1:
        i, j = i+1, j
        path.append((i, j))
        k -= 1
      elif j < len(steps[i]) - 1 and steps[i][j + 1] == k-1:
        i, j = i, j+1
        path.append((i, j))
        k -= 1

    data = outputWayToExit(path)
    ax = sns.heatmap(maze, annot=True, fmt="d", cbar=None, xticklabels=False, yticklabels=False, cmap="Greens_r", vmin=-0.3, vmax=1.3)
    plt.title("Лабиринт", fontsize=18)
    plt.savefig("visualize_maze.png", bbox_inches='tight', dpi=100)
    plt.show()
    ax = sns.heatmap(data, annot=True, fmt="d", cbar=None, xticklabels=False, yticklabels=False, cmap="Greens_r", vmin=0, vmax=1.3)
    plt.title("Выход", fontsize=18)
    plt.savefig("visualize_way_to_exit.png", bbox_inches='tight', dpi=100)
    plt.show()