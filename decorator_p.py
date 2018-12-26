from decimal import Decimal


class Fees(object):
    def __init__(self):
        """Constructor"""
        self._fee = None

    @property
    def fee(self):
        """We return the current commission - getter."""
        return self._fee

    @fee.setter
    def set_fee(self, value):
        """Set the amount of commission - setter."""
        if isinstance(value, str):
            self._fee = Decimal(value)
        elif isinstance(value, Decimal):
            self._fee = value


if __name__ == "__main__":
    f = Fees()

# from decimal import Decimal
#
#
# class Fees(object):
#     def __init__(self):
#         """Constructor"""
#         self._fee = None
#
#     def get_fee(self):
#         """We return the current commission."""
#         return self._fee
#
#     def set_fee(self, value):
#         """Set the amount of commission."""
#         if isinstance(value, str):
#             self._fee = Decimal(value)
#         elif isinstance(value, Decimal):
#             self._fee = value

# class Person(object):
#     def __init__(self, first_name, last_name):
#         """Constructor"""
#         self.first_name = first_name
#         self.last_name = last_name
#
#     @property
#     def full_name(self):
#         """Return full name"""
#         return "%s %s" % (self.first_name, self.last_name)


# class DecoratorTest(object):
#     """We're testing the usual method against @classmethod against @staticmethod."""
#
#     def __init__(self):
#         """Constructor"""
#         pass
#
#     def doubler(self, x):
#         print("multiply by 2")
#         return x*2
#
#     @classmethod
#     def class_tripler(klass, x):
#         print("multiply by 3: %s" % klass)
#         return x*3
#
#     @staticmethod
#     def static_quad(x):
#         print("multiply by 4")
#         return x*4
#
#
# if __name__ == "__main__":
#     decor = DecoratorTest()
#     print(decor.doubler(5))
#     print(decor.class_tripler(3))
#     print(DecoratorTest.class_tripler(3))
#     print(DecoratorTest.static_quad(2))
#     print(decor.static_quad(3))
#
#     print(decor.doubler)
#     print(decor.class_tripler)
#     print(decor.static_quad)


# import logging
#
#
# def log(func):
#     """Log which function is called."""
#
#     def wrap_log(*args, **kwargs):
#         name = func.__name__
#         logger = logging.getLogger(name)
#         logger.setLevel(logging.INFO)
#
#         # Open log file for writing.
#         fh = logging.FileHandler("%s.log" % name)
#         fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
#         formatter = logging.Formatter(fmt)
#         fh.setFormatter(formatter)
#         logger.addHandler(fh)
#
#         logger.info("Function calling: %s" % name)
#         result = func(*args, **kwargs)
#         logger.info("Result: %s" % result)
#         return func
#
#     return wrap_log
#
#
# @log
# def double_function(a):
#     """Multiply the received parameter."""
#     return a*2
#
#
# if __name__ == "__main__":
#     value = double_function(23)
#     value = double_function(3)

# def another_function(func):
#     """The function that accepts another function."""
#
#     def other_func():
#         val = "The result from %s is %s" % (func(), eval(func()))
#         return val
#     return other_func
#
#
# @another_function
# def a_function():
#     """Just a function"""
#     return "1+3.3"
#
#
# if __name__ == "__main__":
#     value = a_function()
#     print(value)

# def another_function(func):
#     """The function that accepts another function."""
#
#     def other_func():
#         val = "The result from %s is %s" % (func(), eval(func()))
#         return val
#     return other_func
#
#
# def a_function():
#     """Sample function"""
#     return "1+1"
#
#
# if __name__ == '__main__':
#     value = a_function()
#     print(value)
#
#     decorator = another_function(a_function)
#     print(decorator())
