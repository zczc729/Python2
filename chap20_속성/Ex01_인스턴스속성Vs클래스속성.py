class MyClass:
    # 클래스 변수(속성) : 클래스내에서 선언된 변수
    # 클래스 정의 시 딱 한 번 만 메모리가 할당된다.(인스턴스마다 각각 할당 되는 것이 아니다.)
    # 마치 모든 인스턴스가 공유하는 것처럼 사용 할 수 있다.
    # 클래스 변수는 클래스 명으로 접근 할 수 있다.
    n = 0

    def __init__(self, a, b):
        # 인스턴스 변수 (속성) : self로 선언된 변수
        self.a = a
        self.b = b
        print("[생성자] 매개변수를 전달받아 초기화")

    def set_n(self, num):
        # n = num # set_n 매서드에서만 사용 가능한 지역번수에 저장
        MyClass.n = num # 클래스 변수에 접근 시 반드시 클래스명으로 접근한다.

    def show(self):
        print(f"a = {self.a}, b = {self.b}, n = {MyClass.n}")

m1 = MyClass(2, 3) # 인스턴스 생성
m2 = MyClass(100, 200)
m3 = MyClass(-10, -20)

m1.set_n(-3)
m2.set_n(9999)
m2.set_n(-5)

m1.show()
m2.show()
m3.show()