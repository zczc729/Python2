# 키워드값으로 딕셔너리(key-value)를 만든다
def print_kwargs(**kwargs): 
    print(kwargs)

print_kwargs(name = "홍길동")
print_kwargs(name = "홍길동", age = 18)
print_kwargs(name = "홍길동", age = 24, gender = "male")







