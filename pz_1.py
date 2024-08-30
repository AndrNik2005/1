
'''
a = 1
b = 4
c = 3
if  a + b > c and b + c > a and c + a > b:
    print('Треугольник существует')
    if a!= b and b!= c and c!= a:
        print('Треугольник разносторонний')
    elif a == b and b == c and c == a:
        print('Треугольник равносторонний')
    else:
        print('Треугольник равнобедренный')
else:
    print('Треугольник не существует')
'''
'''
#num = 2

# Введите ваше решение ниже
switch = True
if 2 <= num and num <= 100_000:
    for i in range(2, num):
        if num % i == 0:
            switch = False
    if switch:
        print('Простое')
    else:
        print('Не является простым')
else:
    print("Число должно быть больше 1 и меньше 100000")
'''

#list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
#list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]

# Введите ваше решение ниже
result = 0
for i in list1:
    for j in list2:
        if i == j:
            result += 1

print(f'Количество совпадающих чисел: {result}')






