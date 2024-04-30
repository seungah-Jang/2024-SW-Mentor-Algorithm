a, b = map(int, input().split())
c = int(input())
r = a*60+b+c
if (r >= 1440):
    r = r-1440
print(r//60, r % 60)
