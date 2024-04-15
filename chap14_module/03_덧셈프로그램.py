"""
밑줄 친 부분에 0 ~ 9 사이의 랜덤한 수가 출력 하게 코드를 구현하시오.

1. _ + _ = _
2. _ + _ = _
3. _ + _ = _
4. _ + _ = _
5. _ + _ = _
6. _ + _ = _
7. _ + _ = _
8. _ + _ = _
9. _ + _ = _
10. _ + _ = _
"""

from random import randint

score = 0
for i in range(1, 11):
    ques1 = randint(0, 9)
    ques2 = randint(0, 9)
    print(f"{i}. {ques1} + {ques2} = ", end="")
    cor = int(input())
    if (ques1 + ques2) == cor:
        score += 10

# print("점수 : ", score, "점")
# print("맞힌 개수 : ", int(score / 10), "개")
print(f"10 문제 중 {int(score / 10)}개 정답\n점수 : {score}")