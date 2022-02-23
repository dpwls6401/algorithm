#my
# forbidden_word = list("CAMBRIDGE")
# email = input().upper()

# for i in range(len(email)):
#     if email[i] in forbidden_word:
#         email = email.replace(email[i]," ")
# email = email.replace(" ","")
# print(email)

# #다른 풀이
# delete = "CAMBRIDGE"
# 유학 금지

# append, join 메서드 활용한 풀이
# 금지어 아닌 것들 모아서 join
delete = "CAMBRIDGE"
result = []
for w in input():
    if w not in delete:
        result.append(w)
print(''.join(result))

# 강사님 풀이
word = input()

for i in "CAMBRIDGE":
    word = word.replace(i,"")
print(word)