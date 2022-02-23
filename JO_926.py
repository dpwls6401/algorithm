# my
first = [list(map(int, input().split())) for i in range(2)]
second = [list(map(int, input().split())) for i in range(2)]
product = [[0]*4]*2

for i in range(len(first)):
    product[i] = list(map(lambda x, y: x*y, first[i], second[i]))
print(product)


# # 강사님 피드백 반영
first = [list(map(int, input().split())) for i in range(2)]
second = [list(map(int, input().split())) for i in range(2)]
product = []

for i in range(len(first)):
    product.append(list(map(lambda x,y: x*y, first[i], second[i])))
print(product)

# 강사님 풀이
# 한줄 복제 : option + shift + 방향키 아래
list_a = [list(map(int, input().split())) for i in range(2)]
list_b = [list(map(int, input().split())) for i in range(2)]

for i in range(2):
    for j in range(4):
        print(list_a[i][j] * list_b[i][j], end=" ")
    print()