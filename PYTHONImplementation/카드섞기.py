cardNum = int(input())

orderList = list(map(int, (input()).split()))
shuffleList = list(map(int, (input()).split()))
cardList = [i for i in range(cardNum)]
subList = [0 for i in range(cardNum)]

result = 0
subCheck = True

firstCheck = True
for i in range(cardNum):
    if orderList[i] != (cardList[i]%3):
        firstCheck = False
        break

if not firstCheck:
    while True:
        result += 1

        for i in range(cardNum):
            subList[i] = cardList[shuffleList[i]]
            
        for i in range(cardNum):
            cardList[i] = subList[i]

        resultCheck = True
        for i in range(cardNum):
            if orderList[i] != (cardList[i]%3):
                resultCheck = False
                break

        for i in range(cardNum):
            if cardList[i] == i:
                if i == (cardNum-1):
                    subCheck = False
                    break
            else:
                break
        
        if resultCheck or not subCheck:
            break

if subCheck:
    print(result)
else:
    print(-1)