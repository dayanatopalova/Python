def create_employee(name, salary):
    return {"name": name, "salary": salary}

def input_employee():
    employees = []

    while True:
        employee = input("Enter the name of an employee or 'stop': ")

        if employee.lower() == "stop":
            break

        salary = float(input("Enter the monthly salary of the employee: "))

        employee = create_employee(employee, salary)
        employees.append(employee)

    return employees

def average_salary(employees):

    count = 0
    total = 0

    for person in employees:
        count += 1
        total += person["salary"]

    average = total / count

    return average

def highest_paid_employee(employees):
    highest = employees[0]

    for person in employees:
        if person["salary"] > highest["salary"]:
            highest = person

    return highest

def employees_above_below(employees):
    number = float(input("Enter a sum to compare: "))

    above = []
    below = []
    same = []
    for person in employees:
        if person["salary"] > number:
            above.append(person)
        elif person["salary"] < number:
            below.append(person)
        else:
            same.append(person)

    return {"employees with salary above the sum": above,
            "employees with salary below the sum": below,
            "employees with the same salary as the sum": same}

employees = input_employee()
print(employees)
print(f"The average monthly salary of the employees is: {average_salary(employees)}")
print(f"The highest paid employee is {highest_paid_employee(employees)}")
print(employees_above_below(employees))

