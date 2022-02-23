# 딕셔너리 연습 2 - 나라 이름
n = int(input())
dic = {}

for _ in range(n):
    country, capital = input().split()
    dic[country] = capital

country_name = input()
if country_name in dic.keys():
    print(dic[country_name])
else:
    print("Unknown Country")

# 간단한 방법
print(dic.get(country_name, "Unknown Country"))


