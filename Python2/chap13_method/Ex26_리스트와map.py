num_list = [1, 2, 3, 4, 5]

x2 = lambda x : x * 2
x3 = lambda x : x * 3

# map 함수는 반복적인 애들을 일괄적으로 처리
# map(함수 오브젝트, 리스트 또는 튜플)
# map(mapping) : 각 요소에 함수를 적용 시켜 새로운 리스트나 튜플을 생성

x2_list = list(map(x2, num_list))
x3_list = list(map(x3, num_list))

# x3_list = list(map(lambda x : x * 3, num_list))
x4_list = list(map(lambda x : x * 4, num_list))

print("Original List :", num_list)
print("x2 List :", x2_list)
print("x3 List :", x3_list)
print("x4 List :", x4_list)

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
add_list = list(map(lambda x, y : x + y, list1, list2))

print("add List :", add_list)

str_list = ['apple', 'banana', 'apple mango']
# 문자열의 길이를 저장하는 리스트를 생성하시오. [5, 6, 11]

len_str = list(map(lambda x : len(x), str_list))

print("문자열의 길이 리스트 :", len_str)







