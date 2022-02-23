# 딕셔너리 연습 1
# style guide) "Key": "Value" => 띄어쓰기 주의!
ani = {
     "Pokemon": "Pikachu",
     "Digimon": "Agumon",
     "Yugioh": "Black Magician"
 }

word = input()
if word in ani.keys():
    print(ani[word])
else:
    print("I don't know")

# 간단한 방법
print(ani.get(word, "I don't know"))