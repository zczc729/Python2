"""
▶▶ 확인문제 1

회문 판별 함수인 is_palindrome를 정의해보자. 회문이란 앞/뒤 어느쪽부터 읽어도 같은 문자열이 되는 문자열을 말한다.

[테스트 코드]는 아래와 같다.

str = input("문자열 입력: ")

# is_palindrome함수: 회문이면 True리턴, 평문이면 False리턴
if is_palindrome(str):
    print(f"{str}은(는) 회문입니다.")
else:
    print(f"{str}은(는) 평문입니다.")
"""

def is_palindrome(str):

    strList1 = list(str)                # 넘겨 받은 str을 리스트화 해서 담음
    strList2 = strList1[::-1]           # 넘겨 받은 str을 역순으로 리스트화 해서 담음

    for i in range(len(strList1)):      # strList1의 횟수 만큼 반복문을 돈다
        if strList1[i] == strList2[i]:  # strList1의 i 번째 인덱스가 strList2의 i 번째 인덱스와 같다면
            return True                 # 참
        else :                          # 아니면
            return False                # 거짓
        
def is_palindrome2(str):
    # str을 넘겨 받아 길이가 짝수인지 홀수 인지 판단
    if len(str) % 2 == 0:                       # 짝수일 경우   
        str1 = str[:int(len(str) / 2)]          # str1 문자열에 str의 0번째 부터 길이의 반인 인덱스 까지 저장
        str2 = ''                               # str3에서 나머지 반을 역순으로 받을 빈 문자열
        str3 = str[int(len(str) / 2):]          # str1에서 담고 남은 나머지를 str3에 저장
        
        for i in range(len(str3) - 1, -1, -1):  # str3에 마지막 부터, 0 번 째 까지의 정보를 str2에 저장
            str2 += str3[i]

    else :                                       # 홀수일 경우
        str1 = str[:int(len(str) / 2)]           # str1 문자열에 str의 0번째 부터 길이의 반인 인덱스 까지 저장
        str2 = ''                                # str1 길이의 정확히 반인 인덱스를 제외한 나머지 인덱스의 문자들을 담을 빈 문자열
        for i in range(                          # str의 마지막 문자 부터 길이의 반 번 째 인덱스 까지를 str2에 저장 
            len(str) - 1, 
            int(len(str) / 2), 
            -1
            ):
            str2 += str[i]
    
    if str1 == str2:                             # 위 조건식을 마친뒤 str1과 str2를 비교하여 같을 경우
        return True                              # 참
    else :                                       # 아닐 경우
        return False                             # 거짓
 
        
str = input('문자열 입력 : ')

# is_palindrome함수: 회문이면 True리턴, 평문이면 False리턴
if is_palindrome(str):
    print(f"{str}은(는) 회문입니다.")
else:
    print(f"{str}은(는) 평문입니다.")

if is_palindrome2(str):
    print(f"{str}은(는) 회문입니다.")
else:
    print(f"{str}은(는) 평문입니다.")


"""
▶▶ 확인문제 2

어느 유명 인사가 모임에서 "인생을 100점짜리로 만들기 위한 조건은 무엇일까요?"​라는 질문을 던졌다.
이 장관은 알파벳과 숫자를 연결하여 점수로 환산했다.
a는 1점, b는 2점, c는 3점, ... y는 25점, z는 26점이다.
장관은 물었다.
"열심히 일하기만 하면 될까요?"
계산을 해봤다
“열심히 일하다”의 “hard works”는 8 + 1 + 18 + 4 + 23 + 15 + 18 + 11 = 98점 이었다.​
일만 열심히 한다고 100점짜리 인생이 되는 건 아니라했다.
"지식?" knowledge는 96점
"리더쉽?" leadership은 89점
"운?"​ luck은 47점
"돈?"​ money는 72점이였다.
장관이 물었다.
"그럼 100점짜리는 인생을 만들기 위해 정말로 필요한 건 뭘까요?​“
"바로!! '마음가짐(Attitude)'입니다.​​"
인생은 마음가짐에 따라 달라진다는 말을 하고 싶었던거 같습니다^^ 

[참고 코드]

print('a') # a
print(ord('a')) # 97
print(ord('a') - 96) # 1

print('b') # b
print(ord('b')) # 98
print(ord('b') - 96) # 2

print('c') # c
print(ord('c')) # 99
print(ord('c') - 96) # 3
​
[테스트 코드]는 아래와 같다. 

word = input("100점짜리는 인생을 만들기 위해 정말로 필요한 건 뭘까요? ")

score = get_word_score(word)
print(f"{word}단어의 점수는 {score}점 입니다.")

"""

def get_word_score(word):                                                    
    sumTotal = 0                                                    # 점수 계산을 위한 변수

    if word != 'q' and word != 'Q':                                 # q/Q가 아닐 경우 계속 출력
        for i in word:
            if 'a' <= i <= 'z':                                     # 소문자 영문을 적을 경우 점수 구해주는 식 / 소문자 = 아스키 코드(97 ~  122)
                sumTotal += ord(i) - 96
            elif 'A' <= i <= 'Z':
                sumTotal += ord(i) - 64                             # 대문자 영문을 적을 경우 점수 구해주는 식 / 대문자 = 아스키 코드(65 ~ 90)
            else :                                                  # 대/소문자 영문을 입력하지 않을 경우 오류 출력
                print('\
                        [오류] 대/소문자 영문자만 입력 가능합니다.\
                        ')
                break
                
    return sumTotal                                                 # 누적합 된 점수 리턴
    

print("100점짜리는 인생을 만들기 위해 정말로 필요한 건 뭘까요?")        # 문제 출력

while True:                                                         # 종료 하기 전 까지 무한으로 단어 입력 및 점수 출력 
    word = input("종료 : q/Q\t\t\t 입력 : ")                         # 단어 입력 받기
    score = get_word_score(word)                                    # 함수 통해 점수를 받아와 변수에 저장

    if score != 0:
        if (word == 'q' and word == 'Q') and score != 0:                # 'q' / 'Q' 일 경우
            print('시스템을 종료 합니다.')                                # 종료 메세지와 함께 반복 출력 종료
            break
        if score == 100:
            print(f"\'{word}\' 단어의 점수는 {score}점 입니다.")          
            print('정답 입니다!\n인생은 마음 가짐에 따라 달라 집니다.')     # 100 점일 경우 축하 메시지 출력
            break
        else:                                                           # 'q' / 'Q'가 아닐 경우
            print(f"\'{word}\' 단어의 점수는 {score}점 입니다.")          # 단어와 점수 출력







