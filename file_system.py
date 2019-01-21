"""os"""
import os


os.rmdir("hello")
# os.mkdir("hello")

"""shelve"""
# import shelve
#
#
# FILENAME = "states2"
# with shelve.open(FILENAME) as states:
#     states["London"] = "Great Britain"
#     states["Paris"] = "France"
#     states["Berlin"] = "Germany"
#     states["Madrid"] = "Spain"
#
# with shelve.open(FILENAME) as states:
#     print(states["London"])
#     print(states["Madrid"])

"""pickle"""
# import pickle
#
#
# FILENAME = "users.dat"
#
# users = [
#     ["Tom", 28, True],
#     ["Alice", 23, False],
#     ["Bob", 34, False],
# ]
#
# with open(FILENAME, "wb") as file:
#     pickle.dump(users, file)
#
# with open(FILENAME, "rb") as file:
#     users_from_file = pickle.load(file)
#     for user in users_from_file:
#         print("Name:", user[0], "\tAge:", user[1], "\tMarried:", user[2])

# FILENAME = "user.dat"
#
# name = "Tom"
# age = 19
#
# with open(FILENAME, "wb") as file:
#     pickle.dump(name, file)
#     pickle.dump(age, file)
#
# with open(FILENAME, "rb") as file:
#     name = pickle.load(file)
#     age = pickle.load(file)
#     print("Name: ", name, "\tAge: ", age)

"""csv"""
# import csv
#
# FILENAME = "users.csv"
#
# users = [
#     ["Tom", 28],
#     ["Alice", 23],
#     ["Bob", 34],
# ]
#
# with open(FILENAME, "w", newline="") as file:
#     writer = csv.writer(file)
#     writer.writerows(users)
#
# with open(FILENAME, "a", newline="") as file:
#     user = ["Sam", 31]
#     writer = csv.writer(file)
#     writer.writerow(user)

"""work with file"""
# FILENAME = "messages.txt"
# messages = list()
#
# for i in range(4):
#     message = input("Enter string " + str(i+1) + ": ")
#     messages.append(message + "\n")
#
# with open(FILENAME, "a") as file:
#     for message in messages:
#         file.write(message)
#
# print("Reading message")
# with open(FILENAME, "r") as file:
#     for message in file:
#         print(message, end="")


# with open("hello.txt", "r") as file:
#     str1 = file.readline()
#     print(str1, end="")
#     str2 = file.readline()
#     print(str2)

# with open("hello.txt", "a") as file:
#     file.write("\ngood buy, world")

# with open("hello.txt", "w") as file:
#     file.write("Hello world" * 3)

# try:
#     some_file = open("hello2.txt", "w")
#     try:
#         some_file.write("hello world")
#     except Exception as e:
#         print(e)
#     finally:
#         some_file.close()
# except Exception as ex:
#     print(ex)

# my_file = open("hello.txt", "w")
# my_file.close()
