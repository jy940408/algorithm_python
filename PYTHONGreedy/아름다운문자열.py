fullWord = list(input())
goalWord = list(input())

idxList = [0 for i in range(26)]
for i in range(len(goalWord)):
    idxList[ord(goalWord[i])-97] = (i+1)

board = [0 for i in range(len(goalWord)+1)]
for i in range(len(fullWord)):
    if idxList[(ord(fullWord[i])-97)] != 0:
        if idxList[(ord(fullWord[i])-97)] == 1:
            board[idxList[(ord(fullWord[i])-97)]] += 1

        else:
            if board[idxList[(ord(fullWord[i])-97)]-1] > 0:
                board[idxList[(ord(fullWord[i])-97)]-1] -= 1
                board[idxList[(ord(fullWord[i])-97)]] += 1

print(board[len(goalWord)])