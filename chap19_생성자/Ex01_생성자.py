class Dummy:
    
    def __init__(self) :
        self.a = 100
        self.b = 200
        print("생성자(Constructor) : 인스턴스 생성 시 내부 적으로 호출되는 메서드")

    def show(self) :
        print(f"{self.a}, {self.b}")

d1 = Dummy() # 인스턴스 생성
d1.show()

#--------------------------------------------------------------------------------------------

class DoSomething :
    
    def __init__(self, s, c, dd) :
        self.str = s
        self.ch = c
        self.d = dd
        print("생성자(Constructor) : 인스턴스 생성 시 내부적으로 호출되는 메서드")

    def show(self) :
        print(f"str = {self.str}, ch = {self.ch}, d = {self.d}")


s1 = DoSomething('Hello World', 'R', 3.5) # 인스턴스 생성 시 값을 전달
s1.show()