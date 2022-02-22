chess = [list(input()) for i in range(8)]
white_cnt = 0

for i in range(8):
    if i % 2 == 0:
        for j in range(len(chess[i])):
            if j % 2 == 0:
                white_cnt += chess[i][j].count("F")
   
print(white_cnt)