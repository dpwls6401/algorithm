#미완성!
forbidden_word = list("CAMBRIDGE")
email = input().upper()

for i in range(len(email)):
    if email[i] in forbidden_word:
        email = email.replace(email[i]," ")
email = email.replace(" ","")
print(email)