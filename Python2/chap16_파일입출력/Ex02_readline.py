file = open("score.txt", "r", encoding="utf-8")

# readlines : 파일의 내용을 리스트 타입으로 모두 가져온다.
lines = file.readlines()
print(lines)
print(lines[0])
print(lines[1])
print(lines[2])

# seek(얼마나 이동?, 어디에서)
# 처음 위치 : 0, 현재 위치 : 1, 맨 뒤 위치 : 2
file.seek(0, 0) # 파일 포인터의 위치를 첫 위치로 이동
# 파일을 한 번 읽으면 포인터가 맨 뒤로 이동하기 때문에 처음으로 이동 시켜준것

# 파일의 내용을 문자열 타입으로 모두 가져온다.

str = file.read()

print(str)

file.seek(0, 0)

# 파일을 행 단위로 문자열 타입으로 가져온다
line = file.readline()
print(line)
line = file.readline()
print(line)