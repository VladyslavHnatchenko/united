"""object"""


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Invalid age")

    def display_info(self):
        print("Name:", self.__name, "\tAge:", self.__age)


tom = Person("Tom", 23)
print(tom)

"""polymorphism"""
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def name(self):
#         return self.__name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         def age(self, age):
#             if age in range(1, 100):
#                 self.__age = age
#             else:
#                 print("Invalid age")
#
#     def display_info(self):
#         print("Name:", self.__name, "\tAge:", self.__age)
#
#
# class Employee(Person):
#     # constructor definition
#     def __init__(self, name, age, company):
#         Person.__init__(self, name, age)
#         self.company = company
#
#     # override method display_info
#     def display_info(self):
#         Person.display_info(self)
#         print("Company:", self.company)
#
#
# class Student(Person):
#     # constructor definition
#     def __init__(self, name, age, university):
#         Person.__init__(self, name, age)
#         self.university = university
#
#     # override method display_info
#     def display_info(self):
#         print("Student", self.name, "studied in university", self.university)
#
#
# people = [Person("Tom", 23), Student("Bob", 19, "Harvard"), Employee("Sam", 35, "Google")]
#
# for person in people:
#     person.display_info()
#     print()

"""inheritance"""


# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print("Invalid age")
#
#     @property
#     def name(self):
#         return self.__name
#
#     def display_info(self):
#         print("Name:", self.__name, "\tAge:", self.__age)
#
#
# class Employee(Person):
#     def details(self, company):
#         print(self.name, "work in company", company)
#
#
# tom = Employee("Tom", 23)
# tom.details("Google")
# tom.age = 33
# tom.display_info()

"""oop"""
# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def set_age(self, age):
#         if age in range(1, 100):
#             self.__age = age
#         else:
#             print("Invalid age")
#
#     def get_age(self):
#         return self.__age
#
#     def get_name(self):
#         return self.__name
#
#     def display_info(self):
#         print("Name:", self.__name, "\tAge:", self.__age)


# tom = Person("Tom", 23)
# tom.__age = 43
# tom.display_info()
#
# tom.set_age(-3483)
# tom.display_info()
#
# tom.set_age(25)
# tom.display_info()


# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def display_info(self):
#         print("Hi, my name is", self.name)
#
#
# person1 = Person("Tom")
# person1.display_info()
#
# person2 = Person("Sam")
# person2.display_info()

# class Person:
#     name = "Tom"
#
#     def display_info(self):
#         print("Hi, my name is", self.name)
#
#
# person1 = Person()
# person1.display_info()
#
# person2 = Person()
# person2.name = "Sam"
# person2.display_info()
