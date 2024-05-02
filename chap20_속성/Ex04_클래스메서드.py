class Point:
    # 클래스 변수 : 인스턴스가 공유한다.
    count = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.count = 0
        Point.count += 1 # 클래스 속성에 접근
    
    def get_point(self):
        return f"({self.x}, {self.y})"
    
    @classmethod
    def show_point_count(cls):
        print(f"생성된 자표의 개수는 {cls.count}개 입니다.")
    
p1 = Point(2, 3)
p2 = Point(10, 20)
p3 = Point(-3, 6)
p4 = Point(-100, -200)

# 클래스 속성에 접근 시 클래스명으로 접근하는 것이 일반적이다.
# print(f"생성된 자표의 개수는 {Point.count}개 입니다.")
# p1.show_point_count() # 메서드는 인스턴스에서만 호출 가능함
Point.show_point_count() # 클래서 메서드는 클래스명으로 호출 할 수 있다

print("p1", p1.get_point())
print("p2", p2.get_point())
print("p3", p3.get_point())
print("p4", p4.get_point())
