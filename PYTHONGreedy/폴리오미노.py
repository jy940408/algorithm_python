sentence = input()

result = ""
round = 0
for i in range(len(sentence)):

    if sentence[i] == "X":
        round += 1

        if i == (len(sentence)-1):
            if (round%4)%2 == 0:
                result += "A"*(round//4)*4
                result += "B"*(round%4)
            else:
                result = -1
                break

    elif (sentence[i] == ".") or (i == (len(sentence)-1)):
        
        if (round%4)%2 == 0:
            result += "A"*(round//4)*4
            result += "B"*(round%4)
        else:
            result = -1
            break

        round = 0
        result += "."

print(result)