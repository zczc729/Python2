def is_palindrome(str):
    # str1 = str[:int(len(str) / 2)]
    strList1 = []
    strList2 = []

    for i in str:
        strList1 = list(str)
        strList2 = strList1[::-1]

    for i in range(len(strList1)):
        if strList1[i] == strList2[i]:
            return True
        else :
            return False



str = input('문자열 입력 : ')

# is_palindrome 함수 : 회문이면 True 리턴, 평문이면 False 리턴
if is_palindrome(str):
    print(f"{str}은(는) 회문 입니다.")
else :
    print(f"{str}은(는) 평문 입니다.")

# str1 = input('입력 : ')
# print(str1[0])
# print(ord(str1[0]) - 96)




