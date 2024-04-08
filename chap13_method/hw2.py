"""
전달하는 매개변수의 개수와 상관없이 최댓값을 구해 리턴하는 getMax함수를 정의해보자.

(가변 파라미터 이용)

테스트 코드는 아래와 같다.

n1, n2, n3 = map(int, input("3개의 정수 입력(공백 구분): ").split())
getMax(n1, n2, n3)

n1, n2, n3, n4, n5 = map(int, input("5개의 정수 입력(공백 구분): ").split())
getMax(n1, n2, n3, n4, n5)
"""

def getMax(*args):
    total = 0
    for i in args:
        total += i
    return total

n1, n2, n3 = map(int, input("3개의 정수 입력(공백 구분): ").split())
print(f"{n1} + {n2} + {n3} = {getMax(n1, n2, n3)}")


n1, n2, n3, n4, n5 = map(int, input("5개의 정수 입력(공백 구분): ").split())
print(f"{n1} + {n2} + {n3} + {n4} + {n5} = {getMax(n1, n2, n3, n4, n5)}")

"""
다이아몬드, 직사각형 그리기
"""

def diamomd(height): # 삼각형을 그린뒤 해당 값을 뒤집으면 해결
    for i in range(1, height + 1): # 1 ~ 입력받은 높이값 까지 출력
        print(' ' * (height - i), end="") # 먼저 공백 출력
        print('*' * (2 * i - 1)) # 그다음 별 출력
    for j in range(height - 1, 0, -1): # 입력 받은 높이값 부터 출력 하면 가운데 2부분이 2번 출력 되므로 높이값 - 1 부터 0 까지 1개씩 빼기
            print(' ' * (height - j), end="") # 공백 먼저 출력
            print('*' * (2 * j - 1))  # * 출력
    print()

def rectangle(height): 
    for i in range(height):
        print('* ' * height) # 붙혀서 나오면 안이뻐서 공백 추가
    print()