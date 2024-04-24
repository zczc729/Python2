import random

def randomize(being, end, size):
    for i in range(size):
        nums.append(random.randint(begin, end))

def printList():
    for num in nums:
        print(num, end = " ")
    print()

nums = []

begin = int(input("랜덤 시작값 : "))
end = int(input("랜덤 종료값 : "))
size = int(input("리스트의 크기 : "))

randomize(begin, end, size)
printList()
