def get_max(nums):
    max = nums[0] #  첫 번 째 요소를 최대값으로 설정
    for i in range(1, len(nums)):
        if max < nums[i]:
            max = nums[i]
    return max 

def get_min(nums):
    min = nums[0] # 첫 번 째 요소를 최소값으로 설정
    for i in range(1, len(nums)):
        if min > nums[i]:
            min = nums[i]
    return min

nums = [55, 25, 2, 12, 272, 243, 23, 12, 62, 95, 12, 415, 1, 99, 100, 12, 500, 103, 12, 12, 12]

# print_range(begin, end) 함수 : begin 부터 end 보다 작은 수만 출력
def print_range(nums, begin, end):
    print(f'{begin} 이상 {end} 미만 : ', end='')

    # for i in range(len(nums)): # 첫 번 째 ~ 마지막 인덱스 까지 반복
    #     if begin <= nums[i] and nums[i] < end:
    #         print(nums[i], end=' ')

    for num in nums: # 리스트의 각 요소의 값을 저장해서 반복
        if begin <= num < end:
            print(num, end=' ')
    print()
    
def get_less_list(nums, num1):
    list_nums = []
    for num in nums:
        if num < num1:
            list_nums.append(num)
    list_nums.sort()
    return list_nums

def get_range_list(nums, begin, end):
    listTotal = []
    for num in nums:
        if begin <= num < end:
            listTotal.append(num)
    listTotal.sort()
    return listTotal

def get_remove_value_list(nums, deleteNum):
#     case 1. 삭제할 데이터가 아닌 경우에 리스트에 추가
    temp = []
    for num in nums:
        if num != deleteNum:
            temp.append(num)
    return temp

#     case 2. 리스트 복사 후 삭제할 값 제거
#     temp = nums[::] # 리스트 복사
#     print('len : ',len(temp))
#     print('temp :',temp)
#     for var in temp:
#         if var == deleteNum:
#             temp.remove(deleteNum)
#     return temp



print_range(nums, 100, 500)

less_nums = get_less_list(nums, 450)
less_nums2 = get_less_list(nums, 200)

del_list = get_remove_value_list(nums, 12)
print("12 삭제 된 리스트 :", del_list)

range_nums = get_range_list(nums, 100, 555)
print("100 ~ 555  사이의 리스트 :", range_nums)
print('450 보다 작은 리스트 :', less_nums)
print('200 보다 작은 리스트 :', less_nums2)

print(f"최대값 : {get_max(nums)}")
print(f"최소값 : {get_min(nums)}")
# print(f"최대값 : {max(nums)}")
# print(f"최소값 : {min(nums)}")

# ---------------------------------------------------------------------------------------------------

# user_in = int(input('숫자 입력 : '))
# less_nums3 = get_less_list(nums, user_in)

import random

# rand1 = random.randint(1, 999) 
# print('rand1 :', rand1)
# randList = [] # 추가할 빈 리스트

# for i in range(0, rand1):
#     randList.append(random.randint(1, 999))

# print('randList :', randList)


# print('200 보다 작은 리스트 :', less_nums3)
# print(f'{rand1} 보다 작은 리스트 : ', get_less_list(randList,))





