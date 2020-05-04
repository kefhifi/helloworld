# 包 package
import animal.cat,animal.dog
animal.cat.show_cat_name()
animal.dog.show_dog_name()
print("........................测试二.................................")
from animal.cat import show_cat_name
show_cat_name()
print("........................测试三.................................")
from animal import cat,dog
cat.show_cat_name()

print("........................测试四.................................")
from animal import cat as c,dog as d
d.show_dog_name()

print("........................测试五.................................")
import animal
animal.dog.show_dog_name()

print("........................测试六.................................")
import animal_1
print(animal_1.Mydata)

print("........................测试七.................................")
import animal_1.duck
animal_1.duck.foo()













