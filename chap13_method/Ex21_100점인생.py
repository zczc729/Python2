def get_word_score(word):
    total = 0

    for i in range(len(word)):
        code = ord(word[i]) # 영문자의 유니코드(ordinal) 값을 구한다
        total = total + (code - 96)
    return total # 단어의 합을 리턴


word = input("100점 짜리 인생을 만들기 위해 정말로 필요한건 뭘까요?")

score = get_word_score(word)
print(f"{word} 단어의 점수는 {score} 점 입니다.")



