"""
매개 변수를 0개부터 2개까지 받을 수 있는 getTotal 함수를 정의하시오

getTotal() : 1 ~ 100 사이의 합계를 구해 리턴
getTotal(x) : x ~ 100 사이의 합계를 구해 리턴
get Total(x, y) : x ~ y 사이의 합계를 구해 리턴
"""

def getTotal(x = 1, y = 100):
    sum = 0
    for i in range(x, y + 1):
        sum += i
    return sum

print("1 ~ 100 사이의 합 :", getTotal())
print("77 ~ 100 사이의 합 :", getTotal(77))
print("20 ~ 45 사이의 합 :",getTotal(20, 45))

"""
printChar 함수를 정의하시오

printChar() : '*' 문자를 10개 출력한다.
printChar(문자, 개수) : 문자를 개수만큼 출력한다
"""
def printChar(x = '*', y = 10):
    print(x * y)

printChar()
printChar('#', 100)