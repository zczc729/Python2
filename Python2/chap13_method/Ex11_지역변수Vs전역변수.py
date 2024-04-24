n = -3 # 전역 변수 : 어디서든 사용이 가능한 변수
       # 잘 사용하지 않는편이 좋다.
       # 여기저기 다 얽히게 되서 스파게티 코드가 되게 된다.

def doLocal():
    n = 10 # 지역 변수 : 선언된 함수 내에서만 사용 가능
    print(n)

def doLocal2():
    n = 20
    print(n)

def doGlobal():
    global n # 전역 변수 n을 사용하겠다.
    n = 1234
    print(n)

doLocal()
doLocal2()
print("전역 변수 n :",n)
doGlobal()
