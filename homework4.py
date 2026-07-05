def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Contact not found."
        except IndexError:
            return "Enter the argument for the command"
    return inner
@input_error
def parse_input(user_input: str) -> tuple[str, list[str]]:
    parts = user_input.split()
    if not parts:
        return "", []
    cmd = parts[0].strip().lower()
    args = parts[1:]
    return cmd, args
@input_error
def add_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Додає новий контакт у словник contacts. Очікує, що args містить ім'я та номер телефону.
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."
@input_error
def change_contact(args: list[str], contacts: dict[str, str]) -> str:
    """
    Оновлює номер телефону існуючого контакту. Очікує, що args містить ім'я та новий номер телефону.
    """
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."
@input_error
def show_phone(args: list[str], contacts: dict[str, str]) -> str:
    """
    Показує номер телефону для заданого контакту. Очікує, що args містить ім'я контакту.
    """
    name = args[0]
    return contacts[name]
def show_all(contacts: dict[str, str]) -> str:
    """
    Функція для відображення всіх контактів у словнику contacts. Повертає рядок з усіма контактами.
    """
    if not contacts:
        return "No contacts stored yet."
    lines = [f"{name}: {phone}" for name, phone in contacts.items()]
    return "\n".join(lines)
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    
    while True:
        try:
            user_input = input("Enter a command: ")
        except (KeyboardInterrupt, EOFError):
            print("\nGood bye!")
            break
        command, args = parse_input(user_input)
        if not command:
            continue
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