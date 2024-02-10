contact = {}


def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key, contact.get(key)))


while True:
    try:
        choice = int(input("1. Add new Contact \n 2. Search new Contact \n 3.Display Contact\n 4. Edit Contact \n 5. Delete Contact\n 6. Exit\n Enter Your Choice  "))
        if choice in range(1, 7):
            if choice == 1:
                Name = input("Enter the contact name")
                Phone = input("Enter the Mobile Number")
                contact[Name] = Phone
            elif choice == 2:
                search_name = input("Enter the contact ")
                if search_name in contact:
                    print(search_name, "'s contact number is", contact[search_name])
                else:
                    print("Name is not found in contact book")
            elif choice == 3:
                if not contact:
                    print("empty contact book")
                else:
                    display_contact()
            elif choice == 4:
                edit_contact = input("Enter the contact to be edited")
                if edit_contact in contact:
                    phone = input("enter mobile number")
                    contact[edit_contact] = phone
                    print("contact updated")
                    display_contact()
                else:
                    print("Name is not found in contact book")
            elif choice == 5:
                del_contact = input("Enter the contact to be deleted")
                if del_contact in contact:
                    confirm = input("Do you want to delete this contact y/n?")
                    if confirm == 'y' or confirm == 'Y':
                        contact.pop(del_contact)
                    display_contact()
                else:
                    print("Name is not found in the contact book")
            elif choice == 6:
                break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
    except ValueError:
        print("Invalid input. Please enter a number.")
