a=int(input())
b=list(map(int,input().split()))
c=[]
for i in range(len(b)):
    for j in range(len(b)):
        if i<j:
            c.append(b[i] + b[j] + (i - j))
print(max(*c))
