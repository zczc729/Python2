def sumOfSeveral(*args): # 가변 parameter
    pass
    total = 0
    for arg in args:
        total += arg
        # print(arg, end=" ")
    # print()
    return total

def operOfSeveral(oper, *args):
    if oper == '+':
        total = 0
        for arg in args:
            tptal += arg
    if oper == '*':
        total = 1
        for arg in args:
            total *= arg
    return total

def operOfSeveral2(*args, oper):
    if oper == '+':
        total = 0
        for arg in args:
            tptal += arg
    if oper == '*':
        total = 1
        for arg in args:
            total *= arg
    return total

print(operOfSeveral('*', 3, 4, 5))
print(operOfSeveral2(3, 4, 5, oper = '*')) # 가변 parameter 뒤에 일반 변수가 있는 경우 키워드 값으로 반드시 넘겨줘야 한다.
print("합 :",sumOfSeveral(2, 3))
print("합 :",sumOfSeveral(2, 3, 4, 5, 6, 7, 8))
print("합 :",sumOfSeveral(2, 3, 6))
print("합 :",sumOfSeveral(2, 3, 7 , 8, 9))






