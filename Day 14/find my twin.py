n = int(input())
a = list(map(int, input().split()))
a.sort()
for i in range(n-1):
    if(a[i]==a[i+1]):
        print(a[i])
© 2022 GitHub, Inc.
