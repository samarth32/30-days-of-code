n = int(input())
a = list(map(int,input().split()))
count = 0
for i in range(len(a)):
    if((a[i]+1) in a):
        count += 1
print(count)
