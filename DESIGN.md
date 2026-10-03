# Contact Book Program – Design

## 1. Program Overview

The Contact Book Program allows users to add contacts (names and phone numbers) and look up saved contacts by name during one program run.

## 2. Function Breakdown (Top-Down Design)

### 1. add_contact()

* Ask the user for a contact's name.
* Ask the user for their phone number.
* Store the name and phone number in the contact list.
* Confirm that the contact has been added.

### 2. lookup_contact()

* Ask the user for the name of the contact to search for.
* Search the contact list for the name.
* Display the phone number if the contact is found.
* Display an appropriate message if the contact is not found.

### 3. display_menu()

* Display the available options:

  * Add a contact.
  * Look up a contact.
  * Exit the program.
* Get the user's menu choice.

### 4. main()

* Create an empty contact list.
* Display the main menu.
* Process the user's choice.
* Call the appropriate function.
* Repeat the menu until the user chooses to exit.

## 3. Program Flow

1. Start the program.
2. Create an empty contact list.
3. Display the main menu.
4. Get the user's choice.
5. If the user chooses to add a contact, call `add_contact()`.
6. If the user chooses to look up a contact, call `lookup_contact()`.
7. If the user chooses to exit, stop the program.
8. Repeat until the user exits.
