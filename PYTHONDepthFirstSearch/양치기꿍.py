import sys
sys.setrecursionlimit(10**6)

def dfs(heightRoot, widthRoot, board, visitList):
  visitList[heightRoot][widthRoot] = True

  global goat, wolf
  if board[heightRoot][widthRoot] == "v":
    wolf += 1
  elif board[heightRoot][widthRoot] == "k":
    goat += 1

  for i in range(4):
    subHeight = (heightRoot + upDown[i])
    subWidth = (widthRoot + leftRight[i])

    if(subHeight >= 0 and subWidth >= 0 and subHeight < height and subWidth < width):
      if board[subHeight][subWidth] != "#" and not visitList[subHeight][subWidth]:
        dfs(subHeight, subWidth, board, visitList)

upDown = [-1,1,0,0]
leftRight = [0,0,-1,1]
goat = wolf = 0
goatResult = wolfResult = 0

height, width = map(int, input().split())

board = [["0" for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]
for i in range(height):
  firstLine = input()
  for j in range(width):
    board[i][j] = firstLine[j]

for i in range(height):
  for j in range(width):
    if board[i][j] != "#" and not visitList[i][j]:
      goat = 0
      wolf = 0
      dfs(i, j, board, visitList)
      if goat > wolf:
        goatResult += goat
      else:
        wolfResult += wolf

print(goatResult, wolfResult)
