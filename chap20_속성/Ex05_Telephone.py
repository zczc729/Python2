"""
연락처를 관리하는 Telephone 클래스를 아래와 같이 구현하시오.

- 인스턴스 속성(instance attribute): 번호, 이름, 연락처
- 클래스 속성(class attribute) : 연락처 개수

- 이름과 연락처는 생성자의 매개 변수로 받아 인스턴스 속성을 초기화 한다.
- 번호는 1번부터 1씩 증가되는 값으로 생성자에서 차례대로 저장한다.
- 연락처 정보를 출력하는 메서드를 인스턴스 메서드 (instance method)로 정의한다.
- 연락처 개수를 출력하는 매서드를 클래스 메서드 (class method)로 정의한다.
"""

class Telephone:
    # 클래스 속성
    count = 0

    def __init__(self, name, phone):
        Telephone.count += 1 # 전화번호 개수를 증가
        self.no = Telephone.count
        self.name = name
        self.phone = phone

    # def show_telephone_list(self):
    #     print(f"이름 : {self.name}, 연락처 : {self.phone}")

    def show_telephone_list(self):
        print(f"{self.no}. {self.name} : {self.phone}")

    @classmethod
    def get_telephone_count(cls):
        print(f"연락처 개수 : {cls.count}")

Telephone.get_telephone_count() # 연락처 개수를 출력하는 메서드
t1 = Telephone("홍길동", "010-888-9999") # 인스턴스 생성
t2 = Telephone("이순신", "017-555-4444") 
t3 = Telephone("장보고", "019-222-3333")

t1.show_telephone_list() # 연락처 출력 메소드
t2.show_telephone_list() # 연락처 출력 메소드
t3.show_telephone_list() # 연락처 출력 메소드

Telephone.get_telephone_count() # 연락처 개수를 출력하는 메소드