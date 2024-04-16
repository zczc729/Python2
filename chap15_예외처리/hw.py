"""
▶▶ 확인문제 1
​
덧셈. 뻴셈. 곱셈. 나눗셈 함수를 각각 정의한 후 모듈로 만든다.
모듈을 import한 후 각각의 함수를 사용해보자.
"""

import calculator

n1 = int(input("첫 번 째 숫자 입력 : "))
n2 = int(input("두 번 째 숫자 입력 : "))

print("\t\t*** 결과 ***")
print(f"{n1} + {n2} = {calculator.plus(n1, n2)}")
print(f"{n1} - {n2} = {calculator.minus(n1, n2)}")
print(f"{n1} X {n2} = {calculator.multiple(n1, n2)}")
print(f"{n1} / {n2} = {calculator.division(n1, n2)}")

"""
▶▶ 확인문제 1
① 문자열을 입력 받는다.
② 교환 횟수를 입력 받아 횟수만큼 역순으로 교환한다. (교환 횟수의 유효 범위: 0 ~ 문자열의 길이 / 2)
③ 교환 횟수가 범위를 벗어난 경우 강제적으로 예외를 발생 시킨다.
​
[출력 예
문자열 입력: Hello World
교환 횟수: 4
​
출력 결과: dlroo WlleH
​
[출력 예
문자열 입력: Hello World
교환 횟수: 80
​
1 ~ 5 사이의 교환 횟수를 입력 해주세요.
"""
user_str = input("문자열 입력 : ")
user_int = int(input("교환 횟수 : "))
str1 = ""
str2 = ""

try:
    if user_int > int(len(user_str)) :
        raise Exception(f"1 ~ {int(len(user_str) / 2)} 사이의 교환 횟수를 입력 해주세요.")
    else : # Hello World -> 11글자
        str1 = list(user_str)
        str2 = str1[::-1]

        for i in range(user_int) :
            str1[i] = str2[i]
            str1[(i + 1) * -1] = str2[(i + 1) * -1]
        str1 = ''.join(str1)

        print(f"출력 결과 : {str1}")
except Exception as exp:
    print(exp)
