A,B = map(int,input().split())
C = int(input()) 


A = A + C//60
B = B + C%60

if A >= 24:
    A = A-24
if B >= 60:
    B = B-60
    A = (A+1)%24

print(A,B)



