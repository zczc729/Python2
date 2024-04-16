try :
    weight = float(input("체중 입력(kg) : "))
    height = float(input("키 입력(cm) : "))

    height = height / 100
    bmi = weight / (height * height)
except ZeroDivisionError as exp :
    print("체중이나 키가 0이 될 수 없습니다.", exp)
except ValueError as exp :
    print(exp)
except :
    print("[예외 발생!!!]")
else : # 예외가 발생하지 않는 경우만 수행되는 명령
    if bmi < 18.5 :
        result = "마른 체형"
    elif bmi < 25 :
        result = "표준 체형"
    elif bmi < 30 :
        result = "경도 비만"
    else :
        result = "고도 비만"

    print("BMI :", bmi)
    print("판정 결과 :", result)
finally :
    print("예외 발생과 상관 없이 무조건 수행되는 명령")