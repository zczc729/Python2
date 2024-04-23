with open("word.txt", "r") as file :
    fL = file.read()
    fList = fL.split()
    h_score = 0

    
    for i in range(len(fList)) :
        w_score = 0
        for j in fList[i] :
            w_score += ord(j) - 96
        if w_score == 100 :
            print(f"{i + 1} 번 째 단어 : {fList[i]}")
            print(f"단어의 점수 : {w_score}점\n")
            h_score += 1
    print(f"\n100점 짜리 단어의 개수 : {h_score}개")

    