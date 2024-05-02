class DoSomething:

    def __init__(self):
        # 지역 변수 : 선언된 함수를 벗어나서는 사용이 불가능
        # a = 10
        # b = 20

        # 인스턴스 변수 : 인스턴스 생성 시 메모리 할당
        self.a = 10
        self.b = 20
        self.total = 0

    def show(self):
        for i in range(10) : # i는 지역변수
            print(i)
        print(f"a = {self.a}, b = {self.b}, sum = {self.total}")

    def done(self, n):
        total = 20 * n
        return total

d1 = DoSomething() # 인스턴스 생성
d2 = DoSomething() # 인스턴스 생성

d1.show()
d2.show()