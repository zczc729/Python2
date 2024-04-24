# 삼각형 객체 => 객체를 생성하기 위한 틀(클래스)

class Triangle:
    # 변수
    # base = 0
    # height = 0

    # 함수 => method
    # 클래스내에서 선언된 함수를 메서드라 한다.
    # 메서드의 첫 번 째 매개변수로 반드시 self를 받아야 한다.
    def init(self, b, h) :
        # self로 접근하는 변수는 클래스 내의 변수
        self.base = b
        self.height = h

    def get_area(self):
        area = self.base * self.height / 2

        return area

t1 = Triangle() # 객체 생성 => Triangle 인스턴스(instance/객체) 생성

t1.init(3, 5)
print(f"t1 삼각형의 넓이는 {t1.get_area()} 입니다.")

t2 = Triangle()  # Triangle 인스턴스(instance/객체) 생성

t2.init(20,15)
print(f"t2 삼각형의 넓이는 {t2.get_area()} 입니다.")