print("hello world!")
#第一个测试程序
print(" /  |")
print("   /|")
print("  / |")
print("/___|")

# 变量 variable
name = "李四"
age = "50"

print("有个人，他叫"+name+"，来自北京,已经"+age+"公斤了")
name = "张山"
print("有个人，他叫"+name+"，来自北京,已经"+age+"公斤了")

# 数据类型 data type
print(name+" "+age)

# 字符串 string

name1 = '猎雷'
print(name1)

# 数字
age = 50.55
print(age)
# 实数
# boolean
isMale = True
print(isMale)
# 序列
print(name[0])

# 字符串 string str
mystr = "we \nare "
# 转义字符 escape character
# slash / backslash \
mystr = '"we" are'
print(mystr)
mystr = "\"we\" are"
print(mystr)
# 字符串拼接 concat
mystr = "we are"
print(mystr + " all")

mystr = "We Are"
print(mystr * 3)

print("re" in mystr)
print("you" in mystr)
print("---------------")
# 函数 function
print(mystr.lower())
print(mystr.islower())
print(mystr.isupper())
print("----")
print(mystr.upper().isupper())
print(len(mystr))
print(mystr[0])
print("99999999999")
print(mystr.index("e A"))
print(mystr.replace("We","You"))
print("uuuuuuuuuuuuu")
#print(lower(mystr))

print(mystr.isdigit())
print(mystr.isalpha())
print("0000000000000000")


print(1)
print(1e2)
print(1e+2)
print(1e-2)
print("ddddddddddddd")
print(2**5)
print(2+3)
print(2*3)
print(2/3)
print(2-3)

print(4*(2-3))
print(5%3)


mynum = 5

print(mynum+1)

print(111111111111111111111)
print(str(7) + " days is a week")
# 错误的 ：print(7 + " days is a week")
mynum=-7
print(mynum)
print(abs(mynum))
# abs 函数取绝对值
print(pow(2,4))
print(2**4)
print(max(5,3))
print(min(5,3))
print(round(4.49))

print("222222222222222")
from math import *

print(floor(4.99))
print(sqrt(9))

name="李四"
age=50
message="他是"+name+",已经"+str(age)+"公斤了"
print(message)
# 格式化字符串
msg = f'他是{name},已经{age}公斤了'
print(msg)



