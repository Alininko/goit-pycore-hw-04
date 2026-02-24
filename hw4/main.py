"""Program interacting with user imputs"""


def parse_input(user_input) -> str: #parsing user input, saving 1st element as a command, the rest as arguments in lower case
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def add_contact(args, contacts) -> str: #adding a contact
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts) -> str: #changing an existing contact number
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    return "Contact not found."


def show_phone(args, contacts) -> str: #printing an existing contact name and phone
    name = args[0]
    if name in contacts:
        return contacts[name]
    return "Contact not found."


def show_all(contacts) -> str: #printing all contacts from the list
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main(): # main logics
    contacts = {}
    print("Welcome to the assistant bot!")

    while True: #creating a loop, waiting for a user input
        user_input = input("Enter a command: ")
        if not user_input.strip():
            print("Invalid command.")
            continue

        command, *args = parse_input(user_input) #parsing an input as a command and arguments in lower case and without spaces

        if command in ["close", "exit"]: #exiting the loop is the command is close or exit
            print("Good bye!")
            break

        elif command == "hello": #logic for hello command
            print("How can I help you?")

        elif command == "add": #logic for add command
                print(add_contact(args, contacts))

        elif command == "change": #logic for change command
                print(change_contact(args, contacts))

        elif command == "phone": #logic for phone command
                print(show_phone(args, contacts))

        elif command == "all": #logic for all command
            print(show_all(contacts))

        else: #message for a non existing command
            print("Invalid command.")



if __name__ == "__main__":
    main()