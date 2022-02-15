height, width = map(int, (input()).split())

result = 0
for i in range(height):
    startCheck = False
    firstLine = input()
    
    for j in range(width):
        if firstLine[j] == "/":
            result += 1/2
            if not startCheck:
                startCheck = True
            else:
                startCheck = False

        elif firstLine[j] == "\\":
            result += 1/2
            if not startCheck:
                startCheck = True
            else:
                startCheck = False

        else:
            if startCheck:
                result += 1

print(int(result))