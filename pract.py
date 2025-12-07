# number1 = int(input("Enter num1: "))
# number2 = int(input("Enter num2: "))
# operation = input("Enter operation (add/subtract/multiply/divide): ")
# add = number1 + number2
# subtract = number1 - number2
# multiply = number1 * number2
# divide = number1 / number2 if number2 != 0 else None
# if operation == "add":
#     print(f"The sum is: {add}")
# elif operation == "subtract":
#     print(f"The difference is: {subtract}")
# elif operation == "multiply":
#     print(f"The product is: {multiply}")
# elif operation == "divide":
#     if divide is not None:
#         print(f"The quotient is: {divide}")
#     else:
#         print("Cannot divide by zero")

# name = input("Please type in your name: ")

# if name == "Huey" or name == "Dewey" or name == "Louie":
#     print("I think you might be one of Donald Duck's nephews.")
# elif name == "Morty" or name == "Ferdie":
#     print("I think you might be one of Mickey Mouse's nephews.")
# else:
#     print("You're not a nephew of any character I know of.")


# attempts = 0

# while True:
#     code = input("Please type in your PIN: ")
#     attempts += 1

#     if attempts == 3:
#         success = False
#         break

#     if code == "1234":
#         success = True
#         break

#     print("Incorrect...try again")

# if success:
#     print("Correct PIN entered!")
# else:
#     print("Too many attempts...")

# upperLimit = int(input("Please type in a number: "))
# base = int(input("Please type in a base: "))

# num = 1

# while(num <= upperLimit):
#     print(num)
#     num*=base

# limit = int(input("Please type in a number: "))

# i = 1

# while i <= limit:
#     j = 1
#     while j <= limit:
#         print(f"{i} x {j} = {i * j}")
#         j += 1
#     i += 1

def arithmeticMean(n1, n2, n3):
    res = (n1 + n2 + n3) / 3
    print(f"The arithmetic mean is: {res}")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
mean = arithmeticMean(num1, num2, num3)
 