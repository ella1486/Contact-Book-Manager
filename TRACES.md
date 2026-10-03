# Contact Book Program – Trace Documentation

## (a) Trace: Looking Up a Contact That Was Never Added

**Scenario:** The user tries to look up a contact named "David", but David has not been added to the contact list.

**Initial contact list:**

```python
contacts = []
```

**Step-by-step trace:**

1. The `main()` function calls `display_menu()`.
2. `display_menu()` displays the menu and asks the user to choose an option.
3. The user enters `2` to look up a contact.
4. `display_menu()` returns `"2"` to `main()`.
5. `main()` calls `lookup_contact(contacts)`, passing the empty contact list.
6. `lookup_contact()` asks the user for a contact name.
7. The user enters `"David"`.
8. The function loops through the contact list but finds no matching contact because the list is empty.
9. `lookup_contact()` returns `None`.
10. Control goes back to `main()`.
11. `main()` checks whether the returned value is `None`.
12. Since it is `None`, the program displays `"Contact not found."`.
13. The `while True` loop starts another menu cycle.

**Final result:** The program handles the missing contact correctly without crashing.

---

## (b) Trace: Adding One Contact and Successfully Looking It Up

**Scenario:** The user adds Emmanuel with phone number 08012345678 and then looks up Emmanuel.

### Step 1: Program starts

The `main()` function creates an empty list:

```python
contacts = []
```

### Step 2: Display the menu

* `main()` calls `display_menu()`.
* `display_menu()` displays the available options.
* The user enters `"1"` to add a contact.
* `display_menu()` returns `"1"` to `main()`.

### Step 3: Add a contact

`main()` calls:

```python
add_contact(contacts)
```

**Value received by `add_contact()`:**

```python
[]
```

Inside `add_contact()`:

* The user enters the name `"Emmanuel"`.
* The user enters the phone number `"08012345678"`.
* The function creates a dictionary:

```python
{
    "name": "Emmanuel",
    "phone": "08012345678"
}
```

* The dictionary is appended to the contact list.

**Updated contact list:**

```python
[
    {
        "name": "Emmanuel",
        "phone": "08012345678"
    }
]
```

* `add_contact()` returns the updated contact list to `main()`.

### Step 4: Store the updated list

`main()` receives the returned list and assigns it back to `contacts`:

```python
contacts = add_contact(contacts)
```

The contact list now contains Emmanuel's name and phone number.

### Step 5: Display the menu again

* The `while True` loop repeats.
* `main()` calls `display_menu()`.
* The user enters `"2"` to look up a contact.
* `display_menu()` returns `"2"` to `main()`.

### Step 6: Look up the contact

`main()` calls:

```python
lookup_contact(contacts)
```

**Value received by `lookup_contact()`:**

```python
[
    {
        "name": "Emmanuel",
        "phone": "08012345678"
    }
]
```

Inside `lookup_contact()`:

* The user enters `"Emmanuel"`.
* The function loops through the contact list.
* It compares the entered name with the stored name.
* The names match.
* The function returns `"08012345678"` to `main()`.

### Step 7: Display the result

`main()` receives the phone number.

Since the returned value is not `None`, the program displays:

```text
Phone number: 08012345678
```

### Step 8: End of lookup

The program returns to the menu because the `while True` loop is still running.

The user can choose another operation or quit.

---

## Summary of Data Flow

| Function           | Receives     | Returns                |
| ------------------ | ------------ | ---------------------- |
| `main()`           | No arguments | Nothing explicitly     |
| `display_menu()`   | No arguments | User's menu choice     |
| `add_contact()`    | Contact list | Updated contact list   |
| `lookup_contact()` | Contact list | Phone number or `None` |

**Conclusion:**

The Contact Book Program uses function parameters and return values to transfer information between functions. The `main()` function controls the program, while the other functions perform specific tasks. The program also handles unsuccessful searches without crashing.
