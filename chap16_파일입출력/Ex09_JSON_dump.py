# JSON(JavaScript Object Notation) : 데이터를 효율적으로 저장하고 교환하기 위한 경량의 텍스트로 
#                                    리스트나 딕셔너리 같은 복잡한 데이터를 저장 할 때 사용하면 좋다

# 학생 dict를 선언 (key : value의 쌍으로 이루어진다.) - key 값은 무조건 문자열이다.

import json

student = {
    "name" : "Jaden Kim",
    "age" : 25,
    "isStudent" : True,
    "grade" : [98, 72, 65], # 성적은 리스트에 저장
    "address" : {
        "city" : "Busan",
        "zipcode" : "4783"
        } # 주소는 딕셔너리에 저장
}

with open("studentInfo.json", "w") as file :
    json.dump(student, file) # 딕셔너리를 json 타입으로 저장