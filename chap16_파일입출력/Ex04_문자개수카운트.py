# file = open("pigs.txt", "r", encoding="utf-8")

# 파일의 내용을 문자열 타입으로 모두 읽어오기
u_count = 0
v_count = 0
t_count = 0

# with 블럭이 끝나면 파일이 자동으로 닫힘
with open("pigs.txt", "r", encoding="utf-8") as file :
    while True:
        ch = file.read(1) # 한 글자씩 읽어 들인다

        if not ch : # 읽어들인 문자가 없다면?
            break   # 무한 루프 탈출
        elif 'A' <= ch <= 'Z' :
            u_count += 1 
        if ch in "AEIOUaeiou" : # 문자가 "AEIOUaeiou"에 포함 되어 있다면?
            v_count += 1        # 모음 개수 추가
        
        t_count += 1 # 반복 횟수가 전체 글자수가 된다

print(f"대문자 개수 : {u_count}")
print(f"모음 개수 : {v_count}")
print(f"전체 글자 개수 : {t_count}")

# file.close()