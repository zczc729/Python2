def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

# 변수에 함수를 대입 할 수 있음

func = mul
print(mul(3, 5))
print(func(3, 5))

func = sub
print(sub(3, 5))
print(func(3, 5))


