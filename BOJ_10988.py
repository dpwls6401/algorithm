# 팰린드롬인지 확인하기

# 1. 문자열 슬라이싱
word = input()
if word == word[::-1]:
    print("1")
else:
    print("0")

# 2. 반복문
word = input()
cnt = 0
for i in range(len(word)):
    if word[i] == word[len(word)-1-i]:
        cnt += 1
if cnt == len(word):
    print("1")
else:
    print("0")  

# 3. 강사님 풀이
word = input()
reversed_word = ""

for i in range(len(word) - 1, -1, -1):
    reversed_word += word[i]

if word == reversed_word:
    print(1)
else:
    print(0)

# 한 줄로 쓰기
print(1 if word == word[::-1] else 0)

# bool type 특성 활용
print(int(word == word[::-1]))      