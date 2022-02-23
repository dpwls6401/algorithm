# 나는 요리사다

score = [list(map(int, input().split())) for i in range(5)]
final = []

for i in range(5):
    final.append(sum(score[i]))
winner = max(final)
print(final.index(winner) + 1, winner)