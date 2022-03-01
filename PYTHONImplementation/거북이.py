upDown = [-1, 1, 0, 0]
leftRight = [0, 0, -1, 1]
turnLeft = [2, 3, 1, 0]
turnRight = [3, 2, 0, 1]

roundNum = int(input())
for i in range(roundNum):
    testCase = input()
    
    minHeight, minWidth, maxHeight, maxWidth = 0, 0, 0, 0
    thisHeight, thisWidth, direction = 0, 0, 0
    
    for j in testCase:
        if j == "L":
            direction = turnLeft[direction]
            continue

        elif j == "R":
            direction = turnRight[direction]
            continue

        elif j == "F":
            thisHeight += upDown[direction]
            thisWidth += leftRight[direction]
        elif j == "B":
            thisHeight -= upDown[direction]
            thisWidth -= leftRight[direction]
            
        minHeight = min(minHeight, thisHeight)
        minWidth = min(minWidth, thisWidth)
        maxHeight = max(maxHeight, thisHeight)
        maxWidth = max(maxWidth, thisWidth)

    print(abs(maxHeight - minHeight) * abs(maxWidth - minWidth))