def input_grades():
    grades = []

    while True:
        value = input("Enter a grade or 'stop': ")
        if value.lower() == "stop":
            break
        grades.append(int(value))

    return grades

def create_student(name, grades):
    average = round(sum(grades) / len(grades), 2)
    return {"name": name, "average grade": average}

students = []

while True:
    name = input("Enter student name or 'stop': ")

    if name.lower() == "stop":
        break

    print(f"Enter grades for {name} ")
    grades = input_grades()
    student = create_student(name, grades)
    students.append(student)

print(students)