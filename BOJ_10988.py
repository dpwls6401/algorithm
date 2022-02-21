#문자열 슬라이싱
word = input()
if word == word[::-1]:
    print("1")
else:
    print("0")

#반복문
# word = input()
# cnt = 0
# for i in range(len(word)):
#     if word[i] == word[len(word)-1-i]:
#         cnt += 1
# if cnt == len(word):
#     print("1")
# else:
#     print("0")        