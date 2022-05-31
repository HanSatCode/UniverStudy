num = int(input())
member = []

for x in range(num) :
    member.append(input().split())

member.sort(key = lambda x : int(x[0]))

for x in range(num) :
    print(member[x][0], member[x][1])


''' # 이전 알고리즘 - 시간초과
num = int(input())
member = []

for x in range(num) :
    reg = input().split()
    member.append(reg)

x = 0

while True :
    if len(member) == 0 :
        break

    else :
        minAge = min(member)[0]

        if member[x][0] == minAge :
            print(member[x][0], member[x][1], sep=' ', end='\n')
            member.remove(member[x])
            x = 0
        else :
            x += 1
'''