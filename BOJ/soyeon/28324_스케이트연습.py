import sys
input = sys.stdin.readline

N = int(input())
V = list(map(int, input().split()))
V.reverse()
h, n = 0, 0
for i in range(N):
    if (V[i] > n):
        n += 1
    elif (V[i] < n):
        n = V[i]
    h += n
print(h)
