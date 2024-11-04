
#Первое задание

# name = str(input("Введите имя:"))
# surname = str(input("Введите фамилию:"))
# print("Hello", name, surname, "! You just delved into Python. Great start!")

#Второе задание

# text = str(input("Введите строку любой длины:"))
# print (str.title(text))

#Третье задание

def format_currency(amount):
    amount = round(amount, 2)

    formatted_amount = f"{amount:,.2f}"

    return formatted_amount



amount = float(input("Введите число:"))
result = format_currency(amount)
print(result)
