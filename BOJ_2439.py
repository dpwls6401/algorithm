# 별 찍기 - 2
num = int(input())
for i in range(num):
    print(f'{" " * (num - i - 1)}{"*" * (i + 1)}')