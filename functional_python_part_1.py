#Задание 1
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

celsius_temperatures = [39.2, 36.5, 37.8, 37.8]
fahrenheit_temperatures = []

for temperature in celsius_temperatures:
    fahrenheit_temperatures.append(celsius_to_fahrenheit(temperature))

print(fahrenheit_temperatures)

#Задание 2
def get_string_lengths(strings):
    return [len(string) for string in strings]

example_strings = ['Tina', 'Raj', 'Tom']
lengths = get_string_lengths(example_strings)
print(lengths)

#Задание 3

sentences = ['капитан джек воробей',
             'капитан дальнего плавания',
             'ваша лодка готова, капитан']

cap_count = sum(sentence.count('капитан') for sentence in sentences)
print(cap_count)

#Задание 4
def raise_num_to_degree(x, y):
    return [x ** y for x, y in zip(x, y)]

x = [2, 3, 4]
y = [10, 11, 12]

result = raise_num_to_degree(x, y)
print(result)

#Задание 5
def generate_values(n):
    for x in range(n + 1):
        if x == 0:
            yield -10
        elif x % 3 == 0:
            yield 45
        elif x % 5 == 0:
            yield (x / 5) + 93
        else:
            yield x / 2


n = 3
print(list(generate_values(n)))

n = 7
print(list(generate_values(n)))

#Задание 6

def largest_histogram(heights):
    heights.append(0)
    max_area = 0
    stack = []

    for i, h in enumerate(heights):
        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]
            width = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)
        stack.append(i)

    return max_area



print(largest_histogram([5]))
print(largest_histogram([5, 3]))
print(largest_histogram([1, 1, 4, 1]))
print(largest_histogram([1, 1, 3, 1]))
print(largest_histogram([2, 1, 4, 5, 1, 3, 3]))
