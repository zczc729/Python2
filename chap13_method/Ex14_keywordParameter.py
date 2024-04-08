def print_person_info(name, postition = "staff", nationality="Korea"):
    print(f"name = {name}")
    print(f"posistion = {postition}")
    print(f"nationality = {nationality}")
    print()

print_person_info("홍길동")
print_person_info("고길동", "japan") # 키워드 생략시 순서대로 전달된다.
print_person_info("고길동", nationality = "japan") #keyword parameter





