n=int(input())
k=int(input())
l=list(map(int,input().split()))
try:
    print(l.index(k))
except:
    print("-1")
