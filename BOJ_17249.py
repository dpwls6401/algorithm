# 태보태보 총난타

# 1. for문 활용
taebo = input().split("(^0^)")
left_cnt = 0
right_cnt = 0

for i in range(len(taebo[0])):
    if taebo[0][i] == "@":
        left_cnt += 1

for i in range(len(taebo[1])):
    if taebo[1][i] == "@":
        right_cnt += 1

print(left_cnt, right_cnt)


# 2. 메서드 활용 - 간단한 방법
left, right = input().split("0")
print(left.count('@'), right.count('@'))