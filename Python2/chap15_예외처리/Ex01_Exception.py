try : 
    num1 = int(input("첫 번 째 수 입력 : "))
    num2 = int(input("두 번 째 수 입력 : "))

    result = num1 / num2
    print("나눗셈 결과 :", result)

    dm = divmod(num1, num2)
    print(f"몫 : {dm[0]}, 나머지 : {dm[1]}")
except ZeroDivisionError as exp:
    print("0으로 나눌수 없습니다.", exp)
except ValueError as exp:
    print("숫자만 입력 할 수 있습니다.", exp)
except :
    print("그 밖에 예외는 여기서 처리된다")
finally : # 예외 발생과 상관 없이 무조건 실행되는 명령
    print("예외 발생과 상관 없이 무조건 실행되는 명령")