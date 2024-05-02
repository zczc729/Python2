class StringUtil:
    # 문자열을 판별해서 회문이면 True 리턴, 아니라면 False 리턴

    # @staticmethod
    # def is_pailndrome(str):
    #     str_list = list(str)
    #     str_Rlist = str_list[::-1]
    #     count = 0

        # for i in range(0, int(len(str_list) / 2)):
    #         if str_list[i] == str_Rlist[i] :
    #             count += 1
        
    #     if count == int(len(str_list) / 2 ) :
    #         return True
    #     else : 
    #         return False

    @staticmethod
    def is_pailndrome(str):
        # copy = str[::-1] # 역순 저장
        # strip : 앞 뒤 공백을 제거
        # replace(old, new)
        copy = str.lower().replace(" ", "") # 대소문자 구분이 없게 된다.
        reverse_copy = copy[::-1]

        if copy == reverse_copy :
            return True
        else : 
            return False


str = input("문자열 입력 : ")

if StringUtil.is_pailndrome(str) :
    print(f"{str}은 회문 입니다.")
else :
    print(f"{str}은 평문 입니다.")
