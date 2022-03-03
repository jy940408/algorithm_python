from collections import deque

operatorList = ["*", "+", "-", "/"]

startNum, goalNum = map(int, input().split())
visitDict = {}

bfsDeque = deque()
bfsDeque.append([startNum, ""])
result = "-1"

if startNum == goalNum:
  result = "0"

if result == "-1":
  while bfsDeque:
    thisDeque = bfsDeque.popleft()

    if thisDeque[0] == goalNum:
      result = thisDeque[1]
      break

    for i in range(4):
      if i == 0:
        if (thisDeque[0]*thisDeque[0]) <= 1000000000 and not (thisDeque[0]*thisDeque[0]) in visitDict:
          bfsDeque.append([(thisDeque[0]*thisDeque[0]), (thisDeque[1] + operatorList[i])])
          visitDict[(thisDeque[0]*thisDeque[0])] = True
      elif i == 1:
        if (thisDeque[0]+thisDeque[0]) <= 1000000000 and not (thisDeque[0]+thisDeque[0]) in visitDict:
          bfsDeque.append([(thisDeque[0]+thisDeque[0]), (thisDeque[1] + operatorList[i])])
          visitDict[(thisDeque[0]+thisDeque[0])] = True
      elif i == 2:
        if (thisDeque[0]-thisDeque[0]) >= 0 and  not (thisDeque[0]-thisDeque[0]) in visitDict:
          bfsDeque.append([(thisDeque[0]-thisDeque[0]), (thisDeque[1] + operatorList[i])])
          visitDict[(thisDeque[0]-thisDeque[0])] = True
      else:
        if thisDeque[0] != 0:
          if not (thisDeque[0]//thisDeque[0]) in visitDict:
            bfsDeque.append([(thisDeque[0]//thisDeque[0]), (thisDeque[1] + operatorList[i])])
            visitDict[(thisDeque[0]//thisDeque[0])] = True

print(result)