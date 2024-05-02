"""
아래의 조건을 만족하는 Score 클래스를 디자인 해보자.

멤버 변수 : 이름, 국어점수, 영어점수, 총점, 평균, 등급을 구한다.
"""


class Score:
    grade = ''

    def init(self, name, korean, english, math) :
        self.name = name
        self.korean = korean
        self.english = english
        self.math = math
        self.avg = (self.korean + self.english + self.math) / 3
        self.getGrade()

    def getGrade(self):
        if 90 <= self.avg <= 100 :
            self.grade = 'A'
        elif 80 <= self.avg < 90 :
            self.grade = 'B'
        elif 70 <= self.avg < 80 :
            self.grade = 'C'
        elif 60 <= self.avg < 70 :
            self.grade = 'D'
        else :
            self.grade = 'F'
        
        return self.grade

    def showScore(self) :
        print(f"{self.name} 님의 평균 : {self.avg:.2f} => {self.grade} 등급")
    
student1 = Score()
student1.init('홍길동', 90, 85, 75)
student1.showScore()