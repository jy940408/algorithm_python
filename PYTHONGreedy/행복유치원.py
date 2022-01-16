kidsNum, groupNum = map(int, (input()).split())
heightList = list(map(int, (input()).split()))

diffList = []
for i in range(1, kidsNum):
    diffList.append(heightList[i]-heightList[i-1])
diffList.sort()

result = 0
for i in range(kidsNum-groupNum):
    result += diffList[i]

print(result)