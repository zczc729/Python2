"""
사용자로 부터 정수를 입력 받는다.
입력 받은 값이 1에서 5 사이의 정수인지 확인한 후 범위를 벗어나면 예외를 강제적으로 발생 시킨다. (raise 사용)
예외가 발생하지 않으면 입력한 값을 출력 하고, 예외가 발생한 경우는 예외 메시지를 출력한다.
"""

try :
    num = int(input("숫자 입력 : "))

    if num < 1 or num < 5 :
        raise Exception("입력 받은 숫자는 1에서 5 사이의 정수가 아닙니다.")
except Exception as exp :
    print("예외 발생 :", exp)
else :
    print("입력한 값 :", num)