menuNum = int(input())
board = list(map(int, input().split()))
visitList = [0 for i in range(menuNum+1)]

subResult = 0
result = 0

for i in range(menuNum*2):
    if visitList[board[i]] == 0:
        visitList[board[i]] += 1
        subResult += 1

    elif visitList[board[i]] == 1:
        visitList[board[i]] += 1
        subResult -= 1
    
    result = max(result, subResult)
        
print(result)