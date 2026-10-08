students = [
    {
        "id": 1,
        "name": "Rahul",
        "age": 21,
        "course": "Python"
    },
    {
        "id": 2,
        "name": "Priya",
        "age": 22,
        "course": "Data Science"
    },
    {
        "id": 3,
        "name": "Amit",
        "age": 20,
        "course": "Java"
    }
]


def get_all_students():
    return students


def add_student(student_id, name, age, course):
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course
    }

    students.append(student)
    return student


def find_student(student_id):
    for student in students:
        if student["id"] == student_id:
            return student

    return None

def get_average_age():
    if not students:
        return 0

    total_age = sum(student["age"] for student in students)
    average_age = total_age / len(students)
    return average_age