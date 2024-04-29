N = int(input())

ar = list(map(int,input().split()))
k=1;cnt=0
for i in range(len(ar)):
    if ar[i]==k:
        k+=1
    else:
        cnt+=1

    

print(cnt)