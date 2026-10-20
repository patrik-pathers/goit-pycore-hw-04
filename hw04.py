def parse_input(user_input: str) -> tuple[str, ...]:
    """
    Розбирає введений користувачем рядок на команду та її аргументи.
    Команда приводиться до нижнього регістру.
    """
    if not user_input.strip():
        return ("",)
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Додає новий контакт (ім'я та телефон) до словника контактів.
    """
    try:
        name, phone = args
    except ValueError:
        return "Give me name and phone please."
    contacts[name] = phone
    return "Contact added."


def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Змінює номер телефону для існуючого контакту в словнику.
    """
    try:
        name, phone = args
    except ValueError:
        return "Give me name and phone please."
    if name not in contacts:
        return "Contact not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Повертає номер телефону для зазначеного контакту за його ім'ям.
    """
    try:
        name = args[0]
    except IndexError:
        return "Enter user name."
    if name not in contacts:
        return "Contact not found."
    return contacts[name]


def show_all(contacts: dict[str, str]) -> str:
    """
    Повертає всі збережені контакти з номерами телефонів.
    """
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main() -> None:
    """
    Головна функція, що управляє основним циклом обробки команд CLI-бота.
    Усі виклики input() та print() відбуваються виключно тут.
    """
    contacts: dict[str, str] = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
