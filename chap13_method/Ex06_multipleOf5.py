"""
함수의 매개변수로 정수를 전달 받아
5의 배수인지를 판별한 후 리턴하는 함수를 정의해 보자

[출력 예]
정수 입력 : 45
45는 5의 배수 입니다.
"""

def mul5(num):
    if num % 5 == 0:
        return 1
    else:
        return 0

n = int(input("정수 입력 : "))
if mul5(n):
    print(f"{n}은(는) 5의 배수입니다.")
else:
    print(f"{n}은(는) 5의 배수가 아닙니다.")





