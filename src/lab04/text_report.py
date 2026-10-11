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
