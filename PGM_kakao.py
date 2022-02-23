def solution(s):
    # 1. 숫자 영단어 테이블을 딕셔너리로 정의
    number = {"zero": '0',
              "one": '1',
              "two": '2',
              "three": '3',
              "four": '4',
              "five": '5',
              "six": '6',
              "seven": '7',
              "eight": '8',
              "nine": '9'}
    
    # 2. 문자열에서 영어 -> 숫자
    # 딕셔너리 기준으로 for 돌리기
    for key, value in number.items():
        s = s.replace(key, value) #s에서 key 글자를 value로 바꿀거야
        
    # 3. 바뀐 숫자를 출력
    return int(s)