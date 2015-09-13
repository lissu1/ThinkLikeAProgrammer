__author__ = 'lissu1'
import unittest


# temp_number_holder = 0


def insertion_sort(for_sorting):
    array_for_sorting = for_sorting
    for index in range(0, len(array_for_sorting)):
        for second_index in range(index+1, len(array_for_sorting)):
            if array_for_sorting[index] > array_for_sorting[second_index]:
                temp_number_holder = array_for_sorting[index]
                array_for_sorting[index] = array_for_sorting[second_index]
                array_for_sorting[second_index] = temp_number_holder
    return array_for_sorting


#
#    print(insertion_sort(array_f_sorting))


class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        array_f_sorting = [3, 5, 1, 22, 4, 399, 211, 43]
        self.assertEqual(insertion_sort(array_f_sorting), [1, 3, 4, 5, 22, 43, 211, 399])

if __name__ == "__main__":
    unittest.main()
