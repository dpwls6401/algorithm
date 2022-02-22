first = [list(map(int, input().split())) for i in range(2)]
second = [list(map(int, input().split())) for i in range(2)]
product = [[0]*4]*2

for i in range(len(first)):
    product[i] = list(map(lambda x,y: x*y, first[i], second[i]))
print(product)