# Лабораторная работа 4

## Задание A

Реализованы функции чтения текста, создания родительской папки и записи CSV-файла. По умолчанию текст читается в UTF-8. Другую кодировку можно передать через параметр `encoding`, например `encoding="cp1251"`.

```python
import csv
from pathlib import Path


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """Прочитать файл. Кодировку можно указать через encoding."""
    file_path = Path(path)
    return file_path.read_text(encoding=encoding)


def ensure_parent_dir(path: str | Path) -> None:
    """Создать родительскую папку, если её нет."""
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)


def write_csv(
    rows: list[tuple | list],
    path: str | Path,
    header: tuple[str, ...] | None = None,
) -> None:
    """Записать строки одинаковой длины в CSV-файл."""
    expected_length = len(header) if header is not None else None

    for row in rows:
        if not isinstance(row, (tuple, list)):
            raise TypeError("строка CSV должна быть кортежем или списком")

        if expected_length is None:
            expected_length = len(row)
        elif len(row) != expected_length:
            raise ValueError("все строки CSV должны иметь одинаковую длину")

    file_path = Path(path)
    ensure_parent_dir(file_path)

    with file_path.open("w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=",", lineterminator="\n")

        if header is not None:
            writer.writerow(header)

        writer.writerows(rows)
```

![Чтение TXT и запись CSV](/images/lab04/img4.1.png)

Проверка строк разной длины:

```python
from src.lab04.io_txt_csv import write_csv

write_csv([("word", 1), ("bad",)], "/tmp/bad.csv")
```

Если строки содержат разное количество элементов, функция поднимает `ValueError`.

![Ошибка при разной длине строк CSV](/images/lab04/img4.2.png)

## Задание B

Скрипт читает текстовый файл, использует функции `normalize`, `tokenize`, `count_freq` и `top_n` из ЛР3, сохраняет CSV-отчёт и выводит краткую статистику в консоль.

```python
import argparse
import sys
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.lab04.io_txt_csv import read_text, write_csv
from src.lib.text import count_freq, normalize, tokenize, top_n


DEFAULT_INPUT_PATH = PROJECT_ROOT / "data" / "lab04" / "input.txt"
DEFAULT_OUTPUT_PATH = PROJECT_ROOT / "data" / "lab04" / "report.csv"


def frequencies_from_text(text: str) -> dict[str, int]:
    """Посчитать частоты слов в тексте."""
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    return count_freq(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    """Отсортировать слова по частоте и алфавиту."""
    return top_n(freq, len(freq))


def create_report(
    input_path: str | Path,
    output_path: str | Path,
    encoding: str = "utf-8",
) -> tuple[int, dict[str, int]]:
    """Создать CSV-отчёт и вернуть статистику."""
    text = read_text(input_path, encoding=encoding)
    frequencies = frequencies_from_text(text)
    rows = sorted_word_counts(frequencies)

    write_csv(rows, output_path, header=("word", "count"))
    return sum(frequencies.values()), frequencies


def print_summary(total_words: int, frequencies: dict[str, int]) -> None:
    """Напечатать краткую статистику."""
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {len(frequencies)}")
    print("Топ-5:")

    for word, count in top_n(frequencies, 5):
        print(f"{word}:{count}")


def parse_args() -> argparse.Namespace:
    """Получить аргументы командной строки."""
    parser = argparse.ArgumentParser(
        description="Создание CSV-отчёта со статистикой слов."
    )
    parser.add_argument(
        "--in",
        dest="input_path",
        type=Path,
        default=DEFAULT_INPUT_PATH,
        help="путь к входному TXT-файлу",
    )
    parser.add_argument(
        "--out",
        dest="output_path",
        type=Path,
        default=DEFAULT_OUTPUT_PATH,
        help="путь к выходному CSV-файлу",
    )
    parser.add_argument(
        "--encoding",
        default="utf-8",
        help="кодировка входного файла, по умолчанию utf-8",
    )
    return parser.parse_args()


def main() -> None:
    """Создать отчёт и вывести статистику."""
    args = parse_args()
    total_words, frequencies = create_report(
        args.input_path,
        args.output_path,
        encoding=args.encoding,
    )
    print_summary(total_words, frequencies)


if __name__ == "__main__":
    main()
```

Программа читает UTF-8-файл, создаёт `report.csv` с колонками `word,count` и сортирует строки по убыванию частоты, затем по слову в алфавитном порядке.

![Базовый отчёт по тексту](/images/lab04/img4.3.png)

Проверка пустого входного файла:

```python
rows = sorted_word_counts(frequencies)
write_csv(rows, output_path, header=("word", "count"))
```

Для пустого файла выбрана такая политика: CSV содержит только заголовок `word,count`. В консоли выводится нулевое количество всех и уникальных слов.

![Отчёт для пустого файла](/images/lab04/img4.4.png)

Проверка входного файла в кодировке `cp1251`:

```python
parser.add_argument(
    "--encoding",
    default="utf-8",
    help="кодировка входного файла, по умолчанию utf-8",
)

text = read_text(input_path, encoding=encoding)
```

Кодировка входного файла передаётся через `--encoding cp1251`. CSV-отчёт независимо от входной кодировки записывается в UTF-8.

![Чтение файла в кодировке cp1251](/images/lab04/img4.5.png)

## Запуск
Запуск с путями по умолчанию:

```bash
python -m src.lab04.text_report
```

При таком запуске читает `data/lab04/input.txt` и записывает отчёт в `data/lab04/report.csv`.

Запуск с произвольными путями:

```bash
python src/lab04/text_report.py --in data/lab04/input.txt --out data/lab04/report.csv
```

Запуск с другой кодировкой:

```bash
python src/lab04/text_report.py --in data/input.txt --out data/report.csv --encoding cp1251
```

## Обязательные условия

- Входные файлы читаются в UTF-8, кодировка может быть указана.
- CSV-файлы записываются в UTF-8 с разделителем `,`.
- Если входной файл отсутствует, возникает `FileNotFoundError`.
- Если кодировка указана неверно, возникает `UnicodeDecodeError`.
- Пустой входной файл создаёт отчёт только с заголовком `word,count`.
- `write_csv` без строк и без заголовка создаёт пустой файл.
- `write_csv` без строк, но с заголовком создаёт файл только с заголовком.
- В этой работе файл разрешено читать целиком. Для очень больших файлов на практике лучше использовать построчное чтение, чтобы не хранить весь текст в памяти.
