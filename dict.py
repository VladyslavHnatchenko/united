"""set"""
users = {"Tom", "Bob", "Alice"}
users2 = {"Sam", "Kate", "Bob"}

users3 = users.union(users2)
print(users3)

"""dict"""
# users = {
#     "+111": "Tom",
#     "+222": "Bob",
#     "+333": "Alice"
# }
# for key in users:
#     print(key, " - ", users[key])

# users = {
#     "+1111": "Tom",
#     "+2222": "Bob",
#     "+5555": "Alice"
# }
# key = "+5555"
# user = users.pop(key)
# print(user)
#
# user = users.pop("+4444", "Unknown user")
# print(user)

# users = {
#     "+23dsf": "Tom",
#     "+fvdf23": "Bob",
#     "+fdver12": "Alice",
# }
#
# key = "+44444"
# if key in users:
#     user = users[key]
#     print(user)
# else:
#     print("Element not found")

# users = {
#     "+23dsf": "Tom",
#     "+fvdf23": "Bob",
#     "+fdver12": "Alice",
# }
# print(users["+fdver12"])
# users["+fvdf23"] = "Bob Smith"
# print(users["+fvdf23"])

# users_tuple = (
#     ("+12dsf323r32", "Chuck"),
#     ("+rfger232323", "Gram"),
#     ("+fwerfk12131", "Den"),
# )
# users_dict = dict(users_tuple)
# print(users_dict)

# users_list = [
#     ["+12321321312", "Tom"],
#     ["+35323223234", "Bob"],
#     ["+33231323000", "Alice"]
# ]
# users_dict = dict(users_list)
# print(users_dict)
