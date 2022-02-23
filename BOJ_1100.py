chess = [list(input()) for i in range(8)]

# 1. without comprehension
# white_chess = []
# for i in range(8):
#     for j in range(8):
#         if (i % 2 == j % 2) and chess[i][j] == "F":
#             white_chess.append(chess[i][j])
# print(len(white_chess))

# # 2. w/ list comprehension
# white_chess = [chess[i][j] for i in range(8) for j in range(8) if (i % 2 == j % 2) and (chess[i][j] == "F")]
# print(len(white_chess))

# without comprehension - 피드백 반영
chess = [list(input()) for i in range(8)]
white_chess = []
cnt = 0

for i in range(8):
	for j in range(8):
		if (i % 2 == j % 2) and (chess[i][j] == "F"):
			cnt += 1
print(cnt)