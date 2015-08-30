__author__ = 'lissu1'

from string import ascii_lowercase, ascii_uppercase
#from enum import Enum

#Enum("mode", "UPPER LOWER PUNCTUATION")
my_punctuation = '!?,. ;"\''
input_string = '18,12312,171,763,98423,1208,216,11,500,18,241,0,32,20620,27,10'

mode = 'UPPER'

def main():
    for ch in input_string.split(','):
        decoder(ch)


# mode = 'UPPER'
def decoder(coded_ch):
    global mode
    if mode == 'UPPER':
        reminder = int(coded_ch) % 27
        if reminder != 0:
            decoded = ascii_uppercase[reminder-1]
            return print(decoded)
        else:
            mode = 'LOWER'
    elif mode == 'LOWER':
        reminder = int(coded_ch) % 27
        if reminder != 0:
            decoded = ascii_lowercase[reminder-1]
            return print(decoded)
        else:
            mode = 'PUNCTUATION'
    elif mode == 'PUNCTUATION':
        reminder = int(coded_ch) % 9
        if reminder != 0:
            decoded = my_punctuation[reminder-1]
            return print(decoded)
        else:
            mode = 'UPPER'


main()
