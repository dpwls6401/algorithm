N = int(input())
num = []

for i in range(N):
    num.append(int(input()))
num = sorted(num)

for j in range(len(num)):
    print(num[j])