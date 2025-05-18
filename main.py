from student_db import *

def menu():
    while True:
        print("\n🎓 Student Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            course = input("Enter course: ")
            add_student(name, age, course)
            print("✅ Student added successfully.")

        elif choice == '2':
            students = get_all_students()
            print("\n📋 All Students:")
            for student in students:
                print(f"ID: {student[0]} | Name: {student[1]} | Age: {student[2]} | Course: {student[3]}")

        elif choice == '3':
            student_id = int(input("Enter student ID to update: "))
            name = input("New name: ")
            age = int(input("New age: "))
            course = input("New course: ")
            update_student(student_id, name, age, course)
            print("✅ Student updated successfully.")

        elif choice == '4':
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)
            print("❌ Student deleted successfully.")

        elif choice == '5':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice. Try again.")

# Initialize DB and run menu
connect_db()
menu()
