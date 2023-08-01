# 1
value1 = input("Введите первое число: ")
value2 = input("Введите второе число: ")
value3 = input("Введите третье число: ")
print(value1,value2,value3,sep="")

# 2
value4 = input("Введите число: ")
count = 1
for i in value4:
    count *= int(i)
print(count)

# 3
value5 = int(input("Введите количество метров: "))
sm = value5*100
dm = value5*10
mm = value5*1000
mill = value5*0.00062
print(value5, "метров - это ", sm, " сантиметров.")
print(value5, "метров - это ", dm, " дециметров.")
print(value5, "метров - это ", mm, " миллиметров.")
print(value5, "метров - это ", mill, " миль.")

# 4
value6 = int(input("Введите размер основания треугольника: "))
value7 = int(input("Введите высоту треугольника: "))
area = value6*value7/2
print("Площадь треугольника составляет", area)

# 5
value8 = int(input("Введите число: "))
value9 = 0
while value8>0:
    value9 = value9*10 + value8%10
    value8 = value8//10
print(value9)
