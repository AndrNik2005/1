#1
'''
items = {'ключи': 0.3, 'кошелек': 0.2, 'телефон': 0.5, 'зажигалка': 0.1}
max_weight = 1.0

backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight
print(backpack)
'''

#3

lst = [1, 1, 2, 2, 3, 3]

# Введите ваше решение ниже
def remove_duplicates(lst):
    seen = []
    result = []
    for item in lst:
        if item not in seen:
            seen.append(item)
        elif item in seen and item not in result:
            result.append(item)
    return result

result = remove_duplicates(lst)
print(result)


#2
text = 'Hello world. Hello Python. Hello again.'

# Введите ваше решение ниже
import re
from collections import Counter

def top_10_words(text):
    # Используем регулярное выражение, которое учитывает апострофы
    words = re.findall(r"[a-zA-Z]+", text.lower())
    word_counts = Counter(words)
    # Удаляем слова, состоящие только из цифр
    word_counts = {word: count for word, count in word_counts.items() if not word.isdigit()}
    # Сортируем слова по убыванию количества повторений и обратному алфавитному порядку
    sorted_words = sorted(word_counts.items(), key=lambda x: (x[1], x[0]), reverse=True)
    return sorted_words[:10]

# Пример использования
# text = 'Hello world. Hello Python. Hello again.'
result = top_10_words(text)
print(result)



