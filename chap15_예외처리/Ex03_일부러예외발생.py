nums = [17, 145, 35, 345, 37, 32, 987]
try :
    index = int(input("리스트의 첨자를 입력 하세요 : "))

    if index < len(nums) * -1 : # 음수인 경우 예외를 별도로 처리
        raise Exception("사용 가능한 음수 범위를 벗어났습니다.") # 예외가 강제적으로 발생
    
    print(f"nums[{index}] = {nums[index]}")
except IndexError as exp :
    print(exp)
except Exception as exp:
    print(exp)
