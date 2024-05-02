"""
아래의 조건을 만족하는 Rgb 클래스를 정의하시오.

1. __init__ : red, green, blue의 값을 저장하는 인스턴스 속성을 private 멤버로 선언한다.
             전달 받은 매개변수로 인스턴스 속성을 초기화 한다.
2. __str__ : rgb 색상의 값을 문자열로 만들어서 리턴한다.
3. getter : red, green, blue 값을 리턴하는 메서드를 각각 정의한다.
3. setter : red, green, blue 값을 설정하는 메서드를 각각 정의한다.
"""

class Rgb:

    def __init__(self, r = 255, g = 255, b = 255):
        if 0 <= r <= 255 : # 유효성 체크
            self.__red = r
        else :
            self.__red = 255

        if 0 <= g <= 255 :
            self.__green = g
        else :
            self.__green = 255

        if 0 <= b <= 255 :
            self.__blue = b
        else :
            self.__blue = 255

    def __str__(self):
        # return f"r : {self.__red}, g : {self.__green}, b : {self.__blue}"
        return f"({self.__red}, {self.__green}, {self.__blue})"
    
    @property
    def r(self):
        return self.__red
    
    @property
    def g(self):
        return self.__green
    
    @property
    def b(self):
        return self.__blue
    
    @r.setter
    def r(self, r):
        if 0 <= r <= 255 : # 유효성 체크
            self.__red = r
        else :
            self.__red = 255

    @g.setter
    def g(self, g):
        if 0 <= g <= 255 :
            self.__green = g
        else :
            self.__green = 255

    @b.setter
    def b(self, b):
        if 0 <= b <= 255 :
            self.__blue = b
        else :
            self.__blue = 255
    
    
    # r = property(get_red, set_red)
    # g = property(get_green, set_green)
    # b = property(get_blue, set_blue)
    
    
c1 = Rgb(255, 100, 0)
print(f"c1 rgb 값 : {c1}")
# print(f"c1의 red 값은 {c1.__red} 입니다.") # error : private 멤버 접근 불가
# print(f"c1의 red 값은 {c1.get_red()} 입니다.")
print(f"c1의 red 값은 {c1.r} 입니다.") # 변수처럼 접근 가능
print(f"c1의 green 값은 {c1.g} 입니다.")
print(f"c1의 blue 값은 {c1.b} 입니다.")

c2 = Rgb(-3, 66, 7777)
# c2.__blue = 100 # 값이 변경되지 않는다.
# c2.set_blue(100)
c2.b = 100
print(f"c2 rgb 값 : {c2}")

c3 = Rgb()
print(f"c3 rgb 값 : {c3}")
