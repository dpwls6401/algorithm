# 2차원 리스트 곱셈 - 헷갈리면 과정 사이사이에 print 찍어서 값의 변화 확인
# my
first = [list(map(int, input().split())) for _ in range(2)]
second = [list(map(int, input().split())) for _ in range(2)]
product = []

for i in range(2):
    tmp = []
    for j in range(3):
        tmp.append(first[i][j] * second[i][j])
    product.append(tmp)
print(product)

for x,y,z in product:
    print(x,y,z)

# 강사님 풀이
list_a = [list(map(int, input().split())) for _ in range(2)]
list_b = [list(map(int, input().split())) for _ in range(2)]
list_c = [[0] * 3 for _ in range(2)]

for i in range(2):
    for j in range(3):
        list_c[i][j] = list_a[i][j] * list_b[i][j]

for i in range(2):
    for j in range(3):
        print(list_c[i][j], end=" ")
    print()