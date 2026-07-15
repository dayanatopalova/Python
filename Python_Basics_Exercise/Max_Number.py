numbers = []

while True:
    value = input("Enter a number or 'stop' - command: ")


    if value.lower() == "stop":
        break

    numbers.append(int(value))

if not numbers:
    print("You have to enter at least one number first.")
else:
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    print(f"The number {largest} is the largest one.")
