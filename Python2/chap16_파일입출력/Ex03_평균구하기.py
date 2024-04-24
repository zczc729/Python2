file = open("score.txt", "r", encoding="utf-8")

# 모든 내용을 리스트 형태로 읽어 들인다
lines = file.readlines()
print(lines)
file.close

search_name = input("검색할 이름 입력 : ")

for line in lines : # 리스트 반복
    studentInfo = line.split()

    if search_name == studentInfo[0] :
        total = int(studentInfo[1]) + int(studentInfo[2]) + int(studentInfo[3])
        print(f"{studentInfo[0]}의 평균 : {total / 3:.2f}")

if search_name != studentInfo[0]:
    print(f"검색한 이름 {search_name}이(가) 없습니다.")
