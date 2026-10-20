from pathlib import Path


def get_cats_info(path: str | Path) -> list[dict[str, str]]:
    """
    Читає файл з інформацією про котів та повертає список словників
    із ключами "id", "name", "age".

    :param path: Шлях до текстового файлу з даними про котів.
    :return: Список словників з інформацією про кожного кота.
    """
    cats_info: list[dict[str, str]] = []

    try:
        with open(path, mode="r", encoding="utf-8") as file:
            for line_num, line in enumerate(file, start=1):
                cleaned_line = line.strip()
                if not cleaned_line:
                    continue

                parts = cleaned_line.split(",")
                if len(parts) != 3:
                    raise ValueError(
                        f"Неправильний формат даних у рядку {line_num}: '{cleaned_line}'"
                    )

                cat_id, name, age = parts
                cats_info.append({
                    "id": cat_id.strip(),
                    "name": name.strip(),
                    "age": age.strip(),
                })

        return cats_info

    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
        return []
    except ValueError as e:
        print(f"Помилка обробки даних у файлі '{path}': {e}")
        return []
    except OSError as e:
        print(f"Помилка читання файлу '{path}': {e}")
        return []


if __name__ == "__main__":
    sample_file = Path(__file__).with_name("cats_file.txt")
    cats_info = get_cats_info(sample_file)
    print(cats_info)
