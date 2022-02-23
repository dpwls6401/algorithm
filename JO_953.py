# 딕셔너리 연습 3 - 야구 파울
foul = input().split()
player = dict.fromkeys(foul,0)

for i in range(len(foul)):
    player[foul[i]] += 1

for p_key in player.keys():
    if player[p_key] == min(player.values()):
        print(p_key)
print(min(player.values()))