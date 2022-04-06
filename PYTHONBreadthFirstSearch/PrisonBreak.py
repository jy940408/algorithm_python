from collections import deque

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

roundNum = int(input())
for i in range(roundNum):
  width, height, startWidth, startHeight, goalWidth, goalHeight = map(int, input().split())
  startHeight = (height-startHeight)
  startWidth -= 1
  
  goalHeight = (height-goalHeight)
  goalWidth -= 1

  board = [list(input()) for i in range(height)]
  visitList = [[False for i in range(width)] for i in range(height)]

  bfsDeque = deque()
  bfsDeque.append([startHeight, startWidth, board[startHeight][startWidth]])

  result = "NO"
  while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == goalHeight and thisDeque[1] == goalWidth:
      result = "YES"
      break

    for i in range(4):
      thisHeight = (thisDeque[0] + upDown[i])
      thisWidth = (thisDeque[1] + leftRight[i])

      if 0 <= thisHeight < height and 0 <= thisWidth < width:
        if board[thisHeight][thisWidth] == thisDeque[2]:
          if not visitList[thisHeight][thisWidth]:
            visitList[thisHeight][thisWidth] = True
            bfsDeque.append([thisHeight, thisWidth, thisDeque[2]])

  print(result)