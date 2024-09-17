# 1.打印和输出
print("Hello, World") # 打印一行文本

# 2.变量和数据类型
## 数字
x = 10 # 整数
y = 3.14 # 浮点数

## 字符串
name = "Alice"

## 布尔值
is_sunny = True

# 3. 列表（数组）
## 定义一个列表
fruits = ["apple", "banana", "cherry"]

## 访问列表元素
print(fruits[0]) # 输出“apple”

## 添加元素
fruits.append("orange")

## 删除元素
fruits.remove("banana")


# 4.循环
for fruit in fruits:
    print(fruit)

# while 循环
i = 0
while i < 5:
    print(i)
    i += 1

# 5.条件判断
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")

# 6.函数
def greet(name):
    return f"Hello, {name}!"

message = greet("Alice")
print(message)

# 7.字典
## 创建字典
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

## 访问字典值
print(person["name"]) 

## 修改字典值
person["age"] = 31

# 8.文件操作
## 写入文件
with open("example.txt", "w") as file:
    file.write(person)

##读取文件
with open("example.txt", "r")  as file:
    content = file.read()
    print(content)
# 9.异常处理
try:
    number =int(input("Enter a number: "))
    print(100 / number)
expect ZeroDivisionError:
    print("Cannot divide by Zeor")
except ValueError:
    print("Invalid input, please enter a number")

# 10. 类与对象
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} says woof")
##创建对象
my_dog = Dog("Buddy", 5)
my_dog.bark() # "Buddy says woof!"