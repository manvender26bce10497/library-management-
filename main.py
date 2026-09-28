

# Library Management System

library = {
    "Python Programming": {
        "location": "Shelf A1",
        "number": "B001",
        "stock": 5
    },
    "Data Structures": {
        "location": "Shelf A2",
        "number": "B002",
        "stock": 3
    },
    "Computer Networks": {
        "location": "Shelf B1",
        "number": "B003",
        "stock": 4
    },
    "Engineering Mathematics": {
        "location": "Shelf B2",
        "number": "B004",
        "stock": 6
    }
}


while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Search Book")
    print("2. Add Book")
    print("3. Show All Books")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter book name: ")

        if name in library:
            book = library[name]

            print("\nBook Found!")
            print("Book Name :", name)
            print("Book Number :", book["number"])
            print("Location :", book["location"])
            print("Available Stock :", book["stock"])
        else:
            print("Book not found!")

    elif choice == "2":
        name = input("Enter book name: ")
        number = input("Enter book number: ")
        location = input("Enter book location: ")
        stock = int(input("Enter stock: "))

        library[name] = {
            "number": number,
            "location": location,
            "stock": stock
        }

        print("Book added successfully!")

    elif choice == "3":
        print("\n===== ALL BOOKS =====")

        for name, book in library.items():
            print("\nBook Name :", name)
            print("Book Number :", book["number"])
            print("Location :", book["location"])
            print("Stock :", book["stock"])

    elif choice == "4":
        print("Thank you for using Library Management System!")
        break

    else:
        print("Invalid choice!")