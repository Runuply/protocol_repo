# 1 切片格式,lst[start:stop:step]
lst = [0,1,3,4,5,6,7,8,9]
print(lst[::-2])
# start: 开始索引（包括该索引的元素）
# stop： 结束索引（不包括该索引的元素）
# ：在切片表达式中用于分隔 start stop 和step
# start 和 stop 省略：默认从头到尾
# step = -2：表示列表末尾开始，每次跳过一个元素。
# 输出： [9,7,5,3,0]
lst = [0,1,3,4,5,6,7,8,9]
print(lst[1:4])
# 这里1:4 表示从1索引，一直到索引4（元素4）结束，但是不包含索引4
# 这个是不带步长的切片。没有制定step，所以python默认step是1，即每次取下一个连续的元素。


# 2 计算水仙花数（阿姆斯特朗数/Armstrong numbers）
# 一个三位数，它的每个位上的数字的3次幂之和等于它本身（例如：1^3+5^3+3^3 = 153)
for i in range(100, 1000):
    a = i // 100  # bai/ extracts the hundreds digit.
    b = i // 10 % 10 # shi/ extracts the tens digit.
    c = i % 10 # ge/ extracts the units digit
    if a ** 3 + b ** 3 + c ** 3 == i:
        print(i)  

# Integer division (//) divides the number and returns the whole number without the remainder.
# For example:
#if i = 456, then i // 100 = 456 // 100 = 4
#if i = 789, then i // 100 = 789 // 100 = 7
#This is because 100 fits into 456 four times and into 789 seven times. The result is the hundreds digit.

# i // 10 performs integer division by 10, which removes the last digit (the units digit).
# If i = 456, then i // 10 = 45.
# If i = 789, then i // 10 = 78.
# Next, % 10 (modulus 10) gives the remainder when the result is divided by 10, effectively isolating the last digit of this result, which is the tens digit.
# 456 // 10 = 45, and 45 % 10 = 5 (the tens digit).
# 789 // 10 = 78, and 78 % 10 = 8 (the tens digit).

# The modulus operator (%) gives the remainder when dividing by 10. This remainder is the units (ones) digit.
# If i = 456, then 456 % 10 = 6.
# If i = 789, then 789 % 10 = 9.