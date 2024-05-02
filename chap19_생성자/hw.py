from random import randint

class Rsp:

    def __init__(self) :
        while True:
            self.rsp = [1, 2, 3]
            self.rsp_list = ['가위', '바위', '보']

            print("\t\t*** 가위 바위 보 게임 ***")
            print("\n가위 (1) / 바위 (2) / 보 (3)")
            self.user_in = int(input("당신의 선택 : "))
            self.com_in = self.rsp[randint(0, 2)]

            print("컴퓨터 :",self.rsp_list[int(self.com_in) - 1])
            print("당 신 :", self.rsp_list[int(self.user_in) - 1])

            if self.user_in == self.com_in :
                print("\t[비겼다]")
            elif (self.user_in == 1 and self.com_in == 3) or (self.user_in == 2 and self.com_in == 1) or (self.user_in == 3 and self.com_in == 1):
                print("\t[이겼다]")
            elif (self.user_in == 1 and self.com_in == 2) or (self.user_in == 2 and self.com_in == 3) or (self.user_in == 3 and self.com_in == 1) :
                print("\t[졌다]")

            self.again = input("\t한 판 더(Y/y) / 종료 (아무키)")

            if self.again not in "yY" :
                break
            else:
                continue

            



r = Rsp()