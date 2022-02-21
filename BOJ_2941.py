croatia_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]
result = []

for w in input():
    if w not in croatia_alpha:
        result.append(w)
print(len(''.join(result)))