import sys
input = sys.stdin.readline

for _ in range(3) :
    arr = list(map(int, input().split()))
    
    sum = 0
    for i in range(4) :
        if arr[i]==0 :
            sum += 1
    
    if sum==1 :
        print("A")
    elif sum==2 :
        print("B")
    elif sum==3 :
        print("C")
    elif sum==4 :
        print("D")
    else :
        print("E")
