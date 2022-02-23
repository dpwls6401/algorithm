# 리스트 Q&A
#문자열이 덩어리처럼 보이지만 사실은 하나하나 인덱싱 되어 연속적으로 붙어 있는 것!
word = "abcdefg"
dic = {1, 2, 3}

a = list(word) #문자열 각 원소가 리스트가 되도록 바꿔라
a2 = list(dic) #{} 벗겨내고 리스트로 만들어라
a3 = list(map(int, input().split()))

b = [word] #그냥 통째로 넣겠다
b2 = [dic] #딕셔너리를 그대로 리스트에 넣어라
b3 = [map(int, input().split())] #map이 반환하는 걸 통으로 리스트에 넣겠다

print(a)
print(b)