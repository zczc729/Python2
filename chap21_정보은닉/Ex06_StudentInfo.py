class StudentInfo:
    NO_LEN = 13

    MIN_MAJOR_LEN = 2
    MAX_MAJOR_LEN = 50

    MIN_NAME_LEN = 2
    MAX_NAME_LEN = 20

    MIN_PHONE_LEN = 12
    MAX_PHONE_LEN = 14

    def __init__(self, no, major, name, phone):
        # if len(no) == self.NO_LEN:
        #     self.__no = no
        # else:
        #     raise ValueError(f"길이는 {self.NO_LEN}자리 고정 입니다.")

        # if self.MIN_MAJOR_LEN <= major <= self.MAX_MAJOR_LEN:
        #     self.__major = major
        # else:
        #     raise ValueError(f"길이는 {self.MIN_MAJOR_LEN} ~ {self.MAX_MAJOR_LEN} 범위만 가능합니다")
        
        # if self.MIN_NAME_LEN <= name <= self.MAX_NAME_LEN:
        #     self.__name = name
        # else:
        #     raise ValueError(f"길이는 {self.MIN_NAME_LEN} ~ {self.MAX_NAME_LEN} 범위만 가능합니다")
        
        # if self.MIN_PHONE_LEN <= phone <= self.MAX_PHONE_LEN:
        #     self.__phone = phone
        # else:
        #     raise ValueError(f"길이는 {self.MIN_PHONE_LEN} ~ {self.MAX_PHONE_LEN} 범위만 가능합니다")

        self.__no = self.__validate_length(no, self.NO_LEN)
        self.__major = self.__validate_range_length(major, self.MIN_MAJOR_LEN, self.MAX_MAJOR_LEN)
        self.__name = self.__validate_range_length(name, self.MIN_NAME_LEN, self.MAX_NAME_LEN)
        self.__phone = self.__validate_range_length(phone, self.MIN_PHONE_LEN, self.MAX_PHONE_LEN)
        
    def __validate_range_length(self, value, min_len, max_len):
        if min_len <= len(value) <= max_len:
            return value
        else:
            raise ValueError(f"길이는 {min_len} ~ {max_len} 범위만 가능합니다")
        
    def __validate_length(self, value, length):
        if len(value) == length:
            return value
        else:
            raise ValueError(f"길이는 {length}자리 고정입니다.")
        
    @property
    def no(self):
        return self.__no
    
    @no.setter
    def no(self, no):
        self.__no = self.__validate_length(no, self.NO_LEN)

    @property
    def major(self):
        return self.__major
    
    @major.setter
    def major(self, major):
        self.__major = self.__validate_range_length(major, self.MIN_MAJOR_LEN, self.MAX_MAJOR_LEN)

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        self.__name = self.__validate_range_length(name, self.MIN_NAME_LEN, self.MAX_NAME_LEN)

    @property
    def phone(self):
        return self.__phone
    
    @phone.setter
    def phone(self, phone):
        self.__phone = self.__validate_range_length(phone, self.MIN_PHONE_LEN, self.MAX_PHONE_LEN)

    def __str__(self):
        return f"학번 : {self.__no}, 전공 : {self.__major}, 이름 : {self.__name}, 연락처 : {self.__phone}"
    

try:
    s1 = StudentInfo("123-56789-123", "컴퓨터과학과", "홍길동", "010-8888-9999")
    print("s1 =", s1)

    s2 = StudentInfo("123-56789-124", "", "김수한무거북이와두루미감천갑자동박삭", "010-1234-5678")
    print("s2 =", s2)
except ValueError as e:
    print("유효하지 않은 입력 :", e)