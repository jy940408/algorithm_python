from collections import deque

upDown = [-1, -2, -2, -1, 1, 2, 2, 1]
leftRight = [-2, -1, 1, 2, -2, -1, 1, 2]

startHeight, startWidth = map(int, input().split())
goalHeight, goalWidth = map(int, input().split())

visitList = [[False for i in range(9)] for i in range(9)]

bfsDeque = deque()
bfsDeque.append([startHeight, startWidth, 0])

result = 0
while bfsDeque:
  thisDeque = bfsDeque.popleft()

  if thisDeque[0] == goalHeight and thisDeque[1] == goalWidth:
    result = thisDeque[2]
    break

  for i in range(8):
    thisHeight = (thisDeque[0] + upDown[i])
    thisWidth = (thisDeque[1] + leftRight[i])

    if 1 <= thisHeight < 9 and 1 <= thisWidth < 9:
      if not visitList[thisHeight][thisWidth]:
        visitList[thisHeight][thisWidth] = True
        bfsDeque.append([thisHeight, thisWidth, (thisDeque[2]+1)])

print(result)