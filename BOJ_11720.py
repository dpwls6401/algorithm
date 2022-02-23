# += 방식
# N = int(input())
# n = input()
# sum = 0

# for i in range(N):
#     sum += int(n[i])
# print(sum)

#강사님 풀이 - sum 내장함수
n = int(input()) #파이썬에서는 필요 없음. 다른 언어 위해 써둔 것
numbers = list(map(int, input()))
print(sum(numbers))