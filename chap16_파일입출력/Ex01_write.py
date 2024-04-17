# 파일 모드 : r(읽기 모드, read), w(기록 모드, write), a(추가 모드, append)
# w 모드 : 파일 오픈 시 내용이 있다면 그 내용을 삭제 후 새로 기록한다
# a 모드 : 파일 오픈 시 내용이 있다면 그 내용 뒤에 기록
file = open("test.txt", "a", encoding="utf-8") # 파일명은 필수, 파일 모드는 필수 X

file.write("오늘은 뭐먹지")

file.close() # 파일 닫기

## open ~ close 사이 수행하고 싶은 명령 수행

f = open("sample.txt", "w", encoding="utf-8")

for i in range(1, 10):
    f.write(str(i) + "\n") # 기록 할 때는 문자열로 들어가기 때문에 int형으로 들어갈 수 없다.
f.close()

score = ["이순신 100 100 100" , "장보고 90 80 70", "강감찬 78 98 56"]

fi = open("score.txt" , "w", encoding="utf-8")

for student in score :
    fi.write(student + "\n")
fi.close()