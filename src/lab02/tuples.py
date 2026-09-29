def format_record(rec: tuple[str, str, float]) -> str:

    # Проверяем количество элементов
    if len(rec) != 3:
        raise ValueError

    # Получаем ФИО, группу и GPA
    fio, group, gpa = rec

    # Проверяем типы
    if not isinstance(fio, str):
        raise TypeError

    if not isinstance(group, str):
        raise TypeError

    if not isinstance(gpa, (int, float)):
        raise TypeError

    # Убираем лишние пробелы
    fio = " ".join(fio.split())
    group = group.strip()

    # Проверяем, что ФИО и группа не пустые
    if not fio:
        raise ValueError

    if not group:
        raise ValueError

    # Разделяем ФИО на слова
    parts = fio.split()

    # нужно указать минимум фамилию и имя
    if len(parts) < 2:
        raise ValueError

    # Первое слово — фамилия
    surname = parts[0].capitalize()

    # Получаем инициалы имени и отчества
    initials = ""

    for word in parts[1:3]:
        initials += word[0].upper() + "."

    # Формируем результат
    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"


if __name__ == "__main__":
    print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
    print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
    print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
    print(format_record(("  сидорова  анна  сергеевна ", "ABB-01", 3.999)))
    # print(format_record(("", "ABB-01", 3.999)))
    # print(format_record(("  сидорова  анна  сергеевна ", "", 3.999)))
    print(format_record(("  сидорова  анна  сергеевна ", "ABB-01", "3.999")))
