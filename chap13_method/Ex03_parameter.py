"""
함수의 매개 변수로 반복 횟수를 전달 받아
반복 횟수 만큼 '*' 문자를 출력하는 함수를 정의해보자.

[출력 예]
반복 힛수 입력 : 10
"""

def print_star(count):
    print('*' * count)

def print_char(count, ch):
    print(ch * count)

n = int(input("반복 횟수 입력 : "))
ch = input("반복 문자 입력 : ")

print_star(n)
# print_char 함수 : 반복 횟수만큼 반복 문자를 출력
print_char(n, ch)

