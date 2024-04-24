with open("proverb.txt", "r") as file :
    while True :
        line = file.readline()
        if not line :
            break
        else :
            print(line, end="") # 속담 출력

            a_count = 0

            # 속담에서 a, A의 개수 찾기
            for letter in line :
                if letter in "aA" :
                    a_count += 1
            print(f"a(A)의 개수는 {a_count}개 입니다.\n")