import json

with open("studentInfo.json", "r") as file:
    student = json.load(file) # 파일 읽기
    
print(student)