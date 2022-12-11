import seaborn as sns; sns.set()
import matplotlib.pyplot as plt

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
steps = [[0]*length for i in range(length)]
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
    k-=1
  elif i < len(steps) - 1 and steps[i + 1][j] == k-1:
    i, j = i+1, j
    path.append((i, j))
    k -= 1
  elif j < len(steps[i]) - 1 and steps[i][j + 1] == k-1:
    i, j = i, j+1
    path.append((i, j))
    k -= 1

data = outputWayToExit(path)
ax = sns.heatmap(data, annot=True, fmt="d", cbar=None, xticklabels=False, yticklabels=False)
plt.title("Визуализация массива",fontsize=12)
plt.savefig("visualize_way_to_exit.png", bbox_inches='tight', dpi=100)
plt.show()