"""for"""
# multiplication table
for i in range(1, 10):
    for j in range(1, 10):
        print(i * j, end="\t")
    print("\n")


# number = int(input("Enter the number: "))
# factorial = 1
# for i in range(1, number + 1):
#     factorial *= i
# print("The factorial of the number", number, "is", factorial)

"""while"""
# number = int(input("Enter the number: "))
# i = 1
# factorial = 1
# while i <= number:
#     factorial *= i
#     i += 1
#
# print("The factorial of the ", number, "is", factorial)

# choice = "y"
#
# while choice.lower() == "y":
#     print("Hello")
#     choice = input("To continue, press Y, and to exit any other key: ")
#
# print("The program is completed")

"""if elif else"""
# Exchange office - program
# usd = 28
# euro = 32
#
# money = int(input("Enter the amount you want to exchange: "))
# currency = int(input("Enter the currency code (dollars - 400, euro - 401): "))
#
# if currency == 400:
#     cash = round(money / usd, 2)
#     print("Currency: dollars USA")
# elif currency == 401:
#     cash = round(money / euro, 2)
#     print("Currency: euro")
# else:
#     cash = 0
#     print("Unknown currency")
#
# print("To be received: ", cash)

# age = 22
# if age > 21:
#     print("Access is allowed")
# else:
#     print("Access in denied")

"""strings"""
# print("Cafe \"Central Park\"")

# print("Time to grown up\nNOW!")
# name = "Tom"
# age = 33
# info = "Name: " + name + " Age: " + str(age)
# print(info)

"""True or False"""
# age = 22
# isMarried = False
# result = age > 21 or isMarried
# print(result)

# age = 27
# weight = 68
# result = age > 21 and weight == 68
# print(result)

# a = 5
# b = 6
# result = 5 == 6
# print(result)
# print(a != b)
# print(a > b)
# print(a < b)
#
# bool1 = True
# bool2 = False
# print(bool1 == bool2)

"""arithmetic operations"""
# number = 3 + 4 * 5 ** 2 + 7
# print(number)
#
# number2 = (3 + 4) * (5 ** 2 + 7)
# print(number2)

# print(7 % 2)
# print(17 % 5)
# print(72 % 23)

# print(6**2)

# print(7 / 2)
# print(7 // 2)

# print(6 + 2)
# print(6 - 2)

"""variables and types"""
# user_id = "12tomsmith438"
# print(type(user_id))
#
# user_id = 234
# print(type(user_id))

# x = 3.9e-3
# x = 3.9e3
# print(x)
# name = input("Enter your name: ")
# print("Hello, ", name)
