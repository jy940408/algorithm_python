roundNum = int(input())
roomList = []

for i in range(roundNum):
    startNum, endNum = map(int, (input()).split())
    roomList.append([startNum, endNum])

roomList = sorted(roomList, key = lambda a: a[0])
roomList = sorted(roomList, key = lambda a: a[1])

endTime, result = 0, 0

for i in range(len(roomList)):
    if roomList[i][0] >= endTime:
        endTime = roomList[i][1]
        result += 1

print(result)