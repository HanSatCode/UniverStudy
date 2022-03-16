s = []
c = []
result = ''
for x in range(0, 5) :
    s.append(list(str(input())))
    c.append(len(s[x]))

for x in range(0, 5) :
    for y in range(len(s[x]), max(c)) :
        s[x].append('')

for x in range(0, max(c)) :
    for y in range(0, 5) :
        if str(s[y][x]) == '' :
            continue
        else :
            result += str(s[y][x])

print(result)