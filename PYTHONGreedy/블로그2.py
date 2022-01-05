length = int(input())
sentence = input()

lastLength = 0
result = 0
if sentence[0] != sentence[length-1]:
    for i in range((length-1), -1, -1):
        if sentence[length-1] == sentence[i]:
            lastLength += 1
        else:
            result += 2
            whileNum = 0
            while whileNum < ((length-1)-lastLength):
                if sentence[(length-1)] == sentence[whileNum]:
                    while sentence[(length-1)] == sentence[whileNum]:
                        whileNum += 1
                    result += 1
                whileNum += 1
            break

else:
    result += 1
    whileNum = 0
    while whileNum < length:
        if sentence[0] != sentence[whileNum]:
            while sentence[0] != sentence[whileNum]:
                whileNum += 1
            result += 1
        whileNum += 1

print(result)
