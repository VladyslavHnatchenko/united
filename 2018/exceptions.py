"""tuples"""

countries = (
    ("Germany", 80.2, (("Berlin", 3.326), ("Hamburg", 1.718))),
    ("France", 66, (("Paris", 2.2), ("Marsel", 1.6)))
)

for country in countries:
    country_name, country_population, cities = country
    print("\nCountry: {} population: {}".format(country_name, country_population))
    for city in cities:
        city_name, city_population = city
        print("City: {} population: {}".format(city_name, city_population))

# users_list = ["Tom", "Bob", "Kate"]
# users_list = tuple(users_list)
# print(users_list)
# users_list[1] = "Tim"
# print(users_list)

# user = ("Tom", 23)
# print(user)
#
# users = ("Dick", )
# print(users)

"""list"""
# users = [
#     ["Tom", 29],
#     ["Alice", 33],
#     ["Bob", 27]
# ]
# for user in users:
#     for item in user:
#         print(item, end=" | ")

# user = list()
# user.append("Bill")
# user.append(41)
# user.append("Teddy")
# user.append(22)
# users.append(user)
# print(users)

# print(users[0])
# print(users[0][0])
# print(users)

# import copy
#
#
# users1 = ["Tom", "Bob", "Alice"]
# users2 = copy.deepcopy(users1)
# users2.append("Sam")
#
# print(users1)
# print(users2)

# numbers = [9, 21, 12, 1, 3, 15, 18]
# print(min(numbers))
# print(max(numbers))

# users = ["Tom", "Bob", "Alice", "Tom", "Bill", "Tom"]
# users.sort()
# users.reverse()
# print(users)

# users_count = users.count("Tom")
# print(users_count)

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 33]
# numbers2 = list(range(1, 10))
# if numbers == numbers2:
#     print("numbers equal to numbers2")
# else:
#     print("numbers is not equal to numbers2")

# companies = ["Microsoft", "Google", "Oracle", "Apple"]
# for item in companies:
#     print(item)

# i = 0
# while i < len(companies):
#     print(companies[i])
#     i += 1

# numbers = list(range(10))
# print(numbers)
# numbers1 = list(range(2, 8))
# print(numbers1)
# numbers2 = list(range(10, 2, -2))
# print(numbers2)

# numbers = [5] * 6
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# # numbers1 = []
# numbers2 = list(numbers)
# print(numbers2)

"""exceptions"""
# try:
#     number1 = int(input("Enter first number: "))
#     number2 = int(input("Enter second number:"))
#     if number2 == 0:
#         raise Exception("The second number not equals = 0")
#     print("The result of division:", number1/number2)
# except ValueError:
#     print("No correct data")
# except Exception as e:
#     print(e)
# print("Shut down")

# try:
#     number = int(input("Enter a number: "))
#     print("Enter a number: ", number)
# except ValueError as e:
#     print("Could not convert number", e)
# # finally:
# #     print("Block try completed")
# print("Shut down")
