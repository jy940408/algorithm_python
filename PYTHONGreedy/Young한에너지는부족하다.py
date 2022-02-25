crewNum = int(input())
crewList = list(map(int, input().split()))

crewList = sorted(crewList)
result = crewList[2*crewNum-1] - crewList[crewNum]

print(result)