#my
N = int(input())
num = []

for i in range(N):
    num.append(int(input()))
num = sorted(num)

for j in range(len(num)):
    print(num[j])


#강사님 풀이
n = int(input())
numbers = []

for i in range(n): #여러 줄이므로 여러 input 필요하므로 for문
    number = int(input())
    numbers.append(number)

for number in sorted(numbers):
    print(number)