class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def get_x(self) :
        print("property : (x)로 메서드가 호출된다고?")
        return self.__x
    
    def get_y(self) :
        print("property : (y)로 메서드가 호출된다고?")
        return self.__y

    def get_point(self):
        return f"({self.__x}, {self.__y})"
    
    def __str__(self): # 모든 클래스에 포함된 메서드(인스턴스 출력 시 호출된다.)
        return f"({self.__x}, {self.__y})"
    
    # 속성명 = property(getter, setter)
    x = property(get_x, set_x)
    y = property(get_y, set_y)
    
p1 = Point(2, 3)
p2 = Point(100, 200)
p3 = Point(-3, 6)

# print(f"p1의 y 좌표 값은 {p1.__y}입니다.") # error : 비공개된 멤버는 접근 불가
# print(f"p1의 y 좌표 값은 {p1.get_y()}입니다.")
# print(f"p3의 x 좌표 값은 {p3.get_x()}입니다.")

print(f"p1의 y 좌표 값은 {p1.y}입니다.")
print(f"p3의 x 좌표 값은 {p3.x}입니다.")


# p2.__x = 999 # 값이 변경 되지 않는다.
# p2.set_x(999)
p2.x = 999

# p3.__y = 3000
# p3.set_y(3000)
p3.y = 3000

# print(f"p1 = {p1.get_point()}")
# print(f"p2 = {p2.get_point()}")
# print(f"p3 = {p3.get_point()}")

print(f"p1 = {p1}") # 인스턴스명을 호출시 내부적으로 __str__ 메서드가 호출된다.
print(f"p2 = {p2}")
print(f"p3 = {p3}")
