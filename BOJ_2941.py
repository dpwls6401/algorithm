#다시 풀어보기
croatia_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = input()

for i in croatia_alpha:
    word = word.replace(i,"@")
print(len(word))
