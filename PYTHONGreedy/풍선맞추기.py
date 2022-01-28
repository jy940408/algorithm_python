balloonNum = int(input())

subBalloon = list(map(int, (input()).split()))

balloonList = [0 for i in range(1000001)]

print(0, balloonList)
result = 0
for i in subBalloon:
    
    if balloonList[i] == 0:
        balloonList[i-1] += 1
        result += 1

    else:
        balloonList[i] -= 1
        balloonList[i-1] += 1
    
    print(i, balloonList)

print(result)