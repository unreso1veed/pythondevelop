#задание 1

number = int(input("Введите положительное целое число: "))

if number % 3 == 0 and number % 5 == 0:
    print("Fizz Buzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)

#задание 2

x = int(input('Введите число:'))

if x % 2 != 0:
    print('Плохо')
elif x in range(2, 5 + 1):
    print ('Неплохо')
elif x in range(6, 20 + 1):
    print ('Так себе')
elif x > 20 and x % 2 == 0:
    print ('Отлично')

#задание 3

N = int(input('Введите число в промежутке от 1 до 9:'))

if N in range(1, 9 + 1):
    print (list(range(1, N + 1)))

else:
    print ('Число не в диапозоне от 1 до 9.')

#задание 4

user_str = str(input('Введите строку:'))
uppercase_letters = ''.join([char for char in user_str if char.isupper()])
print(uppercase_letters)

#задание 5

def has_three_consecutive_words(s):
    parts = s.split()

    count = 0
    for part in parts:
        if part.isalpha():
            count += 1
            if count == 3:
                return True
        else:
            count = 0

    return False

input_string = "5 6 7"
result = has_three_consecutive_words(input_string)
print(result)

