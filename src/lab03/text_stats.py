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