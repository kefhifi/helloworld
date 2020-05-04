my_name= "jack.ma"
list_name= ["jack.ma","pony.ma","robin.li"]
def who_am_i(name):
    print(f'my name is {name}')
class Student:
    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
    def who_am_i(self):
        print(f'i am a student,{self.__name}|{self.__age}|{self.__sex}')
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name = name
print(__name__)
if (__name__ == "__main__"):
    print(my_name)
    print(list_name)
    who_am_i("duke")
    tom = Student("tom.li",15,"male")
    tom.who_am_i()