a = input('Enter String : ').split('/')

if len(a) > 3 :
    for x in range(3, len(a)) :
        a[2] += '/' + str(a[x])

print(f'"First String : {a[0].lower()}"')
print(f'"Second String : {a[1].lower()}"')
print(f'"Third String : {a[2].lower()}"')