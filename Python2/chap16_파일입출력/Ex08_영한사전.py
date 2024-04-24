search_word = input("검색 단어를 입력 하세요 : ")

try :
    with open("meaning.txt", "r", encoding="euc-kr") as file :
        is_search = False

        while True :
            line = file.readline() # 한 행 씩 읽어 들이기
            
            if not line : # 파일의 끝이라면?
                break     # 무한 루프 탈출

            list_word = line.split() # 공백으로 나눠서 리스트를 생성
            word = list_word[0] # 단어 분리해서 저장
            meaning = ""
            
            for i in range(1, len(list_word)) :
                meaning += list_word[i] + " "

            if word == search_word :
                print(f"검색한 단어 [{word}]의 뜻은 [{meaning}] 입니다.")
                is_search = True

        if is_search == False :
            print(f"검색한 단어 [{search_word}]가 없습니다.")
except FileNotFoundError as exp_msg :
    print("파일을 찾을수 없습니다.", exp_msg)
        


