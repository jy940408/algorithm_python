sensorNum = int(input())
centerNum = int(input())

firstLine = (input()).split()

sensorList = []
for i in range(sensorNum):
    sensorList.append(int(firstLine[i]))
sensorList.sort()

lengthList = []
for i in range(1, len(sensorList)):
    lengthList.append((sensorList[i] - sensorList[(i-1)]))
lengthList.sort()

result = 0
for i in range((len(lengthList)-(centerNum-1))):
    result += lengthList[i]

print(result)
