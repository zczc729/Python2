def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def calculator(func, arg1, arg2):
    return func(arg1, arg2)
    
print(calculator(mul, 3, 5))
print(calculator(sub, 3, 5))

