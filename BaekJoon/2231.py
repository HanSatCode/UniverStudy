num = int(input())
result = 0

for x in range(1, num+1) :
    sumsum = x + sum(list(map(int, str(x))))
    if sumsum == num :
        result = x
        break
print(result)



'''num = int(input())
result = 0

for x in range(1, num+1) :
    if x + (x//100) + (x%100//10) + (x%100%10) == num :
        result = x
        break

print(result)'''