#my
# forbidden_word = list("CAMBRIDGE")
# email = input().upper()

# for i in range(len(email)):
#     if email[i] in forbidden_word:
#         email = email.replace(email[i]," ")
# email = email.replace(" ","")
# print(email)

#다른 풀이
delete = "CAMBRIDGE"
result = []
for w in input():
    if w not in delete:
        result.append(w)
print(''.join(result))