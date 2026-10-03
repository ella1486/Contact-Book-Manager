def add_contact(contacts):
    """Add a new contact to the contact list and return the updated list."""
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")

    contacts.append({
        "name": name,
        "phone": phone
    })

    print(f"{name} has been added successfully.")
    return contacts


def lookup_contact(contacts):
    """Look up a contact by name and return the phone number or None."""
    name = input("Enter contact name to look up: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact["phone"]

    return None


def display_menu():
    """Display the main menu and return the user's selected option."""
    print("\nContact Book")
    print("1. Add contact")
    print("2. Look up contact")
    print("3. Exit")

    return input("Choose an option: ")


def main():
    """Run the contact book program until the user chooses to exit."""
    contacts = []

    while True:
        choice = display_menu()

        if choice == "1":
            contacts = add_contact(contacts)

        elif choice == "2":
            phone = lookup_contact(contacts)

            if phone is not None:
                print(f"Phone number: {phone}")
            else:
                print("Contact not found.")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()