def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
def contact_added(args,contacts):
    name, phone = args 
    contacts[name] = phone
    return "Contact updated"
def show_phone(args,contacts):
    name = args[0]
    try:
        return contacts[name]
    except:
        return f"User not found!"
def show_all(contacts):
    return contacts
def main():
    contacts = {}
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
            print(contact_added(args,contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")
if __name__ == "__main__":
    main()
