def f_add(a, b):
    return a + b

# 익명 함수 : 이름이 없는 함수
# 람다 함수는 함수의 이름이 없는 익명 함수
# 변수 = lambda 매개변수: 구현
add = lambda a, b : a + b

print(f_add(3, 5))
print(add(3, 5))

def f_square(x):
    return x ** 2

square = lambda x: x ** 2

print(f_square(5))
print(square(5))

def getTriangleArea(base, height):
    return base * height / 2

tArea = lambda base, height: base * height / 2

print(getTriangleArea(3, 5))
print(tArea(3, 5 ))

def f_is_even(num):
    if num % 2 == 0:
        return True
    else : 
        return False
    
is_even = lambda num : True if num % 2 == 0 else False
is_odd = lambda num : True if num % 2 != 0 else False

mul = lambda num1, num2 : num1 * num2
sub = lambda num1, num2 : num1 - num2

def calculator(func, arg1, arg2):
    return func(arg1, arg2)

cal = lambda func, arg1, arg2 : func(arg1, arg2)

print("짝수냐 ? ", f_is_even(10))
print("짝수냐 ? ", is_even(10))
print("홀수냐 ? ", is_odd(10))
print("곱셈 결과 :", mul(3, 5))
print("뺄셈 결과 :", sub(3, 5))
print("곱셈 결과 :", calculator(lambda a, b: a * b, 3, 5)) # 람다 함수를 직접 전달
print("뺄셈 결과 :", calculator(lambda a, b : a - b, 3, 5))
print("곱셈 결과 :", cal(mul, 3, 5))
print("뺄셈 결과 :", cal(sub, 3, 5))






