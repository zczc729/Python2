class Health:

    def __init__(self, gender, height, weight):
        self.__gender = gender
        self.__height = height
        self.__weight = weight

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        self.__gender = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, value):
        self.__weight = value

class Member(Health): # Health 상속

    def __init__(self, gender, cm, kg):
        super().__init__(gender, cm, kg) # 부모의 __init__을 호출
        self.__standard_weight = 0
        self.__obesity = 0
        self.__obesity_result = ""

        self.calc_standard_weight() # 포준 체중을 계산하는 메서드를 호출
        self.calc_obesity() # 비만도 계산 메서드 호출

    def calc_standard_weight(self):
        if(self.gender == "male"):
            self.__standard_weight = (self.height - 100) * 0.9
        else:
            self.__standard_weight = (self.height - 100) * 0.85

    def calc_obesity(self):
        # 비만도 = 현재체중 / 표준체중 * 100
        self.__obesity = self.weight / self.__standard_weight * 100

        if self.__obesity <= 90 :
            self.__obesity_result = '저체중'
        elif self.__obesity <= 110:
            self.__obesity_result = '표준 체중'
        elif self.__obesity <= 120:
            self.__obesity_result = '과체중'
        elif self.__obesity <= 130:
            self.__obesity_result = '경도 비만'
        elif self.__obesity <= 150:
            self.__obesity_result = '중도 비만'
        else :
            self.__obesity_result = '고도 비만'

    def __str__(self):
        return f"표준 체중 : {self.__standard_weight:.2f} / 비만도 : {self.__obesity:.2f} / 측정 결과 : {self.__obesity_result}" 


m1 = Member("female", 162.98, 59.44)
m2 = Member("male", 184.12, 120.55)
m3 = Member("female", 172.3, 57.2)

print("m1 :", m1)
print("m2 :", m2)
print("m3 :", m3)