"""
▶▶ 확인문제 1

상품 정보를 관리하는 클래스를(Product) 아래와 같이 구현하시오.

인스턴스 속성(instance attribute): 일련번호, 상품명, 제조사, 가격

- 상품명, 제조사, 가격은 생성자의 매개 변수로 받아 인스턴스 속성을 초기화한다.
- 일련번호는 1200번부터 1씩 증가되는 값으로 생성자에서 차례대로 저장한다.
- 상품  정보를 출력하는 메서드를 인스턴스 메서드(instance method)로 정의한다.
- 상품 개수를 출력하는 메서드를 클래스 메서드(class method)로 정의한다.

[실행 예]

[상품 리스트​]
1200.    새우깡      농심(주)        1900원
1201.    빼빼로      롯데제과       2200원
1202.    먹태깡      농심(주)        2500원 
---------------------------------------------
총 상품 개수: 3개
"""

class Product:
    count = 0

    def __init__(self, name, brand, price):
        self.name = name
        self.brand = brand
        self.price = price
        self.num = Product.count + 1200
        Product.count += 1

    def show_product_list(self):
        print(f"{self.num}. \t{self.name}\t\t{self.brand}\t{self.price}")

    @classmethod
    def show_count(cls):
        print(f"총 상품 개수 : {cls.count}")


p1 = Product('새우깡', '농심(주)', '1900원')
p2 = Product('빼빼로', '롯데제과', '2200원')
p3 = Product('먹태깡', '농심(주)', '2500원')

print("[상품 리스트]")
p1.show_product_list()
p2.show_product_list()
p3.show_product_list()
print("---------------------------------------------------")
Product.show_count()
    

"""
▶▶ 확인문제 2

도형 클래스(Shape)를 아래와 같이 구현하시오.

원의 넓이를 계산하는 정적 메서드는 반지름을 매개변수로 받아서 원의 넓이를 리턴한다.
원의 둘레를 계산하는 정적 메서드는 반지름을 매개변수로 받아서 원의 둘레를 리턴한다.
삼각형의 넓이를 계산하는 정적 메서드는 밑변과 높이를 매개변수로 받아서 삼각형의 넓이를 리턴한다.
삼각형의 둘레를 계산하는 정적 메서드는 세 변의 길이를 매개변수로 받아서 삼각형의 둘레를 리턴한다.
삼각형의 빗변의 길이를 계산하는 정적 메서드는 밑변과 높이를 매개변수로 받아서 삼각형의 빗변의 길이를 리턴한다.
사각형의 넓이를 계산하는 정적 메서드는 가로와 세로를 매개변수로 받아서 사각형의 넓이를 리턴한다.
사각형의 둘레를 계산하는 정적 메서드는 가로와 세로를 매개변수로 받아서 사각형의 둘레를 리턴한다.
"""

class Shape:
    PI = 3.141592

    @staticmethod
    def area_round(n) :
        return f"반지름이 {n}인 원의 넓이 : {Shape.PI * (n * n)}"
    
    @staticmethod
    def perimeter_round(n) :
        return f"반지름이 {n}인 원의 둘레 : {2 * Shape.PI * n}"
    
    @staticmethod
    def area_triangle(under, heigth):
        return f"밑변이 {under} 높이가 {heigth}인 삼각형의 넓이 : {under * heigth / 2}"    
    
    @staticmethod
    def perimeter_triangle(n1, n2 ,n3):
        return f"첫 번 째 변이 {n1}, 두 번 째 변이 {n2}, 세 번 째 변이 {n3}인 삼각형의 둘레 : {n1 + n2 + n3}"
    
    @staticmethod
    def area_square(width, length):
        return f"가로가 {width}, 세로가 {length}인 사각형의 넓이 : {width * length}"
    
    @staticmethod
    def perimeter_square(width, length):
        return f"가로가 {width} 세로가{length}인 사각형의 둘레 : {(width + length) * 2}"
    
print(Shape.area_round(5))
print(Shape.perimeter_round(5))
print(Shape.area_triangle(3, 5))
print(Shape.perimeter_triangle(5, 10, 7))
print(Shape.area_square(10, 6))
print(Shape.perimeter_square(6, 7))