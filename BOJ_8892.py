T = int(input())
words = int(input())

for i in range(T):
    for j in range(words):
        word = input()

        palindrome = word[j].join(word[j:j+words])

    if palindrome == palindrome[::-1]:
        print(palindrome)
    else:
        print("0")