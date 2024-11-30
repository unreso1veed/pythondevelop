#задание 1
import string
from collections import defaultdict

text = "hello, word of word"

text = text.translate(str.maketrans('', '', string.punctuation))
words = text.split()

words_popularity = defaultdict(int)
chars_popularity = defaultdict(int)

for word in words:
    words_popularity[word] += 1
    for char in word:
        chars_popularity[char] += 1


words_popularity = dict(words_popularity)
chars_popularity = dict(chars_popularity)


print("words_popularity:", words_popularity)
print("chars_popularity:", chars_popularity)

#задание 2

all_roman = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

def to_roman(num):
    roman = ''
    while num > 0:
            for i, r in all_roman:
                while num >= i:
                    roman += r
                    num -= i



    return roman

print("Число 3999 в римской системе = " + to_roman(3999))
print("Число 6 в римской системе = " + to_roman(6))
print("Число 87 в римской системе = " + to_roman(87))

#задание 3

rates = {
    'Sberbank': 114.02,
    'Alfa': 112.67,
    'T-bank': 109.56,
    'VTB': 116.12,  #trailling command
}

min_value = min(rates.values())

for key, value in rates.items():
    if value == min_value:
        key_found = key
        break

print(key_found,'-->', min_value)

# задание 4

book = {
    'Petr': '546810',
    'Katya': '241815',
    'Ivan': '228666',
    'Serega': '123456', #trailling command
}

book_inv = {}

for key, value in book.items():
    book_inv[value] = key
    book_inv[key] = value
    book_inv.pop(key, value)

print(book)
print(book_inv)

# задание 5

dates = ['2024-08-12', '2024-11-30']
rates = [87.99, 114.12]

dates_rates = {}

for i in range(len(dates)):
    for j in range(len(rates)):
       if i == j:
           dates_rates.update({dates[i]: rates[j]})

print(dates_rates)

# задание 6 Junior +

data = [
    "OO.",
    "XOX",
    "XOX"
]

for row in data:
    if row == "XXX":
        result = "X"
        break
    elif row == "OOO":
        result = "O"
        break
else:

    for col in range(3):
        if data[0][col] == data[1][col] == data[2][col] == "X":
            result = "X"
            break
        elif data[0][col] == data[1][col] == data[2][col] == "O":
            result = "O"
            break
    else:
        if data[0][0] == data[1][1] == data[2][2] == "X" or data[0][2] == data[1][1] == data[2][0] == "X":
            result = "X"
        elif data[0][0] == data[1][1] == data[2][2] == "O" or data[0][2] == data[1][1] == data[2][0] == "O":
            result = "O"
        else:
            if all(cell != '.' for row in data for cell in row):
                result = "D"
            else:
                result = None

print(result)






