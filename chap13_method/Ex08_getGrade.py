

def getGrade(num):
    if 90 <= num <= 100:
        return 'A'
    elif(80 <= num):
        return 'B'
    elif(70 <= num):
        return 'C'
    elif(60 <= num):
        return 'D'
    else:
        return 'F'


score = int(input("점수 입력 : "))
#getGrade : 점수로 등급을 구해 리턴하는 함수
print("%d점 : %s등급" %(score, getGrade(score)))




