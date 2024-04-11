"""
문제 1

섭씨(C)를 화씨(F)로 변환하는 함수를 정의해보자.
화씨 온도(F) = (섭씨 온도(C) × 1.8) ＋ 32
=> CelToFah(celsius) 메서드 : 섭씨를 화씨로 변환한 후 리턴하는 메서드

실행 예)
섭씨 입력 : 100
섭씨 100도 -> 212도
"""

def CelToFah(celsius):
    return (celsius * 1.8) + 32

temp = int(input("섭씨 입력 : "))

if int(CelToFah(temp)) == CelToFah(temp): # temp에서 CelToFah 함수로 넣은뒤 return 값이 정수일 경우 소숫점 제거하여 정수로 출력
    print("화씨 : ", int(CelToFah(temp)), "도")
else: # 아닐경우 소수점 표시하여 실수로 출력
    print("화씨 : ", CelToFah(temp), "도")



"""
문제 2

전달하는 매개변수의 개수와 상관없이 최댓값을 구해 리턴하는 함수를 정의해 보시오. 

(가변 파라미터 이용 - 리스트나 튜플 사용 불가)

실행 예)
3개의 정수 입력 (공백 구분) : 3 5 7
최댓값은 7 입니다.

실행 예)
정수 입력 (공백 구분) : 3 255 7 9 2 18
최댓값은 255 입니다.
"""


def maxNum(*args):
    args = map(int, input("숫자 입력 : ").split())
    return max(args)

print("최댓값은", maxNum(),"입니다.")


"""
문제 3
 
리스트에 1 ~ 100사이의 수를 랜덤하게 100개 저장한 후 시작 수와 끝 수 사이의 수만 출력하는 코드를 작성해보자.

[출력 예]
시작 수 입력 : 90
끝 수 입력 : 99
*** 90 ~ 99 범위의 랜덤 값 출력 ***
92 90 97 96 92 91

"""

import random

randomNum = [] # 1 ~ 100까지 랜덤한 숫자를 담을 빈 리스트
randomNumPopOut = [] # 위 리스트에서 조건에 부합하는 숫자들을 담을 리스트

for i in range(0, 100):
    randomNum.append(random.randrange(1, 100)) # 1 ~ 100까지 랜덤한 숫자를 반복문으로 담기
    randomNum.sort() # 작은 수 ~ 큰 수로 정렬

def randomNumPop(num1, num2):
    if num2 < num1: # 끝 수가 시작 수 보다 작으면 값이 출력되지 않게 조건문 작성
        print("끝 수가 시작 수 보다 작습니다.")
    else:
        for i in range(len(randomNum)):
            if num1 <= randomNum[i] <= num2: # 시작수 이상 끝 수 이하일 경우
                randomNumPopOut.append(randomNum[i]) # 새로운 리스트에 추가
                randomNumPopOut.sort() # 정렬
        return randomNumPopOut # 새로운 값을 담은 리스트 return


n1 = int(input("시작 수 입력 : "))
n2 = int(input("끝 수 입력 : "))
n3 = len(randomNumPopOut)
listRan = randomNumPop(n1,n2) # 할 필요 없지만, 갯수가 몇 개 인지 알려주기 위해 따로 변수 설정
if n1 < n2:
    print(f"{n1}과 {n2} 사이의 랜덤 값 개수는 {len(randomNumPopOut)}개 이고, 값은 다음과 같습니다.","\n", listRan)


"""
문제 4

아래 리스트에서 3의 배수이면서 5보다 큰 수만 추출하여 새로운 리스트를 만들어 출력하시오.
반드시 람다함수를 이용하시오.

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 18]
"""

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 18]
    
newList = list(filter(lambda x : x % 3 == 0 and 5 < x, numList))
number1 = len(newList) # 리스트의 개수를 세기 위한 변수 지정
print(f"numList 리스트에서 3의 배수이면서 5보다 큰 수는 {number1}개 이고 값은 다음과 같습니다.\n",newList)


    







