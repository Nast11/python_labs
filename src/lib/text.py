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

def tokenize(text: str) -> list[str]:

    words_re = r"\w+(?:-\w+)*"
    words = re.findall(words_re, text)

    return words

def count_freq(tokens: list[str]) -> dict[str, int]:

    freq = {} # создаём пустой словарь

    for token in tokens: # по очереди берём каждое слово из списка tokens
        if token in freq:
            freq[token] += 1
        else:
            freq[token] = 1

    return freq

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    
    items = list(freq.items())
    items.sort(key=lambda item: (-item[1], item[0]))
    
    return items[:n]

if __name__ == "__main__":
    pass

    # Тесты normalize
    # print(normalize("ПрИвЕт\nМИр\t"))
    # print(normalize("ёжик, Ёлка", yo2e=True))
    # print(normalize("Hello\r\nWorld"))
    # print(normalize("  двойные   пробелы  "))

     # Тесты tokenize
    # print(tokenize("привет мир"))
    # print(tokenize("hello,world!!!"))
    # print(tokenize("по-настоящему круто"))
    # print(tokenize("2025 год"))
    # print(tokenize("emoji 😀 не слово"))

    # # Первый тест count_freq и top_n
    # tokens_1 = ["a", "b", "a", "c", "b", "a"]
    # frequencies_1 = count_freq(tokens_1)

    # print(frequencies_1)
    # print(top_n(frequencies_1, n=2))

    # # Второй тест count_freq и top_n
    # tokens_2 = ["bb", "aa", "bb", "aa", "cc"]
    # frequencies_2 = count_freq(tokens_2)

    # print(frequencies_2)
    # print(top_n(frequencies_2, n=2))
