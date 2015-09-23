__author__ = 'lissu1'
import unittest


array_f_sorting = [3, 5, 1, 22, 4, 399, 211, 43]
array_for_mode = [4, 7, 9, 7, 9, 9, 8, 3, 3, 3, 3, 10, 9]


def insertion_sort(for_sorting):
    array_for_sorting = for_sorting
    for index in range(0, len(array_for_sorting)):
        for second_index in range(index+1, len(array_for_sorting)):
            if array_for_sorting[index] > array_for_sorting[second_index]:
                temp_number_holder = array_for_sorting[index]
                array_for_sorting[index] = array_for_sorting[second_index]
                array_for_sorting[second_index] = temp_number_holder
    return array_for_sorting


def average_grade(grades):
    sum_of_grades = 0
    for grade in grades:
        sum_of_grades += grade
#    print(sum_of_grades)
#    print(len(grades))
    aver_grade = float(sum_of_grades) / float(len(grades))
    return aver_grade


def mode(numberlist):
    """
    :desc gets list of numbers and finds the one that appears most
    :param numberlist: array of numbers, each number is between 1 - 10
    :return: number from numberlist that appears the most
    """
    helper_array_count_numbers = [0]*10
    for number in numberlist:
        helper_array_count_numbers[number-1] +=1
    return helper_array_count_numbers.index(max(helper_array_count_numbers))+1


class TestMethods(unittest.TestCase):
    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(array_f_sorting), [1, 3, 4, 5, 22, 43, 211, 399])

    def test_average_grade(self):
        self.assertEqual(average_grade(array_f_sorting), 86)

    def test_mode(self):
        self.assertEqual(mode(array_for_mode), 3, "Mode väärtus ei ole kolm")


if __name__ == "__main__":
    unittest.main()

