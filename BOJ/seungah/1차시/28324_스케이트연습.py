import sys

input = sys.stdin.readline
N = int(input())
ar = list(map(int,input().split()))

cnt = [0]*N
cnt[-1]=1
p = 1
for i in range(N-1):
    if(p+1 <= ar[N-i-2]):
        p=p+1
        cnt[N-i-2] = p
    else:
        p = ar[N-i-2]
        cnt[N-i-2] = p
print(sum(cnt))


