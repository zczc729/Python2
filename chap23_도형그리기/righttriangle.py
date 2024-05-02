# figure.py 파일(모듈)에서 Figure 클래스를 import 하겠다.
from figure import Figure

class RightTriangle(Figure):
    # 자식 클래스가 __init__을 정의하지 않을 시 부모의 __init__을 호출한다.ㄴ

    # def __init__(self, h, c):
    #     super().__init__(h, c) # 부모 생성자를 호출

    def draw(self):
        for i in range(self.height):
            print(self.ch * (i + 1))
