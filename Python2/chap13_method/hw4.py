"""
▶▶ 확인문제 5

아래 리스트에서 3의 배수이면서 5보다 큰 수만 추출하여 새로운 리스트를 만들어 출력하시오.
반드시 람다함수와 filter함수를 이용하시오.

리스트는 아래와 같다.

numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 18]

"""
numList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 15, 18]

total = list(filter(lambda x : True if x % 3 == 0 and x > 5 else False, numList))
print("3의 배수이면서 5보다 큰 수 :", total)


"""
▶▶ 확인문제 6

전달된 매개변수의 곱셈 테이블을 생성하는 코드를 작성하시오.
반드시 람다함수와 map함수를 이용하시오.

람다 함수의 매개변수로 5가 전달 된 경우는 5를 1부터 10까지 곱한 리스트를 반환한다.

[5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

만약, 함수의 매개변수로 3이 전달 된 경우라면 아래와 같은 리스트를 반환한다.

[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
"""

table = int(input("정수 입력 : "))
mulTotal = list(map(lambda x : x * table, range(1, 11)))

print(f"{table}의 구구단 = {mulTotal}")




