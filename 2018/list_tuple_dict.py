"""Python classes"""


class Vehicle:
    """docstring"""

    def __init__(self, color, doors, tires, vtype):
        """Constructor"""
        self.color = color
        self.doors = doors
        self.tires = tires
        self.vtype = vtype

    def brake(self):
        """Stop the car"""
        return "%s braking" % self.vtype

    def drive(self):
        """Drive the car"""
        return "I'm driving a %s %s!" % (self.color, self.vtype)


if __name__ == "__main__":
    car = Vehicle("blue", 5, 4, "car")
    print(car.brake())
    print(car.drive())

    truck = Vehicle("red", 3, 6, "truck")
    print(truck.drive())
    print(truck.brake())

# x = "Mike"
# print(dir(x))

"""python string handling"""

# a = "Python is as simple as {0}, {1}, {2}".format("a", "b", "c")
# print(a)
#
# b = "Python is as simple as {1}, {0}, {2}".format("a", "b", "c")
# print(b)
#
# xy = {"x": 0, "y": 10}
# c = "Graph a point at where x={x} and y={y}".format(**xy)
# print(c)

# a = "%(value)s %(value)s %(value)s !" % {"value": "SPAM"}
# print(a)
#
# b = "%(x)i + %(y)i = %(z)i" % {"x": 1, "y": 2, "z": 3}
# print(b)

# print("%(lang)s is fun!" % {"lang": "Python"})

# my_string = "%i + %i = %i" % (1, 2, 3)
# print(my_string)
#
# float_string = "%f" % 1.23
# print(float_string)
#
# float_string2 = "%.2f" % 1.23
# print(float_string2)
#
# float_string3 = "%.2f" % 1.237
# print(float_string3)

# my_string = "I love %s" % "Python"
# print(my_string)
#
# var = "apples"
# new_string = "I eat %s" % var
# print(new_string)
#
# another_string = "I love %s and %s" % ("Python", var)
# print(another_string)

# my_string = "This's a string!"
# my_string.upper()
# print(my_string)
#
# dir(my_string)

# my_string = "abc"
# a = id(my_string)
# print(a)
#
# my_string = "def"
# b = id(my_string)
# print(b)
#
# my_string = my_string + "ghi"
# c = id(my_string)
# print(c)

# my_number = 123
# my_string = str(my_number)
# my_string2 = "Welcome in Python!"
# another_string = "Here a new text..."
# a_long_string = '''And this's ours
#                 new line
#                 in ternary brackets'''

"""dict"""
# my_dict = {}
# another_dict = dict()
#
# my_other_dict = {
#     "one": 1,
#     "two": 2,
#     "three": 3
# }
# print(my_other_dict["one"])
#
# my_dict = {
#     "name": "Mike",
#     "address": "123 Happy Way"
# }
# print(my_dict["name"])
#
# print("name" in my_dict)
# print("state" in my_dict)
# print(my_dict.keys())

"""tuple"""
# my_tuple = (1, 2, 3, 4, 5)
# a = my_tuple[0:3]
# print(a)
#
# another_tuple = tuple()
# abc = tuple([1, 2, 3])
# print(abc)

"""list"""
# my_list = [1, 2, 3]
# my_list2 = ["a", "b", "c"]
# my_list3 = ["a", 1, "Python", 5]
#
# # my_nested_list = [my_list, my_list2, my_list3]
# # print(my_nested_list)
#
# combo_list = my_list + my_list2 + my_list3
# # combo_list.sort()
# my_list3.sort()
# print(my_list3)
