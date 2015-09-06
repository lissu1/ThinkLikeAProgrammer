__author__ = 'lissu1'

array_for_sorting = [3, 5, 1, 22, 4, 399, 211, 43]
# temp_number_holder = 0


def insertion_sort():
    for index in range(0, len(array_for_sorting)):
        for second_index in range(index+1, len(array_for_sorting)):
            if array_for_sorting[index] > array_for_sorting[second_index]:
                temp_number_holder = array_for_sorting[index]
                array_for_sorting[index] = array_for_sorting[second_index]
                array_for_sorting[second_index] = temp_number_holder
    return array_for_sorting


print(insertion_sort())


