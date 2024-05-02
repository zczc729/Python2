from figure import Figure
from righttriangle import RightTriangle as rt
from rectangle import Rectangle as rc

while True:
    print("\n\t\t * 그리기 마당 *")
    print("1. 직각 삼각형    2. 피라미드    3. 사각형    4. 다이아몬드    0. 종료")
    choice = int(input("메뉴 선택 : "))

    if choice == 0:
        break

    height = int(input("도형의 높이 : "))
    ch = input("출력 문자 : ")

    fi = None
    if choice == 1:
        fi = rt(height, ch)
    elif choice == 3:
        fi = rc(height, ch)

    fi.draw() # polymorphism 구현
