"""
함수의 매개 변수로 인치(inch)를 전달 받아
인치(inch)를 센치미터(cm)로 변환한 후 리턴하는 함수를 정의해보자

1(in) = 2.54(cm)

인치 입력 : 24.52
24.52 inch는 62.2808 cm 입니다.
"""

def inchToCm(inch):
    return inch * 2.54

inch_input = float(input("인치 입력 : "))
# print(inch_input, "inch는" ,"cm 입니다.")
print(f"{inch_input}inch는 {inchToCm(inch_input)}cm 입니다.")


"""
섭씨(C)를 화씨(F)로 변환하는 함수를 정의해보자.
화씨 온도(F) = (섭씨 온도(C) × 1.8) ＋ 32
=> CelToFah(celsius) 메서드 : 섭씨를 화씨로 변환한 후 리턴하는 메서드
"""
def CelToFah(celsius):
    return (celsius * 1.8) + 32

celsius = float(input("섭씨 온도 : "))
print(f"섭씨 {celsius}는 화씨 온도로 {CelToFah(celsius)} 입니다.")