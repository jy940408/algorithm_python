listNum = int(input())

leftBoard = []
rightBoard = []
for i in range(listNum):
  testNum = int(input())
  if testNum <= 0:
    leftBoard.append(testNum)
  else:
    rightBoard.append(testNum)

leftBoard = sorted(leftBoard)
rightBoard = sorted(rightBoard, reverse=True)

result = 0
for i in range(0, len(leftBoard), 2):
  if i < (len(leftBoard)-1):
    result += (leftBoard[i]*leftBoard[i+1])
  else:
    result += leftBoard[i]

for i in range(0, len(rightBoard), 2):
  if i < (len(rightBoard)-1):
    if rightBoard[i] == 1 or rightBoard[i+1] == 1:
      result += (rightBoard[i]+rightBoard[i+1])
    else:
      result += (rightBoard[i]*rightBoard[i+1])
  else:
    result += rightBoard[i]

print(result)