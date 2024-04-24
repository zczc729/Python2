import sys


def rightTriangle(height):
    for i in range(1, height + 1):
        print('*' * i)
    print()

def pyramid(height):
    pass # 지금 당장 구현하지 않고 틀만 만들어 놓은 후 나중으로 미룬다.
    for i in range(1, height + 1):
        print(' ' * (height - i), end="")# 공백
        print('*' * (2 * i - 1))# *
    print()

# 과제 1)
def diamomd(height):
    pass
    for i in range(1, height + 1):
        print(' ' * (height - i), end="")
        print('*' * (2 * i - 1))
    for j in range(height - 1, 0, -1):
            print(' ' * (height - j), end="")
            print('*' * (2 * j - 1))  
    print()

def rectangle(height):
    for i in range(height):
        print('* ' * height)
    print()

while True:
    print("\n\n\t\t * 그리기 마당 * ")
    print("1. 직각 삼각형   2. 피라미드     3. 다이아몬드   4. 사각형   0. 프로그램 종료")
    choice = int(input("메뉴 선택 : "))

    if choice == 0:
        sys.exit("프로그램을 종료합니다.")

    
    height = int(input("높이 입력 : "))

    if choice == 1:
        rightTriangle(height)
    elif choice == 2:
        pyramid(height)
    elif choice == 3:
        diamomd(height)
    else:
        rectangle(height)










