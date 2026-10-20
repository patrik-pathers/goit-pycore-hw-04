import sys
from pathlib import Path
from colorama import init, Fore, Style


def display_directory_structure(directory_path: Path, indent: int = 0) -> None:
    """
    Рекурсивно обходить директорію та виводить імена всіх піддиректорій
    та файлів із кольоровим форматуванням.

    :param directory_path: Об'єкт Path до директорії.
    :param indent: Рівень вкладеності для відступів.
    """
    if indent == 0:
        root_name = directory_path.name or directory_path.resolve().name
        print(f"{Fore.BLUE}{root_name}/{Style.RESET_ALL}")
        indent = 1

    prefix = "    " * indent

    try:
        # Сортуємо елементи за алфавітом без урахування регістру
        items = sorted(directory_path.iterdir(), key=lambda p: p.name.lower())
    except PermissionError:
        print(f"{prefix}{Fore.RED}[Відмовлено в доступі до '{directory_path.name}']{Style.RESET_ALL}")
        return
    except OSError as e:
        print(f"{prefix}{Fore.RED}[Помилка читання '{directory_path.name}': {e}]{Style.RESET_ALL}")
        return

    for item in items:
        if item.is_dir():
            print(f"{prefix}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
            display_directory_structure(item, indent + 1)
        else:
            print(f"{prefix}{Fore.GREEN}{item.name}{Style.RESET_ALL}")


def main() -> None:
    # Ініціалізація colorama для коректної роботи кольорів у терміналі
    init(autoreset=True)

    # Перевірка наявності аргументу командного рядка
    if len(sys.argv) < 2:
        print(
            f"{Fore.RED}Помилка: Будь ласка, вкажіть шлях до директорії як аргумент командного рядка.{Style.RESET_ALL}"
        )
        print(f"Приклад використання: python {Path(sys.argv[0]).name} /шлях/до/вашої/директорії")
        sys.exit(1)

    target_path = Path(sys.argv[1])

    # Перевірка, чи існує вказаний шлях
    if not target_path.exists():
        print(f"{Fore.RED}Помилка: Вказаний шлях '{target_path}' не існує.{Style.RESET_ALL}")
        sys.exit(1)

    # Перевірка, чи веде шлях саме до директорії
    if not target_path.is_dir():
        print(
            f"{Fore.RED}Помилка: Вказаний шлях '{target_path}' не є директорією.{Style.RESET_ALL}"
        )
        sys.exit(1)

    display_directory_structure(target_path)


if __name__ == "__main__":
    main()
