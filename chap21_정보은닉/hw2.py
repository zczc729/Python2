"""
[Human 클래스]
- 인스턴스 속성: 이름, 나이
- setter, getter를 property데코레이터로 구현한다.
- __str__내장함수를 이름과 나이를 리턴하도록 구현한다.

[Student 클래스]
- 인스턴스 속성: 학번, 전공
- setter, getter를 property데코레이터로 구현한다.
- __str__내장함수를 학번과 전공을 리턴하도록 구현한다.
"""

class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"이름 : {self.__name} 나이 : {self.__age}"
    
class Student:

    def __init__(self, no, major):
        self.__no = no
        self.__major = major

    @property
    def no(self):
        return self.__no
    
    @no.setter
    def no(self, no):
        self.__no = no

    @property
    def major(self):
        return self.__major
    
    @major.setter
    def major(self, major):
        self.__major = major

    def __str__(self):
        return f"학번 : {self.__no} 전공 : {self.__major}"