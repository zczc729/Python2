
def check_password(pw):
    # CheckPw = False

    if len(pw) < 10:
        #  pwChk = False
        return False
    u_chk = l_chk = d_chk = False # 문자 체크 변수를 False 설정

    # for pw in password:
    #     if 'a' <= pw <= 'z': # 소문자가 있다면?
    #         l_chk = True
    #     elif 'A' <= pw <= 'Z': # 대문자가 있다면?
    #         u_chk = True
    #     elif '0' <= pw <= '9': # 숫자 문자가 있다면?
    #         d_chk = True 
    
    # return u_chk and l_chk and d_chk

    # checkStr = ''
         

    # for i in range(65, 91):
    #     checkStr = chr(i)

    # for i in range(97, 123):
    #     checkStr += chr(i)

    # for i in range(48, 58):
    #     checkStr += chr(i)

    # print(type(checkStr))
    # print(checkStr)

    # for pw in password:
    #     if pw != checkStr:
    #         return False
    #     else:
    #         return True
        
    



password = input('비밀번호 입력 : ')

# check_password 함수 : 유효성 체크를 해서 사용 가능한 비밀번호면 True, 아니라면 False 리턴
if check_password(password):
    print('사용 가능한 비밀번호 입니다.')
else:
    print('[오류] 비밀번호는 대/소문자/숫자를 포함해서 최소 10글자 이상 설정해 주세요.')









