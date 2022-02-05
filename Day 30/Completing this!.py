a = int(input())
b = list(input().split(' '))

first, second = 0, 0

for i in range(a):
    if i % 2 == 0:
        first += int(b[i])
    else:
        second += int(b[i])
        
print(max(first, second))
