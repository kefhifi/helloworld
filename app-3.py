# name = input("please input your name:")
# print(name + ", welcome!")
# age = input("请输入你的年龄：")
# print(input("please input your name: ") + ", welcome。"+age+"岁")

# 列表 list
favorite_fruits = ["apple","orange","pear","watermelon","peach"]
#                     0        1       2        3          4
#                    -5       -4       -3       -2          -1
# favorite_fruits = ["apple","orange","pear",109,True]
print(favorite_fruits)
print(favorite_fruits[1])
print(favorite_fruits[-1])

# 索引 index
print("切片..............")
# 切片  slice
# 切到末尾
print(favorite_fruits[1:])

print(favorite_fruits[1:4])
# 2号之前的切下来，不包括2号
print(favorite_fruits[0:2])

favorite_fruits[0] = "grape"
print(favorite_fruits)

# 函数操作列表
print("函数操作列表................")
my_numbers = [10,3,12,14,6,18,15]
my_fruits = ["apple","orange","pear"]
print(my_numbers)
print(my_fruits)
print("extend...................")
# extend
my_fruits.extend(my_numbers)
print(my_fruits)
print("append...................")
my_fruits.append("grape")
print(my_fruits)
print("insert...................")
my_fruits.insert(0,"grape")
print(my_fruits)
my_fruits.insert(3,"grape")
print(my_fruits)
print("remove...................")
my_fruits.remove("grape")
print(my_fruits)
# 只删除了第一个grape
print("clear: 清空列表所有元素...................")
#my_fruits.clear()
print(my_fruits)
print("pop...................")
my_fruits.pop()
print(my_fruits)

my_fruits.pop(0)
print(my_fruits)

print("index:  返回索引位置...................")
print(my_fruits.index("pear"))

my_fruits = ["apple","apple","apple","orange","pear"]
print(my_fruits)
print("count: 查找列表中某个值的元素的个数")

print(my_fruits.count("apple"))

print("sort: 排序...................")
my_fruits = ["apple","pear","orange","apple","apple"]
my_fruits.sort()
print(my_fruits)
print(my_numbers)
my_numbers.sort()
print(my_numbers)
print("reverse: 反转列表...................")
print(my_fruits)
my_fruits.reverse()
print(my_fruits)
print("copy: 把一个列表的值拷贝到另外一个列表...................")
print(my_fruits)
my_fruits2 = my_fruits.copy()
print(my_fruits2)
print("\n---------------------------------分割线------------------------------------------------------------")
# 元组 tuple
print("元组 tuple...............")
best_companies = ["google","microsoft","alibaba","tencent"]
print(best_companies)
best_companies = ("google","microsoft","alibaba","tencent")
print(best_companies)

print(best_companies[0])
# X:   best_companies[0] = "facebook"
# tuple 不能重新赋值，修改，排序等操作
print("\n---------------------------------函数：function------------------------------------------------------------")
# def
def sayHello(name,age):
    print("say,hello " + name + ",your age : "+ age)
# print("say hi")
print("函数调用：call")
print("11111")
#sayHello("张山")
print("22222")

best_friends = ["张山","李四","王五"]
ages = ["10","20","30"]

sayHello(best_friends[0],ages[0])
sayHello(best_friends[1],ages[1])
sayHello(best_friends[2],ages[2])

print("sayHello_2.......................")
def sayHello_2(name,age):
    print("say,hello " + name + ",your age : " + str(age))

ages_2= [10,20,30]
sayHello(best_friends[0],ages[0])
sayHello(best_friends[1],ages[1])
sayHello(best_friends[2],ages[2])

