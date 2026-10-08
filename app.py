from students import get_all_students, add_student, find_student


def display_students():
    print("\n--- Student List ---")

    for student in get_all_students():
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Age: {student['age']} | "
            f"Course: {student['course']}"
        )


def main():
    print("Student Management System")

    display_students()

    print("\nAdding new student...")

    student = add_student(
        4,
        "Sneha",
        21,
        "Python"
    )

    print("Added:", student)

    print("\nSearching for student ID 2...")

    result = find_student(2)

    if result:
        print("Student found:", result)
    else:
        print("Student not found")

from students import get_average_age

if __name__ == "__main__":
    main()
    print("\nAverage Age of Students:", get_average_age())

