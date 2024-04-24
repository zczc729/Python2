def sum(x, y):
    total = x + y
    print(f"두 수의 합은 {total} 입니다.")

def even_or_odd(num): # 매개 변수(parameter)
    if num % 2 == 0:
        print(f"{num}은(는) 짝수 입니다.")
    else:
        print(f"{num}은(는) 홀수 입니다.")

sum(3, 5) # 함수 호출
n = int(input("정수 입력 : "))
even_or_odd(n) # 함수 호출






