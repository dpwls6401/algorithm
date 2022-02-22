#my
# T = int(input())
# for i in range(T):
#     R,S = map(str,input().split())
#     for j in range(len(S)):
#         print(f"{S[j]*int(R)}",end="")
#     print()

#my + 강사님 코드리뷰 참고
T = int(input())

for i in range(T):
    R,S = input().split()
    for j in S:
        print(j * int(R), end="")