even_data = list(filter(lambda x : True if x % 2 == 0 else False, range(1, 30)))
print("짝수 데이터 :", even_data)

num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# filter(함수 오브젝트, 반복 가능한 애들)
# filter(함수 오브젝트, 리스트나 튜플)
# 조건에 맞는 애들만 걸러서 만들어 낸다
even_list = list(filter(lambda x : True if x % 2 == 0 else False, num_list))
print("Original List :", num_list)
print("Even List :", even_list)

# 5 이상 추출 리스트 생성
over_5 = list(filter(lambda x : True if x > 5 else False, num_list))
print("Original List :", num_list)
print("Over 5 List :", over_5)

# 3의 배수만 추출 리스트 생성
multiple_3 = list(filter(lambda x : True if x % 3 == 0 else False, num_list))
print("Original List :", num_list)
print("3의 배수 List :", multiple_3)

# [2, 4, 5, 8, 10, 14, 16, 18, 20]
# [3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
# [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]




