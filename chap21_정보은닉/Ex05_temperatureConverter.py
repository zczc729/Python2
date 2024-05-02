"""
아래와 조건을 만족하는 온도 변환기 클래스(TemperatureCoverter)를 구현하시오.

1. __init__ : 섭씨의 값을 저장하는 인스턴스 속성을 private 멤버로 선언한다.
              전달 받은 매개변수로 인스턴스 속성을 초기화 한다.
              디폴트 파라미터로 구현한다. 디폴트 값은 모두 0으로 초기화한다.

2. celsius : 섭씨의 값을 리턴하는 메서드를 property 속성으로 정의하시오.
3. celsius : 섭씨의 값을 설정하는 메서드를 property 속성으로 정의하시오.
3. fahrenheit: 섭씨를 화씨로 바꿔서 리턴하는 메서드를 property속성으로 정의하시오.
               화씨 = 섭씨 * 9 / 5 + 32

4. kelvin: 섭씨를 캘빈으로 바꿔서 리턴하는 메서드를 property속성으로 정의하시오 
           캘빈 섭씨 + 273.1
"""

class TemperatureConverter:

    def __init__(self, cel):
        self.__cel = cel

    @property
    def cel(self):
        return self.__cel
    
    @cel.setter
    def cel(self, cel):
        self.__cel = cel

    @property
    def fah(self):
        return self.__cel * 9 / 5 + 32
    
    @property
    def kel(self):
        return self.__cel + 273.15
    

t1 = TemperatureConverter(36.5)

print("섭씨 :",t1.cel)
print("화씨 :", t1.fah)
print("켈빈 :",t1.kel)

