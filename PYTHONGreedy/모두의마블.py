cardNum = int(input())

cardList = []
card = (input()).split()
for i in range(cardNum):
    cardList.append(int(card[i]))
    
cardList = sorted(cardList, reverse=True)

result = 0
for i in range(1, cardNum):
    result += (cardList[0] + cardList[i])

print(result)