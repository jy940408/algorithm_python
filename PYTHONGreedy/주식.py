roundNum = int(input())

for i in range(roundNum):
  dayNum = int(input())
  stockList = list(map(int, input().split()))

  maxNum = stockList[dayNum-1]
  result = 0
  for i in range(dayNum-1, -1, -1):
    if stockList[i] > maxNum:
      maxNum = stockList[i]
    else:
      result += (maxNum - stockList[i])

  print(result)