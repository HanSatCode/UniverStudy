n = input()

while True :
    if n.find('pi') >= 0 :
        n = n.replace('pi', ' ')
    elif n.find('ka') >= 0 :
        n = n.replace('ka', ' ')
    elif n.find('chu') >= 0 :
        n = n.replace('chu', ' ')
    else :
        if len(n.strip()) == 0 :
            print('YES')
            break
        else :
            print('NO')
            break


'''word = ["pi", "ka", "chu"]
n = input()
x = 0

while x <= len(n)-1 :
    if len(n[x:]) == 1 :
        print('NO')
        break
    else :
        if str(n[x]+n[x+1]) == word[0] or str(n[x]+n[x+1]) == word[1] :
            x += 2
        elif str(n[x]+n[x+1]+n[x+2]) == word[2] :
            x += 3
        else :
            print('NO')
            break
else :
    print('YES')'''