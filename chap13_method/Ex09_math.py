def factorial(num):
    result = 1
    for i in range(num, 1, -1):
        result *= i
        print(i, "*", end=" ")

    print("1 =", end=" ")
    return result
        
"""
def power(num1, num2):
    return pow(num1, num2)
"""

def power(x, y):
    result = 1
    for i in range(y):
        result *= x
    return result
        




base = int(input("밑 수 입력 : "))
exponent = int(input("지수 입력 : "))
# power : x ^ y를 구해 리턴하는 함수
print(f"{base}^{exponent}={power(base,exponent)}")


n = int(input("자연수 입력 : "))
# factorial : 순차곱 => n ~ 1까지 곱
print(f"{n}! = {factorial(n)}")