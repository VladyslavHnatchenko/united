import re


silly_string = "the cat in the hat"
pattern = "the"

for match in re.finditer(pattern, silly_string):
    s = "Found '{group}' at {begin}:{end}".format(
        group=match.group(), begin=match.start(),
        end=match.end()
    )
    print(s)


# a = re.findall(pattern, silly_string)
# print(a)
#
# match = re.search(pattern, silly_string)
# print(match.group())

# text = "The ants go marching one by one"
#
# strings = ['the', 'one']
#
# for string in strings:
#     regex = re.compile(string)
#     match = re.search(regex, text)
#     if match:
#         print('Found "{}" in "{}"'.format(string, text))
#         text_pos = match.span()
#         print(text[match.start():match.end()])
#     else:
#         print('Did not find "{}"'.format(string))

# import re
#
#
# text = "The ants go marching one by one"
#
# strings = ['the', 'one']
#
# for string in strings:
#     match = re.search(string, text)
#     if match:
#         print('Found "{}" in "{}"'.format(string, text))
#         text_pos = match.span()
#         print(text[match.start():match.end()])
#     else:
#         print('Did not find "{}"'.format(string))

# text = 'abcdefghijk'

# parser = re.search('a[b-f]*f', text)
# print(parser.group())
