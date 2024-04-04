
# n1, n2 = map(int, input("두 수 입력 : ").split())
# largeNumber : 두 수 중 큰 수를 리턴하는 함수
# large = largeNumber(n1,n2)
# print("두 수 중 큰 수는", large, "입니다.")

def largeNumber(num1, num2):
    if(num1 > num2):
        return num1
        """
        elif(num1 == num2):
        return 1
        elif(num1 != num2):
        return 0
        """
    else:
        return num2
    
def same_number(num1, num2):
    if(num1 == num2):
        return 1
    else:
        return 0

"""
def range_sum(num1, num2):
    return sum(list(range(num1, num2 + 1)))
"""

def range_sum(begin, end):
    sum = 0
    for i in range(begin, end + 1):
        sum += i
    return sum






n1, n2 = map(int, input("두 수 입력 : ").split())
large = largeNumber(n1,n2)
print("두 수 중 큰 수는", large, "입니다.")

# same_number : 두 수가 같으면 True, 다르면 False 리턴
if same_number(n1, n2):
    print("두 수는 같습니다.")
else:
    print("두 수는 다릅니다.")

# range_sum : n1부터 ~ n2 까지의 범위 합계를 구해 리턴
total = range_sum(n1, n2)

print(f"범위 합계는 {total}입니다.")
