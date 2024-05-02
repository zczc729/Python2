import math

class Point:

    def __init__(self, x, y) :
        self.x = x
        self.y = y

    def show_point(self) :
        print(f"({self.x}, {self.y})")

    def get_point(self) :
        return f"({self.x}, {self.y})"
    
    def get_distance(self, other) :
        dis_x = (other.x - self.x) ** 2
        dis_y = (other.y - self.y) ** 2

        return math.sqrt(dis_x + dis_y)

p1 = Point(5, 7) # 인스턴스 생성
p2 = Point(0, 0) # 인스턴스 생성
p3 = Point(-10, -20) # 인스턴스 생성

print(f"p1과 p2 두 점의 거리는 {p1.get_distance(p2)} 입니다.") # p1과 p2의 거리를 구한다.
print(f"p2과 p3 두 점의 거리는 {p2.get_distance(p3)} 입니다.") # p2과 p3의 거리를 구한다.

# p1.show_point()
# p2.show_point()
# p3.show_point()

print(f"p1{p1.get_point()}")
print(f"p2{p2.get_point()}")
print(f"p3{p3.get_point()}")

