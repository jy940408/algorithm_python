changeNum = int(input())

greedyStack = []
result = 0
for i in range(changeNum):
    changeIdx, height = map(int, input().split())

    if i == 0:
        if height != 0:
            greedyStack.append(height)
            result += 1
    else:
        while True:
            if len(greedyStack) != 0:
                if height != 0:
                    if greedyStack[-1] > height:
                        greedyStack.pop()
                    elif greedyStack[-1] < height:
                        greedyStack.append(height)
                        result += 1
                        break
                    else:
                        break
                else:
                    greedyStack = []
                    break

            else:
                if height != 0:
                    greedyStack.append(height)
                    result += 1
                    break
                else:
                    break

print(result)