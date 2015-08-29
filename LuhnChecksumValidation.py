__author__ = 'lissu1'

# Luhn algorithm

# 980262438244055
def luhn_checksum_validation():
    """
    Tells if luhn checksum is valid

    """

    input_list = []
    odd_length_checksum = 0
    even_length_checksum = 0
    sum_of_digits = 0
    position = 0

    while True:
        read_input = input()
        if read_input == "":
            break
        double_digit = str(int(read_input) * 2)
        for char in double_digit:
            sum_of_digits += int(char)
        print("sum of digits ", sum_of_digits)
        input_list.append(read_input)

        if position % 2 == 0:
            even_length_checksum += sum_of_digits
            odd_length_checksum += int(read_input)
        else:
            even_length_checksum += int(read_input)
            odd_length_checksum += sum_of_digits

        position += 1
        sum_of_digits = 0

    if position % 2 == 0:  # loop adds 1 to position after finishing
        checksum = even_length_checksum
    else:
        checksum = odd_length_checksum

    if checksum % 10 == 0:
        print("checksum %s is divisible by 10" % checksum)
    else:
        print("checksum %s is not divisible by 10" % checksum)
    print(input_list)

luhn_checksum_validation()