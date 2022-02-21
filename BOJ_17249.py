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