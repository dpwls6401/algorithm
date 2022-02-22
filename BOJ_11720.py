# += 방식
# N = int(input())
# n = input()
# sum = 0

# for i in range(N):
#     sum += int(n[i])
# print(sum)

#내장함수 sum 활용
# n = input()
# for i in range(n):
#     print(sum(map(int, input())))

#강사님 풀이 - sum 내장함수
n = int(input())
numbers = list(map(int, input()))
print(sum(numbers))