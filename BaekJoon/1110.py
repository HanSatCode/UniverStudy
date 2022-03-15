chess = []
result = 0
y = 0

for x in range (0, 8) :
    chess.append(list(str(input())))

while True :

    y += 1

    if y%2 != 0 :
        for x in range (0, 7, 2) :
            if chess[y-1][x] == 'F' :
                result += 1
    else :
        for x in range(1, 8, 2) :
            if chess[y-1][x] == 'F' :
                result += 1

    if y == 8 :
        break

print(result)