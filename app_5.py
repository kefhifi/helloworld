# 二维列表
#维度 dimension
# two demension list
# 2D list
# dim
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
matrix[1][0] = 122
print(matrix[0])
print(matrix[1][0])

for row in matrix:
    for item in row:
        print(item)
print("unpacking............")
# 解包 unpacking
user = ["李四",20,"2002-01-01"]
# 法一
# user_name = user[0]
# age = user[1]
# born_date = user[2]
# 法二
user_name,age,born_date = user
print(user_name)
print(age)
print(born_date)
print("tuple 解包....................")
user = ("李四",20,"2002-01-01")
user_name,age,born_date = user
print(user_name)
print(age)
print(born_date)

# 错误: error
# 异常处理: exception
# indent  : 缩进
try:
    num = int(input("please input number:"))
    result = 1/num
    print(result)
except:
    print("error input")

print("..............")
try:
    num = int(input("please input number:"))
    result = 1/num
    print(result)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")


print("...............................")
try:
    num = int(input("please input number:"))
    result = 1/num
    print(result)
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)
print("...............................")
def test_fails(num):
    return 1/num
try:
    num = int(input("please input number:"))
    result = test_fails(num)
    print(result)
except ZeroDivisionError as error:
    print(error)
except ValueError as error:
    print(error)
print("文件操作....................")
# 文件操作
story_file = open("story.txt","r")
content = story_file.read()
print(content)
story_file.close()

# 读取10个字符
story_file = open("story.txt","r")
content = story_file.read(10)
print(content)
story_file.close()
# 读取一行内容
story_file = open("story.txt","r")
content = story_file.readline()
print(content)
# 再读取第二行内容
print(story_file.readline())
print(story_file.readline())
story_file.close()

story_file = open("story.txt","r")
content = story_file.readlines()
# print(content[1])
for line in content:
    print(line)
story_file.close()

# 追加
story_file = open("story.txt","a")
story_file.write("\nyes")
story_file.write("\nno")
story_file.close()

# 重写
story_file = open("story.txt","w")
story_file.write("wwwwwww")
story_file.close()

# 打开不存在的文件，则新建文件

story_file = open("story_1.txt","w")
story_file.write("wwwwwww")
story_file.close()
