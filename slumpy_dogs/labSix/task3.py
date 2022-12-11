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
start = 7, 0
end = 7, 14
length = len(maze)
steps = [ [0]*length for i in range(length)]
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
    k-=1
  elif i < len(steps) - 1 and steps[i + 1][j] == k-1:
    i, j = i+1, j
    path.append((i, j))
    k -= 1
  elif j < len(steps[i]) - 1 and steps[i][j + 1] == k-1:
    i, j = i, j+1
    path.append((i, j))
    k -= 1
print(path)
