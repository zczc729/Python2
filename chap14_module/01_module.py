# import 모둘명
# import unitConversion # unitConversion 파일을 가져오겠다.
# import 모둘명 as 별명 # 별명을 만들어서 모듈을 간단하게 쓰겠다.
import unitConversion as uc

# from 모둘명 import 요소1, 요소2, 요소3, 요소4 ... # 하뭇 호출시 모듈명으로 호출하기 귀찮다.
from unitConversion import yard_to_meter, inch_to_cm
from unitConversion import ft_to_cm as ftc # 요소에 별명을 붙힐 수 있다.
# from unitConversion import * # 모든 요소를 가지고 오겠다.

# print(f"3mile은 {unitConversion.mile_to_km(3)}km 입니다.") # 모듈명으로 함수 호출
print(f"3 mile은 {uc.mile_to_km(3)}km 입니다.") # 별명으로 함수 호출
print(f"100 yard는 {yard_to_meter(100)} 입니다.")
print(f"24 inch는 {inch_to_cm(24)}cm 입니다.")
print(f"3 ft는 {ftc(3)}cm 입니다.")