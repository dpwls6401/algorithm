# 별 찍기 - 20
num = int(input())
for i in range(num):
    if i%2 ==0:
        print(f'{"* "*num}')
    else:
        print(f'{" *"*num}')

#slicing 활용한 풀이
n = int(input())
line = "* " * n

for i in range(n):
    print(line)
    line = line[::-1] #뒤집은 걸 넣음