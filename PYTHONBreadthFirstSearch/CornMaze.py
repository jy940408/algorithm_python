from collections import deque

height, width = map(int, input().split())

upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]

board = [["" for i in range(width)] for i in range(height)]
visitList = [[False for i in range(width)] for i in range(height)]

slideList = [[[0, 0] for i in range(width)] for i in range(height)]
checkList = [[-1, -1] for i in range(26)]

bfsDeque = deque()
for i in range(height):
  firstLine = input()
  for j in range(width):
    board[i][j] = firstLine[j]

    if board[i][j] == "@":
      bfsDeque.append([i, j, 0])
    elif board[i][j] != "@" and board[i][j] != "." and board[i][j] != "=" and board[i][j] != "#":
      if checkList[ord(board[i][j])-65][0] != -1:
        slideList[i][j] = checkList[ord(board[i][j])-65]
        slideList[checkList[ord(board[i][j])-65][0]][checkList[ord(board[i][j])-65][1]] = [i, j]
        
      else:
        checkList[ord(board[i][j])-65] = [i, j]

result = 0
while bfsDeque:
  thisDeque = bfsDeque.popleft()

  if board[thisDeque[0]][thisDeque[1]] == "=":
    result = thisDeque[2]
    break

  for i in range(4):
    thisHeight = (thisDeque[0] + upDown[i])
    thisWidth = (thisDeque[1] + leftRight[i])

    if 0 <= thisHeight < height and 0 <= thisWidth < width:
      if board[thisHeight][thisWidth] != "#":
        if not visitList[thisHeight][thisWidth]:
          visitList[thisHeight][thisWidth] = True
          if board[thisHeight][thisWidth] == ".":
            bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])
          elif board[thisHeight][thisWidth] != "." and board[thisHeight][thisWidth] != "@" and board[thisHeight][thisWidth] != "=":
            bfsDeque.append([slideList[thisHeight][thisWidth][0], slideList[thisHeight][thisWidth][1], (thisDeque[2]+1)])
          else:
            bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

print(result)