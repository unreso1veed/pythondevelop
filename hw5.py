
#задание 1
elements = [5, 1, 7, 3, 9, 5]
sum_elements = 0
for i in range(len(elements)):
    if i % 2 == 0:
        sum_elements += elements[i]


print(sum_elements * elements[i])

#задание 2

elements = [10.2, -2.2, 0, 1.1, 0.5]

print(round(max(elements) - min(elements), 3))

#задание 3

elements = (-1, -2, -3, 0)

print(sorted(elements, key = abs))

#задание 4 Junior

elements = [3, 6, 20, 99, 10, 15]
elements = sorted(elements)
mediana_element = 0
for i in range(len(elements)):
        if len(elements) % 2 == 1:
            mediana_element = elements[len(elements) // 2]

        else:
            mediana_element = ((elements[len(elements) // 2] + elements[len(elements) // 2 - 1]) / 2)


print(mediana_element)







