class MyMath:
    # 메서드에 첫 번 째 매개변수로 self를 쓰지 않으면, 무조건 정적(static) 메서드이다.
    # 정적 메서드임을 명확하게 하기 위해 @staticmethod를 쓰는 것을 권장한다.(가독성이 높아짐)

    PI = 3.141592

    @staticmethod
    def factorial(n) :
        result = 1
        for i in range(n, 0, -1) :
            result *= i
        return result # 순차곱의 결과를 리턴
    
    @staticmethod
    def is_prime(n) :
        # 소수란? 1보다 큰 자연수중 1과 자신만을 약수로 갖는 수
        if n <= 1 :
            return False
        elif n == 2 :
            return True
        elif n % 2 == 0 : # 2의 배수인 경우? 합성수
            return False
        
        for i in range(3, n, 2) : # 3보다 큰 홀수만 반복
            if n % i == 0 : # 나누어 떨어지는 수가 존재하면?
                return False
            
        return True
    
print(f"5! =", MyMath.factorial(5))
print(f"121은 소수 입니까?",MyMath.is_prime(121))