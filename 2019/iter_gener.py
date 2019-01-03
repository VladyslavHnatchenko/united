"""classes and objects"""


class Figure:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def info(self):
        print("Figure")
        print("Color: " + self.color)


class Rectangle(Figure):
    def __init__(self, color, width=100, height=100):
        super().__init__(color)
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def info(self):
        print("Rectangle")
        print("Color: " + self.color)
        print("Width: " + str(self.width))
        print("Height:" + str(self.height))
        print("Square: " + str(self.square()))


# class Figure:
#     def __init__(self, color):
#         self.color = color
#
#     def get_color(self):
#         return self.color
#
#
# class Rectangle(Figure):
#     def __init__(self, color, width=100, height=100):
#         super().__init__(color)
#         self.width = width
#         self.height = height
#
#     def square(self):
#         return self.width * self.height


# class Rectangle:
#     def __init__(self, color="green", width=100, height=100):
#         self.color = color
#         self.width = width
#         self.height = height
#
#     def square(self):
#         return self.width * self.height

# class Rectangle:
#     color = "green"
#     width = 100
#     height = 100
#
#     def square(self):
#         return self.width * self.height


# class C:
#     pass

"""iterator & generator"""
"""generators"""
# def simple_generator(val):
#     while val > 0:
#         val -= 1
#         yield 1
#
#
# gen_iter = simple_generator(5)
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))
# print(next(gen_iter))


"""iterators"""
# class SimpleIterator:
#     def __iter__(self):
#         return self
#
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration
#
#
# s_iter2 = SimpleIterator(5)
# for i in s_iter2:
#     print(i)

# class SimpleIterator:
#     def __init__(self, limit):
#         self.limit = limit
#         self.counter = 0
#
#     def __next__(self):
#         if self.counter < self.limit:
#             self.counter += 1
#             return 1
#         else:
#             raise StopIteration
#
#
# s_iter1 = SimpleIterator(3)
# print(next(s_iter1))
# print(next(s_iter1))
# print(next(s_iter1))

# num_list = [1, 2, 3, 4, 5]
# for i in num_list:
#     print(i)
