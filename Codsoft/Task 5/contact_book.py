
contacts = {}


def add_contact():
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")

    contacts[name] = {
        'phone_number': phone_number,
        'email': email,
        'address': address
    }
    print(f"Contact {name} added successfully.")


def view_contacts():
    if not contacts:
        print("Contact book is empty.")
    else:
        print("Contact List:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone Number: {info['phone_number']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            print('-' * 20)


def search_contact():
    search_term = input("Enter a name or phone number to search: ")
    found = False

    for name, info in contacts.items():
        if search_term.lower() in name.lower() or search_term in info['phone_number']:
            print(f"Name: {name}")
            print(f"Phone Number: {info['phone_number']}")
            print(f"Email: {info['email']}")
            print(f"Address: {info['address']}")
            found = True

    if not found:
        print("No matching contacts found.")


def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print(f"Updating contact: {name}")
        add_contact()  
    else:
        print(f"Contact {name} not found.")


def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully.")
    else:
        print(f"Contact {name} not found.")


while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting the Contact Book.")
        break
    else:
        print("Invalid choice. Please try again.")
