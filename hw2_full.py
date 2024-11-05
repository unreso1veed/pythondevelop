from random import randint
import math

# первая задача
'''
a = (randint(1, 100))
b = (randint(1, 100))
c = (randint(1, 100))
nums = [a, b, c]

print (a, b, c)
print(a + b + c / len(nums))
'''
# вторая задача

'''
a = (randint(1, 100))
b = (randint(1, 100))

print (a, b)
print (a // b, a % b)
'''
# третья задача
'''
a = float(input("Введите число с плавающей точкой:"))

print(round(a, 2), math.ceil(a))
# последнее не придумал ((
'''
# четвертая задача

'''a = int(input("Введите число:"))

a2 = 0

while a > 0:
    b = a % 10
    a = a // 10

    a2 = a2 * 10
    a2 = a2 + b
else:
    print ("0")

print('Обратное число:', a2)'''

# пятая задача

a = int(input("Введите число:"))

a2 = 0
int32 = 2147483647

if a == 0 or a > int32:
    print ('0')

else:
    while a > 0:
        b = a % 10
        a = a // 10

        a2 = a2 * 10
        a2 = a2 + b

    print('Обратное число:', a2)











