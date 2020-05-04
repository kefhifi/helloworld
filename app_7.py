# 模块 module
# PYTHONPATH
print(".................方法一...................")
import student
print(student.my_name)
print(student.list_name[2])
student.who_am_i("dennis")
kate = student.Student("kate.li",15,"female")
kate.who_am_i()
print("..................分割线...............")
import sys
print(sys.path)
print("..............................")
for line in sys.path:
    print(line)
print(".................方法二...................")
from student import Student,my_name,who_am_i
kate = Student("kate.li",15,"female")
kate.who_am_i()
print(my_name)
print(who_am_i("robin"))
print(".................测试一...................")
my_name = "dell"
from student import my_name
print(my_name)

print(".................测试二...................")
my_name = "dell"
from student import my_name
my_name = "luis"
print(my_name)
print(".................测试三 ...................")
my_name = "dell"
from student import my_name as uname
print(my_name)
print(uname)
print(".................测试四 ...................")
my_name = "dell"
from student import *
print(my_name)
print(list_name)
who_am_i("levis")
jule = Student("jule.ma",12,"female")
jule.who_am_i()

print(".................测试五 ...................")
import student as s
print(s.my_name)
print(".................测试六 ...................")

def foo():
    import sys
    print(sys.path)
foo()
# dir
print(".................查看当前模块的属性 ...................")
print(dir())
print(dir(s))




