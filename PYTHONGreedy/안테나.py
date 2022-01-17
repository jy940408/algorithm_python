houseNum = int(input())

houseList = list(map(int, input().split()))
houseList = sorted(houseList)

print(houseList[(houseNum-1)//2])