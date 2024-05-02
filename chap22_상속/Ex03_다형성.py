class Animal:
    def speak(self):
        pass

    def walk(self):
        print("(부모 클래스) 네 발로 걷는다.")


class Dog(Animal):
    def speak(self):
        print("(overriding) 멍멍!!!")

class Cat(Animal):
    def speak(self):
        print("(overriding) 야옹!!!")

class Pig(Animal):
    def speak(self):
        print("(overriding) 꿀꿀!!!")

class Duck(Animal):
    def speak(self):
        print("(overriding) 꽥꽥!!!")

    def walk(self):
        print("(overriding) 두 발로 걷는다.")

while True:
    print("\n\t\t * 동물 농장 *")
    print("1. dog    2. cat    3. pig    4. duck    0. terminate")
    choice = int(input("메뉴 선택 : "))
    
    ani = None # 인스턴스가 생성되지 않은 경우 None
    if choice == 1: 
        ani = Dog() # 인스턴스 생성
    elif choice  == 2:
        ani = Cat()
    elif choice == 3:
        ani = Pig()
    elif choice == 4:
        ani = Duck()
    else:
        break

    ani.speak() # polymorphism(다형성) : 한 개의 명령으로 다양한 명령을 수행!
    ani.walk()
    