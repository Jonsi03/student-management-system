import csv
import os

class Student:

    def __init__(self, sid, name, age, course):
        self.id = sid
        self.name = name
        self.age = age
        self.course = course

    def display(self):
        print("-" * 35)
        print("ID      :", self.id)
        print("Name    :", self.name)
        print("Age     :", self.age)
        print("Course  :", self.course)
        print("-" * 35)


students = []

# Load Data Automatically
if os.path.exists("students.csv"):

    with open("students.csv", "r", newline="") as file:

        reader = csv.DictReader(file)

        for row in reader:

            student = Student(
                int(row["ID"]),
                row["Name"],
                int(row["Age"]),
                row["Course"]
            )

            students.append(student)

print("Welcome To Student Management System")

while True:

    print("\n========== MENU ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Save Data")
    print("7. Exit")

    try:
        choice = int(input("Enter Choice : "))
    except ValueError:
        print("Please Enter Valid Number.")
        continue

    # ---------------- Add Student ---------------- #

    if choice == 1:

        try:

            sid = int(input("Enter Student ID : "))

            duplicate = False

            for i in students:

                if i.id == sid:
                    duplicate = True
                    break

            if duplicate:
                print("Student ID Already Exists.")
                continue

            name = input("Enter Student Name : ")

            age = int(input("Enter Student Age : "))

            if age <= 0:
                print("Invalid Age.")
                continue

            course = input("Enter Course : ")

            student = Student(
                sid,
                name,
                age,
                course
            )

            students.append(student)

            print("Student Added Successfully.")

        except ValueError:
            print("Invalid Input.")

            # ---------------- View Students ---------------- #

    elif choice == 2:

        if len(students) == 0:
            print("No Students Found.")

        else:

            print("\n===== STUDENT LIST =====")

            for i in students:

                i.display()

            print("Total Students :", len(students))

    # ---------------- Search Student ---------------- #

    elif choice == 3:

        print("\n1. Search By ID")
        print("2. Search By Name")

        option = input("Enter Choice : ")

        found = False

        if option == "1":

            try:

                sid = int(input("Enter Student ID : "))

                for i in students:

                    if i.id == sid:

                        i.display()
                        found = True
                        break

            except ValueError:

                print("Invalid ID.")

        elif option == "2":

            name = input("Enter Student Name : ")

            for i in students:

                if i.name.lower() == name.lower():

                    i.display()
                    found = True

        else:

            print("Invalid Choice.")

        if found == False:

            print("Student Not Found.")

            # ---------------- Update Student ---------------- #

    elif choice == 4:

        try:

            sid = int(input("Enter Student ID : "))

            found = False

            for i in students:

                if i.id == sid:

                    print("\nLeave Blank If You Don't Want To Change.")

                    name = input("Enter New Name : ")

                    if name != "":
                        i.name = name

                    age = input("Enter New Age : ")

                    if age != "":

                        age = int(age)

                        if age > 0:
                            i.age = age

                    course = input("Enter New Course : ")

                    if course != "":
                        i.course = course

                    print("Student Updated Successfully.")

                    found = True
                    break

            if found == False:
                print("Student Not Found.")

        except ValueError:

            print("Invalid Input.")


    # ---------------- Delete Student ---------------- #

    elif choice == 5:

        try:

            sid = int(input("Enter Student ID : "))

            found = False

            for i in students:

                if i.id == sid:

                    students.remove(i)

                    print("Student Deleted Successfully.")

                    found = True

                    break

            if found == False:

                print("Student Not Found.")

        except ValueError:

            print("Invalid Input.")


    # ---------------- Save Data ---------------- #

    elif choice == 6:

        with open("students.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["ID", "Name", "Age", "Course"])

            for i in students:

                writer.writerow([
                    i.id,
                    i.name,
                    i.age,
                    i.course
                ])

        print("Students Saved Successfully.")


    # ---------------- Exit ---------------- #

    elif choice == 7:

        with open("students.csv", "w", newline="") as file:

            writer = csv.writer(file)

            writer.writerow(["ID", "Name", "Age", "Course"])

            for i in students:

                writer.writerow([
                    i.id,
                    i.name,
                    i.age,
                    i.course
                ])

        print("Data Saved Successfully.")
        print("Thank You.")
        break


    else:

        print("Invalid Choice.")