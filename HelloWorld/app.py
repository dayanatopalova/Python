age = 23
age = 30
print(age)

#concatenation
name = input("Enter your name: ")
print ("Hello " + name)

#type conversion
first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))

#string
course = 'Python for beginners' #the string here - bsc an object
print(course.find('y')) #character sensitive!
print(course.replace('y','*')) #methods do not modify the original string
print('Python' in course) #in-operator --> boolean output, .find --> index output

#arithmetic operators
print(10 / 3) #output --> floating point number
print(10 // 3) #output --> whole number
print (10 ** 3) # number to the power of another number

x = 10
x = x + 3
x += 3 #augmented assignment operator

x = 3 != 2
print(x) #output --> boolean

#boolean expressions
price = 5
print(price > 10 and price < 30) #both
print(price > 10 or price < 30) #at least one
print(not price > 10) #inverses any value that we give it

#comparison
temperature = 25

if temperature > 30:
    print("It's a hot day")
    print("Drink water")
elif temperature > 20: #short for else if --> new block of code
    print("It's a nice day")
elif temperature > 10:
    print("It's a bit cold day")
else:
    print("It's a cold day")
print("Done") #not indented --> gets executed always
    #in Python we use indentation instead of curly braces to mark that the lines belong to a certain block of code

#
weight = input("Weight: ")
unit = input ("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = float(weight) / 0.45
    print("Weight in Lbs is: " + str(converted))
else:
    converted = float(weight) * 0.45
    print("Weight in Kgs is: " + str(converted))

#while loops
i = 1
while i <= 5:
    print(i * '*') #we can multiply a number by a string :o :D
    i += 1 #no ++ or -- in Python


#complex types
#lists
names = ["Dayana", "Alex", "Svetla", "Milen"] #there are negative indexes in Python --> from last to first
print(names[0:3])

numbers = [1, 2, 3, 4, 5]
numbers.insert(1, 10)
print(numbers)
numbers.append(6)
print(1 in numbers) #output--> boolean
print(len(numbers))
numbers.remove(1)


#for loop
numbers = [1, 2, 3, 4, 5]
for item in numbers:
    print(item)

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1

