#1
HEX = 16


def self_hex(number: int) -> str:
    if not number:
        return ''
    result = ''
    hex_letters = list('0123456789ABCDEF')
    while number > 0:
        result = hex_letters[number % HEX] + result
        number //= HEX
    return result


print(f'Шестнадцатеричное представление числа: {self_hex(num)}')
print(f'Проверка результата: {hex(num)}')

#2

# frac1 = "1/2"
# frac2 = "1/3"

# Введите ваше решение ниже
import math
from fractions import Fraction

f1 = frac1.split('/')
f2 = frac2.split('/')
a = int(f1[0])
b = int(f1[1])
c = int(f2[0])
d = int(f2[1])

x2 = a * c
y2 = b * d
nod2 = math.gcd(x2, y2)

x1 = (a * d) + (b * c)
y1 = b * d
nod1 = math.gcd(x1, y1)
print('Сумма дробей: ', x1 // nod1, '/', y1 // nod1, sep='')
print('Произведение дробей: ', x2 // nod2, '/', y2 // nod2, sep='')
print('Сумма дробей:', Fraction(frac1) + Fraction(frac2))
print('Произведение дробей:', Fraction(frac1) * Fraction(frac2))