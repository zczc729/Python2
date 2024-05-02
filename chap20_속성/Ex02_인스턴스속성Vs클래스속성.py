class Dummy:
    # 클래스 속성
    # my_list = []

    def __init__(self):
        self.my_list = [] # 인스턴스 속성으로 리스트 생성

    def add(self, n):
        # Dummy.my_list.append(n)
        self.my_list.append(n)

    def show_list(self):
        # print(Dummy.my_list)
        print(self.my_list)

d1 = Dummy() # 인스턴스 생성
d1.add(1)
d1.add(2)
d1.add(3)
d1.add(4)
d1.add(5)


d2 = Dummy() # 인스턴스 생성
d2.add('A')
d2.add('B')
d2.add('C')
d2.add('D')
d2.add('E')


d3 = Dummy() # 인스턴스 생성
d3.add(1.1)
d3.add(2.2)
d3.add(3.3)

d1.show_list()
d2.show_list()
d3.show_list()