# 평균은 넘겠지
C = int(input())
score = [list(map(int, input().split())) for _ in range(C)]
avg = []
good = []

for i in range(C):
    avg.append(sum(score[i][1:]) / len(score[i][1:]))
    for j in range(len(score[i]) - 1):


        if score[i][j + 1] > avg[i]:
            good.append(round((score[1:].count(score[i][j + 1] > avg[i]) / score[i][0]), 3))

print(good)