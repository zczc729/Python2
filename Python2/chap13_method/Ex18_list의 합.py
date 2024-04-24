def evenOrOdd(digits):
    total = 0
    for i in range(len(digit)):
        if digit[i] % 2 == 0:
            total += digit[i]
        elif digit[i] % 2 == 1:
            total -= digit[i]
    return total

def evenOrOdd2(digits):
    total = 0
    for digit in digits:
        if digit % 2 == 0:
            total += digit
        elif digit % 2 == 1:
            total -= digit
    return total

digit = [1, 2, 3, 4, 5, 6, 7, 7, 9, 14, 5, 78, 52]

# evenOrOdd 함수 : 리스트를 반복하면서 짝수면 더하고 홀수면 빼라
print("연산 결과 :",evenOrOdd(digit))
print("연산 결과 :",evenOrOdd2(digit))