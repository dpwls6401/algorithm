##1. replace 이용 - 한글자로 '수정'
# 'z='이 'dz=' 보다 먼저 인식되면 안되므로 순서 맨 뒤로!
croatia_alpha = ["c=","c-","dz=","d-","lj","nj","s=","z="]
word = input()

#굳이 index로 range 돌려서 접근하지 않아도 됨! 가독성 위함
for i in croatia_alpha:
    word = word.replace(i,"@")
print(len(word))

##2. count 이용 - 한글자로 '인식'
word = input()
#'dz='는 3글자이므로 한번 더 빼줘야 함
croatia_alpha = ['=','-','lj','nj','dz=']
total = len(word)

for c in croatia_alpha:
    total -= word.count(c) #전체 문자열 길이에서 빼주는 것
print(total)
