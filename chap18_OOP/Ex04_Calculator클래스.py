import math

class Calculator:

    def __init__(self) : # 생성자
        print("생성자 : 인스턴스가 생성되면 자동으로 호출된다.")
        self.count = [0] * 7 # 리스트를 0으로 채워 7개를 생성한다.

    def add(self, n1, n2) :
        self.count[0] += 1 # 덧셈 횟수 증가
        return n1 + n2
    
    def sub(self, n1, n2) :
        self.count[1] += 1 # 뺄셈 횟수 증가
        return n1 - n2
    
    def mul(self, n1, n2) :
        self.count[2] += 1 # 곱셈 횟수 증가
        return n1 * n2
    
    def div(self, n1, n2) :
        self.count[3] += 1 # 나눗셈 횟수 증가
        return n1 / n2
    
    def power(self, x, y) :
        self.count[4] += 1 # 거듭제곱 횟수 증가
        return x ** y
    
    def power_of_two(self, y) :
        self.count[5] += 1 # 2의 거듭 제곱 횟수 증가
        return 2 ** y
    
    def hypot(self, base, height) :
        self.count[6] += 1 # 빗변의 길이 횟수 증가
        # 빗변의 길이 구하기
        return math.sqrt(base * base + height * height)
    
    def show_op_count(self) :
        print("\n연산 횟수 출력")
        print(f"덧셈 : {self.count[0]}회")
        print(f"뺄셈 : {self.count[1]}회")
        print(f"곱셈 : {self.count[2]}회")
        print(f"나눗셈 : {self.count[3]}회")
        print(f"거듭제곱 : {self.count[4]}회")
        print(f"2의 거듭제곱 : {self.count[5]}회")
        print(f"빗변의 길이 : {self.count[6]}회")

    
c1 = Calculator() # 인스턴스 생성
# c1.init() # 연산횟수를 카운트 할 리스트를 생성
print("덧셈 :", c1.add(2, 5))
print("곱셈 :", c1.mul(2, 5))
print("덧셈 :", c1.add(-3, -781))
print("거듭제곱 :", c1.power(10, 4))
print("2의 거듭제곱 :", c1.power_of_two(4))
c1.show_op_count()