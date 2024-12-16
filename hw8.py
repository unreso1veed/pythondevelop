from collections import Counter
import itertools
#Задание 1

data = [1, 2, 3, 1, 3]
counts = Counter(data)

result = []
for x in data:
    if counts[x] > 1:
        result.append(x)

print(result)


#Задание 2

x, y, z, n = 1, 2, 4, 2

data = [x, y, z]
data_result= []
permutations = list(itertools.permutations(data))


for elements in permutations:
    if elements[0] + elements[1] - elements[2] > n:
        data_result.append(elements)
           
print(data_result)

#Задание 3

n = 5
data = []

for i in range(n):
    if i % 2 != 0:
        data.append(i * 2)

print(data)

#Задание 4 Junior

'я и мой друг не справились (хз реально)'