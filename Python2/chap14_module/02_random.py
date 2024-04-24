# from random import randint
# # import random

# print(randint(1, 100))
# # print(random.randint(1, 100))

from random import randint

def user_choice():
    
    while True: # 1, 2, 3 중 한 개를 선택하기 위한 반복문
        user = int(input("\n가위 (1) | 바위 (2) | 보 (3) 중 하나를 선택하세요 : "))
        if user in [1, 2, 3]:
            return user # 입력 값 리턴
        else :
            print("잘못된 입력 입니다. 1, 2, 3 중 하나를 선택해 주세요.")

def determine_winner(user, computer):
    determine = (computer - user + 3) % 3

    if determine == 0:
        return "비겼다!"
    elif determine == 1:
        return "computer 승!"
    else :
        return "user 승!"

while True:
    # 1. 가위, 2. 바위, 3. 보
    computer = randint(1, 3)
    user = user_choice()

    rsp = ["", "가위", "바위", "보"] # 문자열을 출력하기 위한 리스트

    print(f"\n[user] : {rsp[user]}, [computer] : {rsp[computer]} => {determine_winner(user, computer)}")

    while True: # yes or no만 받기 위한 반복문
        play_again = (input("\n\t 한 판 더 하시겠습니까? (yes or no) : ")).lower()

        if play_again in ["yes", "no"] :
            break
        else :
            print("\t잘못 입력 하셨습니다. 다시 입력해주세요.")

    if play_again == "no" :
        print("\n\t가위 바위 보 게임을 종료 합니다.")
        break # 전체 반복문을 탈출
    
























