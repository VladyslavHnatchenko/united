from collections import OrderedDict


d = {
    'banana': 3,
    'apple': 4,
    'pear': 1,
    'orange': 2
}

new_d = OrderedDict(sorted(d.items()))

print(new_d)

for key in new_d:
    print(key, new_d[key])


# from collections import namedtuple
#
#
# Parts = namedtuple('Parts', 'id_num desc cost amount')
# auto_parts = Parts(
#     id_num='1234',
#     desc='Ford Engine',
#     cost=1200.00,
#     amount=10
# )
# print(auto_parts)

# from collections import deque
# import string
#
#
# d = deque(string.ascii_lowercase)
# for letter in d:
#     print(letter)

# import collections
# from collections import defaultdict
#
# sentence = "The red for jumped over the fence and ran to the zoo for food"
# words = sentence.split(' ')
#
# d = defaultdict(int)
# for word in words:
#     d[word] += 1
#
#
# print(d)


# sentence = "The red for jumped over the fence and ran to the zoo for food"
# words = sentence.split(' ')
#
# reg_dict = {}
# for word in words:
#     if word in reg_dict:
#         reg_dict[word] += 1
#     else:
#         reg_dict[word] = 1
#
#
# print(reg_dict)

# from collections import Counter
#
# a = Counter('superfluous')
# print(a)
#
# counter = Counter('superfluous')
# print(counter['u'])

# import argparse
# import os
#
# from collections import ChainMap
#
#
# def main():
#     app_defaults = {
#         'username': 'admin',
#         'password': 'admin'
#     }
#
#     parser = argparse.ArgumentParser()
#     parser.add_argument('-u', '--username')
#     parser.add_argument('-p', '--password')
#     args = parser.parse_args()
#
#     command_line_arguments = {
#         key: value for key, value in vars(args).items() if value
#     }
#
#     chain = ChainMap(
#         command_line_arguments,
#         os.environ,
#         app_defaults
#     )
#
#     print(chain['username'])
#
#
# if __name__ == '__main__':
#     main()
#     os.environ['username'] = 'test'
#     main()

# from collections import ChainMap
#
#
# car_parts = {
#     'hood': 500,
#     'engine': 5000,
#     'front_door': 750
# }
#
# car_options = {
#     'A/C': 1000,
#     'Turbo': 2500,
#     'rollbar': 300
# }
#
# car_accessories = {
#     'cover': 100,
#     'hood_ornament': 150,
#     'seat_cover': 99
# }
#
# car_pricing = ChainMap(car_accessories, car_options, car_parts)
#
# print(car_pricing)
# print(car_pricing['hood'])
