def testMaze3D():

    maze = [[[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [0, 0, 0, 1, 1]],

            [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1]],

            [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1]],

            [[1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]],

            [[1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1]]]
    start = 0, 4, 0
    end = 4, 0, 2
    length = len(maze)
    steps = [[[0 for i in range(length)] for j in range(length)] for k in range(length)]
    i, j, k = start
    steps[i][j][k] = 1
    for line in maze:
        print(*line)
    def makeStep3D(a):
      for i in range(length):
        for j in range(length):
          for k in range(length):
            if steps[i][j][k] == a:
              if i > 0 and steps[i-1][j][k] == 0 and maze[i-1][j][k] == 0:
                  steps[i-1][j][k] = a + 1
              if j > 0 and steps[i][j-1][k] == 0 and maze[i][j-1][k] == 0:
                  steps[i][j-1][k] = a + 1
              if k > 0 and steps[i][j][k-1] == 0 and maze[i][j][k-1] == 0:
                  steps[i][j][k-1] = a + 1
              if i < len(steps[i][j])-1 and steps[i+1][j][k] == 0 and maze[i+1][j][k] == 0:
                  steps[i+1][j][k] = a + 1
              if j < len(steps)-1 and steps[i][j+1][k] == 0 and maze[i][j+1][k] == 0:
                  steps[i][j+1][k] = a + 1
              if k < len(steps[i])-1 and steps[i][j][k+1] == 0 and maze[i][j][k+1] == 0:
                  steps[i][j][k+1] = a + 1

    def outputWayToExit3D(path):
        wayToExit = [[[1]*length]*length for i in range(length)]
        for i in range(len(path)):
            a, b, c = path[i]
            wayToExit[a][b][c] = 0
        return wayToExit

    k = 0
    while steps[end[0]][end[1]][end[2]] == 0:
        k += 1
        makeStep3D(k)

    i, j, k = end
    a = steps[i][j][k]
    path = [(i, j, k)]
    while a > 1:
      if i > 0 and steps[i - 1][j][k] == a-1:
        i, j, k = i - 1, j, k
        path.append((i, j, k))
        a -= 1
      elif j > 0 and steps[i][j - 1][k] == a-1:
        i, j, k = i, j - 1, k
        path.append((i, j, k))
        a -= 1
      elif k > 0 and steps[i][j][k-1] == a-1:
        i, j, k = i, j, k - 1
        path.append((i, j, k))
        a -= 1
      elif i < len(steps) - 1 and steps[i + 1][j][k] == a-1:
        i, j, k = i + 1, j, k
        path.append((i, j, k))
        a -= 1
      elif j < len(steps[i][j]) - 1 and steps[i][j + 1][k] == a-1:
        i, j, k = i, j + 1, k
        path.append((i, j, k))
        a -= 1
      elif k < len(steps[i]) - 1 and steps[i][j][k + 1] == a-1:
        i, j, k = i, j, k + 1
        path.append((i, j, k))
        a -= 1

    print("Путь через лабиринт: ", path)

def maze3D(maze):
    start = -1, -1, -1
    end = -1, -1, -1
    check = False
    for i in range(len(maze[0])):
        if check:
            break
        for j in range(len(maze[0])):
            if maze[0][i][j] == 0:
                start = 0, i, j
                check = True

    i, j, k = start
    if i == -1:
        print("Нет входа")
        return
    check = False
    for i in range(len(maze[0])):
        if check:
            break
        for j in range(len(maze[0])):
            if maze[len(maze[0]) - 1][i][j] == 0:
                end = len(maze[0]) - 1, i, j
                check = True

    i, j, k = end
    if i == -1:
        print("Нет выхода")
        return
    length = len(maze)
    steps = [[[0 for i in range(length)] for j in range(length)] for k in range(length)]
    i, j, k = start
    steps[i][j][k] = 1
    for line in maze:
        print(*line)
    def makeStep3D(a):
      check = 0
      for i in range(length):
        for j in range(length):
          for k in range(length):
            if steps[i][j][k] == a:
              check = 1
              if i > 0 and steps[i-1][j][k] == 0 and maze[i-1][j][k] == 0:
                  steps[i-1][j][k] = a + 1
              if j > 0 and steps[i][j-1][k] == 0 and maze[i][j-1][k] == 0:
                  steps[i][j-1][k] = a + 1
              if k > 0 and steps[i][j][k-1] == 0 and maze[i][j][k-1] == 0:
                  steps[i][j][k-1] = a + 1
              if i < len(steps[i][j])-1 and steps[i+1][j][k] == 0 and maze[i+1][j][k] == 0:
                  steps[i+1][j][k] = a + 1
              if j < len(steps)-1 and steps[i][j+1][k] == 0 and maze[i][j+1][k] == 0:
                  steps[i][j+1][k] = a + 1
              if k < len(steps[i])-1 and steps[i][j][k+1] == 0 and maze[i][j][k+1] == 0:
                  steps[i][j][k+1] = a + 1
      if check == 0:
        return True
      else:
        return False

    def outputWayToExit3D(path):
        wayToExit = [[[1]*length]*length for i in range(length)]
        for i in range(len(path)):
            a, b, c = path[i]
            wayToExit[a][b][c] = 0
        return wayToExit

    k = 0
    while steps[end[0]][end[1]][end[2]] == 0:
        k += 1
        if makeStep3D(k):
            print("Пути не существет")
            return

    i, j, k = end
    a = steps[i][j][k]
    path = [(i, j, k)]
    while a > 1:
      if i > 0 and steps[i - 1][j][k] == a-1:
        i, j, k = i - 1, j, k
        path.append((i, j, k))
        a -= 1
      elif j > 0 and steps[i][j - 1][k] == a-1:
        i, j, k = i, j - 1, k
        path.append((i, j, k))
        a -= 1
      elif k > 0 and steps[i][j][k-1] == a-1:
        i, j, k = i, j, k - 1
        path.append((i, j, k))
        a -= 1
      elif i < len(steps) - 1 and steps[i + 1][j][k] == a-1:
        i, j, k = i + 1, j, k
        path.append((i, j, k))
        a -= 1
      elif j < len(steps[i][j]) - 1 and steps[i][j + 1][k] == a-1:
        i, j, k = i, j + 1, k
        path.append((i, j, k))
        a -= 1
      elif k < len(steps[i]) - 1 and steps[i][j][k + 1] == a-1:
        i, j, k = i, j, k + 1
        path.append((i, j, k))
        a -= 1

    print("Путь через лабиринт: ", path)