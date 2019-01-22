"""strings"""
import os


def get_words(filename):
    with open(filename, encoding="utf8") as file:
        text = file.read()
    text = text.replace("\n", " ")
    text = text.replace(",", "").replace(".", "").replace("?", "").replace("!", "")
    text = text.lower()
    words = text.split()
    words.sort()
    return words


def get_words_dict(words):
    words_dict = dict()

    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict


def main():
    filename = input("Enter path to file: ")
    if not os.path.exists(filename):
        print("This path doesn't found")
    else:
        words = get_words(filename)
        words_dict = get_words_dict(words)
        print("Amount words: %d" % len(words))
        print("Amount unique words: %d" % len(words_dict))
        print("All words used")
        for word in words_dict:
            print(word.ljust(20), words_dict[word])


if __name__ == "__main__":
    main()

# phone = "+1-234-567-89-10"
# edited_phone = phone.replace("-", " ")
# print(edited_phone)
#
# edited_phone1 = phone.replace("-", "@")
# print(edited_phone1)
#
# edited_phone2 = phone.replace("-", "", 1)
# print(edited_phone2)

# string = input("Enter the number: ")
# if string.isnumeric():
#     number = int(string)
#     print(number)

# string = "hello world"
# for char in string:
#     print(char)

# string = "hello world"
# sub_string1 = string[:5]
# print(sub_string1 + '\n')
#
# sub_string2 = string[2:5]
# print(sub_string2 + '\n')
#
# sub_string3 = string[2:9:2]
# print(sub_string3 + '\n')

# c0 = string[0]
# print(c0)
# c11 = string[11]
# print(c11)
