T = int(input())
for i in range(T):
    R,S = map(str,input().split())
    for j in range(len(S)):
        print(f"{S[j]*int(R)}",end="")
    print()
