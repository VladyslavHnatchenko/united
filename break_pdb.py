import random

from rest_framework import throttling


class RandomRateThrottle(throttling.BaseThrottle):
    def allow_request(self, request, view):
        return random.randint(1, 10) != 1


# import util
# import pdb
#
#
# filename = __file__
# pdb.set_trace()
# filename_path = util.get_path(filename)
# print(f'path = {filename_path}')


# import os
# import pdb
#
#
# def get_path(filename):
#     """Return file's path or empty string if no path."""
#     head, tail = os.path.split(filename)
#     return head
#
#
# filename = __file__
# pdb.set_trace()
# filename_path = get_path(filename)
# print(f'path = {filename_path}')
