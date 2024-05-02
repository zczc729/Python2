class Figure:

    def __init__(self, height, ch):
        self.__height = height
        self.__ch = ch
        print("부모 생성자에서 높이와 문자를 초기화 한다.")
    
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def ch(self):
        return self.__ch

    @ch.setter
    def ch(self, value):
        self.__ch = value

    def draw(self): # 자식 클래스에서 overriding 해서 쓰도록!
        pass