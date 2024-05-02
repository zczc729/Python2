class Trapezoid:

    def init(self, u, d, h) :
        self.u_line = u
        self.d_line = d
        self.height = h

    def get_area(self):
        area = (self.u_line + self.d_line) * self.height / 2

        return area

t1 = Trapezoid()

t1.init(3, 5, 6)
print(f"t1 사다리꼴의 넓이는 {t1.get_area()} 입니다.")

t2 = Trapezoid()

t2.init(11, 26, 7)
print(f"t1 사다리꼴의 넓이는 {t2.get_area()} 입니다.")