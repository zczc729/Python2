class Human:
    def __init__(self, name = "", age = 0):
        self.__name = name
        self.__age = age
        print("부모 생성자")

    @property # getter
    def name(self):
        return self.__name
    
    @property # getter
    def age(self):
        return self.__age
    
    @name.setter # setter
    def name(self, name):
        self.__name = name

    @age.setter # setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"이름 : {self.__name} / 나이 : {self.__age}"
    
# --------------------------------------------------------------------------------------

class Student(Human): # Human 클래스 상속
    def __init__(self, no = "", major = "", na = "", ag = 0):
        super().__init__(na, ag) # 부모의 생성자를 호출
        self.__no = no
        self.__major = major
        print("자식 생성자")

    @property # getter
    def no(self):
        return self.__no
    
    @property # getter
    def major(self):
        return self.__major
    
    @no.setter # setter
    def no(self, no):
        self.__no = no

    @major.setter # setter
    def major(self, major):
        self.__major = major

    def __str__(self):
        super_data = super().__str__() # 부모의 __str__() 호출
        return f"{super_data} / 학번 : {self.__no} / 전공 : {self.__major}"
    
# --------------------------------------------------------------------------------------

s1 = Student("00072482", "컴퓨터과학과", "홍길동", 24)
print(s1)
    