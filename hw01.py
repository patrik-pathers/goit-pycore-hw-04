from pathlib import Path


def total_salary(path: str | Path) -> tuple[int | float, int | float]:
    """
    Аналізує файл із заробітними платами розробників і повертає
    загальну та середню суму заробітної плати всіх розробників.

    :param path: Шлях до текстового файлу з даними.
    :return: Кортеж із двох чисел (загальна сума, середня заробітна плата).
    """
    total = 0.0
    count = 0

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, start=1):
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue

                parts = cleaned_line.split(",")
                if len(parts) != 2:
                    raise ValueError(
                        f"Неправильний формат даних у рядку {line_num}: '{cleaned_line}'"
                    )

                _, salary_str = parts
                salary = float(salary_str)
                total += salary
                count += 1

        if count == 0:
            return 0, 0

        average = total / count
        total_res = int(total) if total.is_integer() else round(total, 2)
        average_res = int(average) if average.is_integer() else round(average, 2)

        return total_res, average_res

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return 0, 0
    except ValueError as e:
        print(f"Помилка обробки даних у файлі '{path}': {e}")
        return 0, 0
    except OSError as e:
        print(f"Помилка читання файлу '{path}': {e}")
        return 0, 0


if __name__ == "__main__":
    sample_file = Path(__file__).with_name("salary_file.txt")
    total, average = total_salary(sample_file)
    print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
