N = int(input())

A = list(map(int,input().split()))

on, cnt = 1, 0
for i in range(N):
    if A[i] == on:
        on += 1
    else:
        cnt += 1

print(cnt)