# Лабораторная работа 3
## Задание 1
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    if not isinstance(text, str):
        raise TypeError

    if casefold:
        text = text.casefold()
    else:
        text = text.lower()

    if yo2e:
        text = text.replace("ё", "е")
        text = text.replace("Ё", "Е")
        ''' уже произошла замена заглавных букв на строчные,
        но т.к. в условии написано, сделаю и такую замену '''

    text = text.replace("\t", " ")
    text = text.replace("\r", " ")
    text = text.replace("\n", " ")

    text = text.strip()
    text = ' '.join(text.split())

    return text

import re

```
![скрин 1](images/lab03/img1.1.png)

```python
def tokenize(text: str) -> list[str]:

    words_re = r"\w+(?:-\w+)*"
    words = re.findall(words_re, text)

    return words
```
![скрин 2](images/lab03/img1.1.png)

```python
def count_freq(tokens: list[str]) -> dict[str, int]:

    freq = {} # создаём пустой словарь

    for token in tokens: # по очереди берём каждое слово из списка tokens
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1

    return freq
```
![скрин 3](images/lab03/img1.1.png)

```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    
    items = list(freq.items())
    items.sort(key=lambda item: (-item[1], item[0]))
    
    return items[:n]

```
![скрин 4](images/lab03/img1.1.png) #Заскриншоть и вставь в папку имагес лаб03 везде так

## Задание 2
```python
from src.lib.text import normalize, tokenize, count_freq, top_n


TABLE_MODE = True

text = input()

normalized_text = normalize(text)
tokens = tokenize(normalized_text)
frequencies = count_freq(tokens)
popular_words = top_n(frequencies, 5)

print(f"Всего слов: {len(tokens)}")
print(f"Уникальных слов: {len(frequencies)}")
print("Топ-5:")

if TABLE_MODE:
    word_width = len("слово")

    for word, count in popular_words:
        if len(word) > word_width:
            word_width = len(word)

    print(f"{'слово':<{word_width}} | частота")
    print("-" * (word_width + 10))

    for word, count in popular_words:
        print(f"{word:<{word_width}} | {count}")

else:
    for word, count in popular_words:
        print(f"{word}:{count}")
```
![скрин 1](images/lab03/img1.1.png) #Заскриншоть и вставь в папку имагес лаб03 везде так