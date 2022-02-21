T = int(input())

for i in range(T):
    #위치를 index로 받기
    index, word = input().split()
    index = int(index)
    changed_word = word[0:index-1] + word[index:]
    print(changed_word)

    # n,s = map(str,input().split())
    #이미 문자열인 애들이므로 str할 필요 없음
    # n = int(n)
    # print(s[:n-1] + s[n:])