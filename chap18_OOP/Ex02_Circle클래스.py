class Circle:

    # method : 클래스 내에서 정의 된 함수를 말한다.
    def init(self, rad) :
        # self로 접근하는 멤버는 instance 멤버이다.
        self.radius = rad
        self.PI = 3.141592

    def get_area(self) :
        area = self.PI * self.radius ** 2

        return area
    
    def get_round(self) :
        round = 2 * self.PI * self.radius

        return round

c1 = Circle() # Circle instance
c1.init(5)
print(f"c1 원의 넓이는 {c1.get_area()} 입니다.")
print(f"c1 원의 둘레는 {c1.get_round()} 입니다.")

c2 = Circle()
c2.init(5.2)
print(f"c2 원의 넓이는 {c2.get_area()} 입니다.")
print(f"c2 원의 둘레는 {c2.get_round()} 입니다.")
