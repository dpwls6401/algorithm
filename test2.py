# 2차원 리스트 만들기 연습

n, m = map(int, input().split()) # 2차원 리스트 가로, 세로 크기 받기
a = [list(map(int, input().split())) for i in range(n)]
print(a)