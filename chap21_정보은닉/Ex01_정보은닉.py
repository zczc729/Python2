class Missile:

    # 비공개 멤버는 언더바(_)를 두 개 쓰면 된다.
    # 그러나, 멤버명 뒤에 언더바를 두 개 쓰게 되면 다시 공개된 멤버가 된다.
    def __init__(self):
        self.__password = "1234"

    def check_password(self, password) :
        if self.__password == password :
            self.__fire()
        else :
            self.__error()

    def __fire(self):
        print("미사일을 발사합니다!")

    def __error(self):
        print("[Error] 비밀번호 오류입니다.")

m1 = Missile() # 인스턴스 생성

# m1.check_password("1234")

m1.__fire