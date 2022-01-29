height, width = map(int, input().split())

startBoard = [list(map(int, input())) for i in range(height)]
goalBoard = [list(map(int, input())) for i in range(height)]

result = 0
for i in range((height-2)):
    for j in range((width-2)):
        if startBoard[i][j] != goalBoard[i][j]:
            for k in range(3):
                for l in range(3):
                    startBoard[i+k][j+l] = (1- startBoard[i+k][j+l])

            result += 1

subCheck = True
for i in range(height):
    for j in range(width):
        if startBoard[i][j] != goalBoard[i][j]:
            subCheck = False

if subCheck:
    print(result)
else:
    print(-1)
