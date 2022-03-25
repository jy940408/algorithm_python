from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

height, width = map(int, input().split())

board = [[0 for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]
for i in range(height):
  firstLine = input()
  for j in range(width):
    board[i][j] = int(firstLine[j])

startHeight, startWidth, colorNum = map(int, input().split())
bfsDeque = deque()
bfsDeque.append([startHeight, startWidth, board[startHeight][startWidth]])
board[startHeight][startWidth] = colorNum
visitList[startHeight][startWidth] = True

while bfsDeque:
  thisDeque = bfsDeque.popleft()

  for i in range(4):
    thisHeight = (thisDeque[0] + upDown[i])
    thisWidth = (thisDeque[1] + leftRight[i])

    if 0 <= thisHeight < height and 0 <= thisWidth < width:
      if board[thisHeight][thisWidth] == thisDeque[2]:
        if not visitList[thisHeight][thisWidth]:
          visitList[thisHeight][thisWidth] = True
          board[thisHeight][thisWidth] = colorNum

          bfsDeque.append([thisHeight, thisWidth, thisDeque[2]])

result = ""
for i in range(height):
  for j in range(width):
    result += str(board[i][j])
  result += "\n"

print(result)