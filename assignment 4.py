#assignment four
#Student Record Management System (SRMS)
students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort Students by Marks")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        roll = input("Enter roll no: ")
        subject = input("Enter subject: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "roll": roll, "subject": subject, "marks": marks})

    elif choice == '2':
        for s in students:
            print(s)

    elif choice == '3':
        roll = input("Enter roll no: ")
        for s in students:
            if s["roll"] == roll:
                print(s)
                break
        else:
            print("Not found")

    elif choice == '4':
        roll = input("Enter roll no: ")
        for s in students:
            if s["roll"] == roll:
                s["marks"] = int(input("Enter new marks: "))
                break

    elif choice == '5':
        roll = input("Enter roll no: ")
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                break

    elif choice == '6':
        students.sort(key=lambda x: x["marks"], reverse=True)

    elif choice == '7':
        break
students = []

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Sort Students by Marks")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        name = input("Enter name: ")
        roll = input("Enter roll no: ")
        subject = input("Enter subject: ")
        marks = int(input("Enter marks: "))
        students.append({"name": name, "roll": roll, "subject": subject, "marks": marks})

    elif choice == '2':
        for s in students:
            print(s)

    elif choice == '3':
        roll = input("Enter roll no: ")
        for s in students:
            if s["roll"] == roll:
                print(s)
                break
        else:
            print("Not found")

    elif choice == '4':
        roll = input("Enter roll no: ")
        for s in students:
            if s["roll"] == roll:
                s["marks"] = int(input("Enter new marks: "))
                break

    elif choice == '5':
        roll = input("Enter roll no: ")
        for s in students:
            if s["roll"] == roll:
                students.remove(s)
                break

    elif choice == '6':
        students.sort(key=lambda x: x["marks"], reverse=True)

    elif choice == '7':
        break
