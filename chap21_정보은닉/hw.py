"""
▶▶ 확인문제 1

아래의 조건을 만족하는 학생 성적 클래스(StudentScore)​를 구현하시오.

1. __init__: 학번, 이름, 자료구조 점수, 알고리즘 점수, Java점수, 총점 평균의 값을 저장하는 인스턴스 속성을 private멤버로 선언한다.
              학번, 이름, 자료구조 점수, 알고리즘 점수, Java점수는 전달받은 매개변수로 인스턴스 속성을 초기화 한다.
              총점, 평균과 등급은 생성자내에서 연산한다.
              디폴트 파라미터로 구현한다. 문자열인 경우 빈 문자열("")로 초기화하고, 점수는 0으로 초기화 한다.

             - 총점 = 자료구조 점수 + 알고리즘 점수 + Java점수
             - 평균 = 총점 / 3
             - 등급 계산 방법은 아래와 같다.
               평균이 100 ~ 90 : A등급, 89 ~ 89 : B등급, 79 ~ 70 : C등급 , 69 ~ 60 : D등급, 그 외 점수는 : F등급이다.

             - 유효성 체크 기준은 아래와 같다.
               학번 길이: 13자리 고정
               이름 길이: 2 ~ 20글자
               각 과목의 점수: 0 ~ 100점

2. 학생 정보 출력 메서드: 학생 정보를 출력한다.
3. getter: property데코레이터를 이용해서 정의한다.
4. setter: property데코레이터를 이용해서 정의한다. => 생성자에서 주어진 조건을 기준으로 유효성을 체크한다.
"""

class StudentScore:

    def __init__(self, num = "", name = "", d_score = 0, a_score = 0, j_score = 0):
        if len(num) == 13:
            self.__num = num
        
        if 2<= len(name) <= 20:
            self.__name = name

        if 0 <= d_score <= 100:
            self.__d_score = d_score
        else :
            self.__d_score = 0
            
        if 0 <= a_score <= 100:
            self.__a_score = a_score
        else :
            self.__a_score = 0

        if 0 <= j_score <= 100:
            self.__j_score = j_score
        else :
            self.__j_score = 0

        self.__total = self.__d_score + self.__a_score + self.__j_score
        self.__avg = self.__total / 3

        if 90 <= self.__avg <= 100 :
            self.__grade = 'A'
        elif 80 <= self.__avg < 90 :
            self.__grade = 'B'
        elif 70 <= self.__avg < 80 :
            self.__grade = 'C'
        elif 60 <= self.__avg < 70 :
            self.__grade = 'D'
        else :
            self.__grade = 'F'
    
    def show_student_info(self):
        print(f"학번 : {self.__num}\n\
이름 : {self.__name}\n\
자료 구조 점수 : {self.__d_score}\n\
알고리즘 점수 : {self.__a_score}\n\
JAVA 점수 : {self.__j_score}\n\
평균 : {self.__avg}\n\
등급 : {self.__grade}")

    def set_num(self, num):
        if len(num) == 13:
            self.__num = num

    def set_name(self, name):
        if 2<= len(name) <= 20:
            self.__name = name

    def set_d_score(self, d_score):
        if 0 <= d_score <= 100:
            self.__d_score = d_score
        else :
            self.__d_score = 0

    def set_a_score(self, a_score):
        if 0 <= a_score <= 100:
            self.__a_score = a_score
        else :
            self.__a_score = 0

    def set_j_score(self, j_score):
        if 0 <= j_score <= 100:
            self.__j_score = j_score
        else :
            self.__j_score = 0

    def set_num(self, num):
         if len(num) == 13:
            self.__num = num

    def set_num(self, num):
         if len(num) == 13:
            self.__num = num

    def get_num(self):
        return self.__num
    
    def get_name(self):
        return self.__name
    
    def get_d_grade(self):
        return self.__d_score
    
    def get_a_grade(self):
        return self.__a_score
    
    def get_j_score(self):
        return self.__j_score
        

s1 = StudentScore("1234567890123", "홍길동", 70, 80, 90)
s1.show_student_info()

print()

s2 = StudentScore("Ab82057186123", "외자", 80, 100, 100)
s2.show_student_info()