__author__ = 'lissu1'

import string

# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.punctuation)
# print(string.whitespace)

lowercase = string.ascii_lowercase
for index in range(len(lowercase)):
    print(index, lowercase[index])
