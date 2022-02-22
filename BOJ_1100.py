chess = [list(input()) for i in range(8)]

# 1. without comprehension
# white_chess = []
# for i in range(8):
#     for j in range(8):
#         if (i % 2 == j % 2) and chess[i][j] == "F":
#             white_chess.append(chess[i][j])
# print(len(white_chess))

# 2. w/ list comprehension
white_chess = [chess[i][j] for i in range(8) for j in range(8) if (i % 2 == j % 2) and (chess[i][j] == "F")]
print(len(white_chess))