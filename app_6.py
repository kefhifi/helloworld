# 类  class
# 实例  实体  instance

class Student:
    pass
jack = Student()
jack.name = "jack.ma"
print(jack.name)

#  构造函数 constructor
print("构造函数 constructor.....................")
class Student:
    def __init__(self):
        print("__init__ is run")
jack = Student()
print("..................2.....................")
class Student:
    def __init__(self,name):
        self.name = name
        print("__init__ is run")
jack = Student("jack.ma")
pony = Student("pony.ma")
print(jack.name)
print(pony.name)
print("...................3....................")
class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
        print("__init__ is run")
jack = Student("jack.ma",16,"male")
pony = Student("pony.ma","10","male")

# 类函数 class function
print(" 类函数.............................")
# 类方法 class method
class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
def print_info(s):
    print(f'{s.name}__{s.age}__{s.sex}')
jack = Student("jack.ma",12,"male")
print_info(jack)
print("...............分割线.1.................")
class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def print_info(self):
        print(f'{self.name}__{self.age}__{self.sex}')
jack = Student("jack.ma",12,"male")
jack.print_info()
print("...............分割线.2.................")
class Student:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
    def print_info(self):
        print(f'{self.name}__{self.age}__{self.sex}')
jack = Student("jack.ma",12,"male")
jack.name = "pony.ma"
jack.print_info()
print("...............分割线.3.................")
# 属性值加两个下划线，属性不能被外部访问。
class Student:
    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
    def print_info(self):
        print(f'{self.__name}__{self.__age}__{self.__sex}')
jack = Student("jack.ma",12,"male")
jack.name = "pony.ma"
jack.print_info()
print("...............分割线.4.................")
class Student:
    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
    def print_info(self):
        print(f'{self.__name}__{self.__age}__{self.__sex}')
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
jack = Student("jack.ma",12,"male")
print(jack.get_name())
jack.set_name("pony")
print(jack.get_name())
jack.print_info()

# 继承   inheritance
print("...............分割线.5.................")
class Person:
    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
    def who_am_i(self):
        print(f'i am a person,{self.__name}|{self.__age}|{self.__sex}')
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self,age):
        sefl.__age = age
    def get_sex(self):
        return self.__sex
    def set_sex(self,sex):
        self.__sex = sex
jack = Person("jack.ma",18,"male")
jack.who_am_i()
jack.set_name("pony")
jack.set_sex("female")
jack.who_am_i()

print("...............分割线.2.................")
class Student(Person):
    def who_am_i(self):
        print(f'i am a student,{self.get_name()}')
    def learn(self):
        print("i am learning")
class Teacher(Person):
    def teach(self):
        print("i am teaching")
brad = Student("brad.pitt",15,"male")
brad.who_am_i()
brad.learn()

































