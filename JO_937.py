# 2차원 리스트 곱셈 - 헷갈리면 과정 사이사이에 print 찍어서 값의 변화 확인
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